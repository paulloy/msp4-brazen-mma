/*globals $:false */
/*jshint esversion: 6 */

// search query
let $q = $('#q');


var mouseOverOM = false;
$('#overlay-menu').mouseenter(function() {
    mouseOverOM = true;
}).mouseleave(function() {
    mouseOverOM = false;
    if (!(inputFocused)) {
        $('#block-content').fadeIn();
        $('#overlay-menu').fadeOut();
    }
});


// display #menu-overlay on focus
var inputFocused = false;
$q.on('focus', function() {
    inputFocused = true;
    $('#block-content').fadeOut();
    $('#overlay-menu').fadeIn();
});

// hide #menu-overlay on blur
$q.on('blur', function() {
    inputFocused = false;
    if (!(mouseOverOM)) {
        $('#block-content').fadeIn();
        $('#overlay-menu').fadeOut();
    }
});

// ajax calls on input
$q.on('input', function() {

    // So href works on development and deployed version
    var location = window.location.protocol + '//' + window.location.host;

    $('#product-row').empty();
    var value = $(this).val();
    
    $('#search-value').empty();
    $('#search-value').text(value);
    $('#product-row').append(`<p id="searching-loader" class="text-white p-5 w-100 text-center h3">Searching <i class="fas fa-spinner fa-pulse"></i></p>`);

    // Display nothing if input is empty
    if (value.length > 0) {
        // Timeout will prevent too many ajax calls.
        clearTimeout(window.timer);
        window.timer=setTimeout(function() {
            $.ajax({
                method: "GET",
                url: `/products/ajax_q/?q=${ value }`,
                async: true,
                success: function(response) {
                    var product = JSON.parse(response);
                    

                    if (product.length === 0) {
                        $('#product-row').empty();
                        $('#product-row').append(`<p class="text-white text-paragraph p-5 text-center">No results found. Please try searching for something else.</p>`);
                        $('#view-full-results').empty();
                    } else {
                        $('#view-full-results').empty();
                        $('#view-full-results').append(`<p class="text-white p-5"><a class="float-right btn btn-primary" href="/products/?q=${value}">View full results?</a></p>`);
                        $('#product-row').empty();
                        var column;
                        for (var i=0; i<4; i++) {
                            if (product[i].fields.price != product[i].fields.rrp) {
                                column = `
                                    <a href="${location}/products/${ product[i].pk }" class="p-2 my-3 mx-auto product-style position-relative d-flex flex-column">                            
                                        <div class="p-0 d-flex justify-content-center">
                                            <img class="img-thumbnail" src="${ mediaPrefix }${ product[i].fields.image }" alt="${ product[i].fields.name }">
                                        </div>
                                        <strong class="my-0 py-2 text-center text-black">${ product[i].fields.name }</strong>
                                        <div class="position-absolute d-flex justify-content-center w-100 p-3">
                                            <p class="mx-2 d-inline-block bold my-0 text-danger">£${ product[i].fields.price } <i class="fas fa-tags"></i></p>
                                            <p class="mr-2 d-inline-block bold my-0 text-muted strike-through">£${ product[i].fields.rrp }</p>
                                        </div>
                                    </a>`;
                                } else {
                                    column = `
                                        <a href="${location}/products/${ product[i].pk }" class="p-2 my-3 mx-auto product-style position-relative d-flex flex-column">                            
                                            <div class="p-0 d-flex justify-content-center">
                                                <img class="img-thumbnail" src="${ mediaPrefix }${ product[i].fields.image }" alt="${ product[i].fields.name }">
                                            </div>
                                            <strong class="my-0 py-2 d-inline-block text-center text-black">${ product[i].fields.name }</strong>
                                            <div class="position-absolute w-100 d-flex justify-content-center p-3">
                                                <p class="mt-2 mb-0 bold text-center d-inline-block text-dark">£${ product[i].fields.price }</p>
                                            </div>
                                        </a>`;                                              
                                }
                            $('#product-row').append(column);
                            }                             
                        }                        
                    }                    
            });
        }, 1000); // 1.0s delay
    } else {
        $('#product-row').empty();
        $('#view-full-results').empty();
    }
});