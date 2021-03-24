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