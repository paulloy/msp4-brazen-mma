/*globals $:false */
/*jshint esversion: 6 */

// order-history

$('.toggle-order-details').click(function() {
    $(this).parent().next().slideToggle();
});

// delivery-info

let countrySelected = $('#id_default_country').val();

if (!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}

$('#id_default_country').change(function() {
    countrySelected = $(this).val();

    if (!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});