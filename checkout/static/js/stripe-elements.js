var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements()

var style = {
    base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neve", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle validation errors
card.addEventListener('change', function(e) {
    var errorDiv = document.getElementById('card-errors');
    if (e.error) {
        var html = `
            <span class="icon text-danger" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span class="text-danger">${e.error.message}</span>`;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});

// handle form submission
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(e) {
    e.preventDefault();
    card.update({'disabled': true});
    $('#submit-form').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var html = `
                <span class="icon text-danger" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span class="text-danger">${result.error.message}</span>`;
            errorDiv.innerHTML = html;
            card.update({'disabled': false});
            $('#submit-form').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});