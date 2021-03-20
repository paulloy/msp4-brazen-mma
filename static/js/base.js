$('#product-menu ul li').click(function() {
    $(this).find('.product-menu-submenu').toggle();
});

let navOpen = false;
$('#navbar-toggle, #navbar-toggle-mobile').click(function() {
    if (navOpen === false) {
        $('#product-menu-tablet').show().animate({
            right: 0
        }, 300, function() {
            navOpen = true;
        });
    } else {
        $('#product-menu-tablet').animate({
            right: '-12.5rem'
        }, 300, function() {
            navOpen = false;
            $('#product-menu-tablet').hide();
        });
    }
});

$('#product-menu-tablet ul li').click(function() {
    $(this).find('.product-menu-submenu').toggle();
});


// toggle includes/header.html menus
var searchMenuSmOpen = false;
var bagSmMenuOpen = false;
var sideNavOpen = false;

$('#toggle-sm-search').click(function() {
    if (searchMenuSmOpen) {
        $('#search-menu-sm').fadeOut();
        searchMenuSmOpen = false;
        if (!(bagSmMenuOpen && sideNavOpen)) {
            $('#block-content').fadeIn();
        }
    } else {
        $('#search-menu-sm').fadeIn();
        searchMenuSmOpen = true;
        $('#block-content').fadeIn();
        $('#bag-sm-menu').fadeOut();
        bagSmMenuOpen = false;
        $('#side-nav').fadeOut();
        sideNavOpen = false;
    }
});
$('#toggle-sm-bag').click(function() {
    if (bagSmMenuOpen) {
        $('#bag-sm-menu').fadeOut();
        bagSmMenuOpen = false;
        if (!(bagSmMenuOpen && sideNavOpen)) {
            $('#block-content').fadeIn();
        }
    } else {
        $('#bag-sm-menu').fadeIn();
        bagSmMenuOpen = true;
        $('#block-content').fadeOut();
        $('#search-menu-sm').fadeOut();
        searchMenuSmOpen = false;
        $('#side-nav').fadeOut();
        sideNavOpen = false;
    }
});
$('#toggle-side-nav').click(function() {
    if (sideNavOpen) {
        $('#side-nav').fadeOut();
        sideNavOpen = false;
        if (!(bagSmMenuOpen && sideNavOpen)) {
            $('#block-content').fadeIn();
        }
    } else {
        $('#side-nav').fadeIn();
        sideNavOpen = true;
        $('#block-content').fadeOut();
        $('#search-menu-sm').fadeOut();
        searchMenuSmOpen = false;
        $('#bag-sm-menu').fadeOut();
        bagSmMenuOpen = false;
    }
});
$('#block-content').click(function() {
    $('#search-menu-sm').fadeOut();
    searchMenuSmOpen = false;
});
/* ------------------------------------- */

// toggle menus within header
var toggleAccountOpen = false;
var toggleBagMenuOpen = false;

$('#toggle-account').click(function() {
    if (toggleAccountOpen) {
        $('#account').slideUp();
        toggleAccountOpen = false;
        if (!(toggleAccountOpen && toggleBagMenuOpen)) {
            $('#product-menu').fadeIn();
        }
    } else {
        $('#account').slideDown();
        $('#bag-menu').fadeOut();
        $('#product-menu').fadeOut();
        toggleAccountOpen = true;
        toggleBagMenuOpen = false;
    }
});

$('#toggle-bag-menu').click(function() {    
    if (toggleBagMenuOpen) {
        $('#bag-menu').slideUp();
        toggleBagMenuOpen = false;
        if (!(toggleAccountOpen && toggleBagMenuOpen)) {
            $('#product-menu').fadeIn();
        }
    } else {
        $('#bag-menu').slideDown();
        $('#account').fadeOut();
        $('#product-menu').fadeOut();
        toggleBagMenuOpen = true;
        toggleAccountOpen = false;
    }
});



// search query
let $q = $('#q');

// display #menu-overlay on focus
var inputFocused = false;
$q.on('focus', function() {
    inputFocused = true;
    $('#block-content').fadeOut();
    $('#overlay-menu').fadeIn();
});

// ajax calls on input
$q.on('input', function() {

    // So href works on development and deployed version
    var location = window.location.protocol + '//' + window.location.host;

    $('#product-row').empty();
    var value = $(this).val();
    
    $('#search-header').empty();
    var header = `<h3 class="text-white text-center w-100 p-4">Search Results for "${value}"</h3>`;
    $('#search-header').append(header);
    $('#product-row').append(`<p class="text-white position-absolute p-5 w-100 text-center h3">Searching <i class="fas fa-spinner fa-pulse"></i></p>`);

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
                        $('#product-row').append(`<p class="text-white p-5 text-center">No results found. Please try searching for something else.</p>`);
                        $('#view-full-results').empty();
                    } else {
                        $('#view-full-results').empty();
                        $('#view-full-results').append(`<p class="text-white p-5"><a class="float-right h3" href="/products/?q=${value}">View full results?</a></p>`);
                        $('#product-row').empty();
                        for (var i=0; i<4; i++) {
                            if (product[i].fields.price != product[i].fields.rrp) {
                                var column = `
                                    <a href="${location}/products/${ product[i].pk }" class="product h-100 col-xl-3 p-2 col-lg-6 carousel-cell d-flex flex-column align-items-center">                            
                                        <div class="img-container">
                                            <img src="${location}/media/${ product[i].fields.image }" alt="${ product[i].fields.name }">
                                        </div>
                                        <p class="my-0 py-2 text-center">${ product[i].fields.name }</p>
                                        <div class="d-flex m-0 py-2 justify-content-between align-items-center">
                                            <strike class="price pl-2 text-left text-muted">£${ product[i].fields.rrp }</strike>
                                            <p class="text-right pr-2 price">£${ product[i].fields.price } <i class="fas fa-tags"></i></p>
                                        </div>
                                    </a>`;
                                } else {
                                    var column = `
                                        <a href="${location}/products/${ product[i].pk }" class="product p-2 h-100 col-xl-3 col-lg-6 carousel-cell d-flex flex-column align-items-center">                            
                                            <div class="img-container">
                                                <img src="${location}/media/${ product[i].fields.image }" alt="${ product[i].fields.name }">
                                            </div>
                                            <p class="my-0 py-2">${ product[i].fields.name }</p>
                                            <p class="my-0 mx-2 text-right py-2 price">£${ product[i].fields.price }</p>
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

// Work on accessibility when focusing by keyboard
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

// hide #menu-overlay on blur
$q.on('blur', function() {
    inputFocused = false;
    if (!(mouseOverOM)) {
        $('#block-content').fadeIn();
        $('#overlay-menu').fadeOut();
    }
});
