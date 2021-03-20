
try {
    var messageValue = document.getElementById('message-value').value;
    var messageTag = document.getElementById('message-tag').value;
} catch(err) {
    /*
        This "try" will prevent the following console error from being logged:

        "Uncaught TypeError: Cannot read property 'value' of null"

        When there are no messages, the #message-value and #message-tag elements are
        not rendered by Django, so the above error gets logged to the console.
    */
}

$(function() {
    if (messageTag === 'success') {
        toastr.success(messageValue);
    } else if (messageTag === 'error') {
        toastr.error(messageValue);
    } else if (messageTag === 'info') {
        toastr.info(messageValue);
    } else if (messageTag === 'warning') {
        toastr.warning(messageValue);
    }
});

/*
    Toastr settings come from:
    https://github.com/CodeSeven/toastr
    https://codeseven.github.io/toastr/demo.html
*/

    toastr.options = {
        "closeButton": true,
        "debug": false,
        "newestOnTop": false,
        "progressBar": true,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }