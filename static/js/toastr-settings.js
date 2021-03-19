
var messageValue = document.getElementById('message-value').value;
var messageTag = document.getElementById('message-tag').value;

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

// Toastr settings come from:
// https://github.com/CodeSeven/toastr

    // add a close button to toast
    toastr.options.closeButton = true;

    // prevent duplicate toasts
    toastr.options.preventDuplicates = true;

    // add a progress bar
    toastr.options.progressBar = true;