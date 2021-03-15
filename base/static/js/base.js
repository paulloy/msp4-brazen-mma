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

// bag menu
$('#open-bag-side-menu').click(function() {
    $('#bag-menu').show().animate({
        right: 0
    }, 300);
});
$('#close-bag-side-menu').click(function() {
    $('#bag-menu').animate({
        right: '-320px'
    }, 300, function() {
        $('#bag-menu').hide();
    });
});