
// add extra script. pointer events set to none on input
let quantityValue = parseInt(document.getElementById('quantity').value);
$('#quantity-sub').click(function() {
    if (quantityValue > 1) {
        quantityValue = quantityValue - 1;
        $('#quantity').val(quantityValue);
    }
});
$('#quantity-add').click(function() {
    if (quantityValue < 99) {
        quantityValue = quantityValue + 1;
        $('#quantity').val(quantityValue);
    }
});

// Selecting sizes

$('.size').click(function() {
    let size = $(this).text();
    $(this).addClass('active-size');
    $(this).siblings().removeClass('active-size');
    document.getElementById('size_input').value = size;
});

// check if a size has been selected
$('#add-to-bag-submit').click(function(e) {
    e.preventDefault();
    if ($('#please-select-size').length != 0) {
        if ($('#size_input').val() == 'false') {
            $('#please-select-size').show();
        } else {
            $('#please-select-size').hide();
            $('#add-to-bag-form').submit();
        }
    } else {
        // If product has no sizes, then submit
        $('#add-to-bag-form').submit();        
    }
});