/*globals $:false */
/*jshint esversion: 6 */

$('#base-product-menu ul li').click(function() {
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
        $('#search-menu-sm').hide();
        searchMenuSmOpen = false;
        if (!(bagSmMenuOpen && sideNavOpen)) {
            $('#block-content').fadeIn();
        }
    } else {
        $('#search-menu-sm').show();
        $('#search-menu-sm form input').focus();
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

$('#toggle-sm-account').click(function() {
    $(this).siblings().slideToggle();
});

// toggle menus within header
var toggleAccountOpen = false;
var toggleBagMenuOpen = false;

$('#toggle-account').click(function() {
    if (toggleAccountOpen) {
        $('#account').slideUp();
        toggleAccountOpen = false;
        if (!(toggleAccountOpen && toggleBagMenuOpen)) {
            $('#base-product-menu').fadeIn();
        }
    } else {
        $('#account').slideDown();
        $('#bag-menu').fadeOut();
        $('#base-product-menu').fadeOut();
        toggleAccountOpen = true;
        toggleBagMenuOpen = false;
    }
});

$('#toggle-bag-menu').click(function() {    
    if (toggleBagMenuOpen) {
        $('#bag-menu').slideUp();
        toggleBagMenuOpen = false;
        if (!(toggleAccountOpen && toggleBagMenuOpen)) {
            $('#base-product-menu').fadeIn();
        }
    } else {
        $('#bag-menu').slideDown();
        $('#account').fadeOut();
        $('#base-product-menu').fadeOut();
        toggleBagMenuOpen = true;
        toggleAccountOpen = false;
    }
});

// toggle product menu lists
$('.toggle-sub-menu').click(function() {
    $(this).find('UL').slideToggle();
});


