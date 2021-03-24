/*globals $:false */
/*jshint esversion: 6 */

$('.quantity-add').click(function() {
    var val = $(this).prev().val();
    if (val < 99) {
        val = parseInt(val) + 1;
        $(this).prev().val(val);
    }
});
$('.quantity-sub').click(function() {
    var val = $(this).next().val();
    if (val > 1) {
        val = parseInt(val) - 1;
        $(this).next().val(val);
    }
});