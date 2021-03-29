/*globals $:false */
/*jshint esversion: 6 */

$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});

$(function() {
    $('#add-new-product-submit').removeAttr('disabled');
});

function jumptTo(){
    window.location.href = '#error-list';
}

$('#add-new-product-submit').click(function(e) {
    // Check for errors before submitting form
    e.preventDefault();

    var selectList = $('#inline-form .select');
    var stockList = $('#inline-form .numberinput');
    var errorList = $('#error-list');
    var selectListError = false;
    var stockListError = false;
    var duplicateError = false;
    var hasSizesError = false;
    var productStockError = false;
    var errorCounter = 0;
    var preventDuplicates = [];
    var hasSizes = false;
    var hasNoSizes = false;
    var getAttr;
       
    // empty error list.
    errorList.empty();                

    for (var i=0; i<selectList.length; i++) {

        var duplicateFound = false;

        selectList[i].classList.remove('error');
        stockList[i].classList.remove('error');                    
                    
        // true if a duplicate is found.
        duplicateFound = preventDuplicates.includes(selectList[i].value);

        if (selectList[i].value != '') {
            preventDuplicates.push(selectList[i].value);
            if ((selectList[i].value != 'false')) {
                hasSizes = true;
            } else {
                hasNoSizes = true;
            }
        }
                    
        // if a duplicate size has been added.
        if (duplicateFound) {
            // so error message displays once
            if (!(duplicateError)) {
                errorList.append('<li>You cannot have duplicate sizes.</li>');
            }
            duplicateError = true;  
            errorCounter++;                          
            var duplicatedValue = preventDuplicates.indexOf(selectList[i].value);
            getAttr = selectList[i].getAttribute('class');
            selectList[i].setAttribute('class', `error ${getAttr}`);
            selectList[duplicatedValue].setAttribute('class', `error ${getAttr}`);
        }
                    
        // if size is empty and stock is not.
        if (selectList[i].value == '' && stockList[i].value != '') {
            if (!(selectListError)) {
                // So error is displayed once.
                errorList.append('<li>You must select a size before you can update its stock.</li>');
            }
            selectListError = true;
            errorCounter++;
            getAttr = selectList[i].getAttribute('class');
            selectList[i].setAttribute('class', `error ${getAttr}`);
        }
        // if stock is empty and size is not.
        if (selectList[i].value != '' && stockList[i].value == '') {
            if (!(stockListError)) {
                errorList.append('<li>You must add the stock quantity to its size.</li>');
            }
            stockListError = true;
            errorCounter++;
            getAttr = stockList[i].getAttribute('class');
            stockList[i].setAttribute('class', `error ${getAttr}`);
        }
        
        // if a size and "false" are simultaneously selected.
        if ((hasSizes == true) && (hasNoSizes == true)) {
            if (!(hasSizesError)) {
                errorList.append('<li>You have selected both a size and "FALSE".</li>');
            }
            hasSizesError = true;
            errorCounter++;
        }
        // if no size has been added to the product.
        if (preventDuplicates.length == 0) {
            if (!(productStockError)) {
                errorList.append('<li>Please add at least one size to the product. If there are no sizes then select "FALSE" and add the product stock quantity.</li>');
            }
            productStockError = true;
            errorCounter++;
        }    
    }   
    if (errorCounter == 0) {
        $('#product-form').submit();
    } else {
        jumptTo();
    }      
});
