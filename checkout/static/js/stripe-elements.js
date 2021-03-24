/*globals $:false */
/*jshint esversion: 6 */

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

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

    $('#checkout-loader').fadeIn();

    card.update({'disabled': true});
    $('#submit-form').attr('disabled', true);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function(result) {
            var errorDiv = document.getElementById('card-errors');
            if (result.error) {
                var html = `
                    <span class="icon text-danger" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span class="text-danger">${result.error.message}</span>`;
                errorDiv.innerHTML = html;
                card.update({'disabled': false});
                $('#submit-form').attr('disabled', false);
                $('#checkout-loader').fadeOut();
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        // error message is displayed via django
        location.reload();
    });    
});