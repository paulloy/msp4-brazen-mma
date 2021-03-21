# Testing

## bag

### Test events 
*21/03/21*

| Event | Expected Response | Pass / Fail ? |
| ----- | ----------------- |   :-----:   |
| Update quantity of product with a value beyond the min/max values of 1 and 99. | Do not submit form. Display "Value must be less than or equal to 99". | Pass |
| Update quantity of product with a non-int number. | Do not submit form. Display "Please enter a valid value". | Pass |
| Update quantity of product with a valid value. | Call {% url 'adjust_bag' <product_id> %} and redirect to {% url 'view_bag' %}. Display toast. | Pass |
| Using Dev tools, change type of input from number to text, then submit form. | Redirect to {% url 'view_bag' %} and display error toast. | Fail |
| Remove product from bag | Redirect to {% url 'view_bag' %} and display toast confirming product removal. Product should now be absent from the bag. | Pass |
| Using Dev tools, delete csrf_token input and submit update form. | Display 403 Forbidden error. | Pass |
| Using Dev tools, change update forms action so an invalid product_id is submitted. | Redirect to {% url 'view_bag' %} and display error toast. | Fail |
| Using Dev tools, change value of hidden size input for remove form to a value that does not exist in the bag. | Redirect to {% url 'view_bag' %} and display error toast. | Fail |
| Select 'Keep Shopping'. | Direct user to {% url 'products' %} | Pass |
| Select 'Checkout'. | Direct user to {% url 'checkout' %} | Pass |
| Select product image, or product name. | Direct user to {% url 'product_details' <product_id> %} (The products individual product page) | Pass |
| Select arrows next to quantity input. | Adjust value within quantity input ± 1. Do not change value to a number beyond the min/max range. | Pass |
| Access bag/remove/<product_id> by direct url input. | Redirect to {% url 'home %} and display error toast. | Fail |
| Access bag/add/<product_id> by direct url input. | Redirect to {% url 'home %} and display error toast. | Fail |
| Access bag/adjust/<product_id> by direct url input for a product that is not in the bag. | Redirect to {% url 'home %} and display error toast. | Fail |
| Bag is empty. | Display message that bag is currently empty. Hide Checkout button. | Pass |