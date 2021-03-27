
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
let add = `Add to bag <i class="fas fa-shopping-bag"></i>`;
let spinner = `ADDING TO BAG <i class="fas fa-spinner fa-pulse"></i>`;
$('#add-to-bag-submit').click(function(e) {
    e.preventDefault();
    $(this).html(spinner);
    setTimeout(function(){
        if ($('#please-select-size').length != 0) {
            if ($('#size_input').val() == 'false') {
                $('#please-select-size').show(); 
                $('#add-to-bag-submit').html(add);  
            } else {
                $('#please-select-size').hide();
                $('#add-to-bag-form').submit(); 
            }
        } else {
            // If product has no sizes, then submit
            $('#add-to-bag-form').submit();     
        }        
        $('#add-to-bag-submit').html(add);
    }, 300);
});

// deleting product 
$('#confirm-delete').click(function() {
    $('#update-delete-product').hide();
    $('#delete-product').show();
});
$('#cancel-delete').click(function() {
    $('#update-delete-product').show();
    $('#delete-product').hide();
});

// open/close #size-chart 

$('#open-size-chart').click(function() {
    $('#size-chart').fadeIn();
});
$('#close-size-chart').click(function() {
    $('#size-chart').fadeOut();
});