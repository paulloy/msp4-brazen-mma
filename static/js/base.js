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
