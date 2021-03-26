$('.open-product-list').click(function(e) {
    e.preventDefault();
    let text = $(this).text();

    if (text === 'BJJ') {
        $('.display-none').hide();
        $('#bjj-list, #bjj-products').show();
    } else if (text === 'MMA') {
        $('.display-none').hide();
        $('#mma-list, #mma-products').show();        
    } else if (text === 'EQUIPMENT') {
        $('.display-none').hide();
        $('#equipment-list, #equipment-products').show();        
    } else if (text === 'MUAY THAI') {
        $('.display-none').hide();
        $('#muay-thai-list, #muay-thai-products').show();        
    }
});



// base-md header 
function smallHeaderBackgroundChange() {    
    var vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0) - 48;
    
    $('#block-content').on('scroll', function() {
        var scroll = $(this).scrollTop() > vh;

        if (scroll) {
            $('#header-md').addClass('header-bg-black');
        } else {
            $('#header-md').removeClass('header-bg-black');
        }
    });
}
$(function() {
    smallHeaderBackgroundChange();
});
$(window).resize(function() {
    smallHeaderBackgroundChange();
});