
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