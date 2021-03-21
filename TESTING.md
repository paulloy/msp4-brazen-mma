# Testing

## bag

### Test events 
*21/03/21*

| ID | Event | Expected Response | Pass / Fail ? |
| ---- | ----- | --------------- |    :-----:    |
| 1.01 | Update quantity of product with a value beyond the min/max values of 1 and 99. | Do not submit form. Display "Value must be less than or equal to 99". | Pass |
| 1.02 | Update quantity of product with a non-int number. | Do not submit form. Display "Please enter a valid value". | Pass |
| 1.03 | Update quantity of product with a valid value. | Call {% url 'adjust_bag' <product_id> %} and redirect to {% url 'view_bag' %}. Display toast. | Pass |
| 1.04 | Using Dev tools, change type of input from number to text, then submit form. | Redirect to {% url 'view_bag' %} and display error toast. | Pass [1] |
| 1.05 | Remove product from bag | Redirect to {% url 'view_bag' %} and display toast confirming product removal. Product should now be absent from the bag. | Pass |
| 1.06 | Using Dev tools, delete csrf_token input and submit update form. | Display 403 Forbidden error. | Pass |
| 1.07 | Using Dev tools, change update forms action so an invalid product_id is submitted. | Redirect to {% url 'view_bag' %} and display error toast. | Pass [1] |
| 1.08 | Using Dev tools, change value of hidden size input for remove form to a value that does not exist in the bag. | Redirect to {% url 'view_bag' %} and display error toast. | Pass [1] |
| 1.09 | Select 'Keep Shopping'. | Direct user to {% url 'products' %} | Pass |
| 1.10 | Select 'Checkout'. | Direct user to {% url 'checkout' %} | Pass |
| 1.11 | Select product image, or product name. | Direct user to {% url 'product_details' <product_id> %} (The products individual product page) | Pass |
| 1.12 | Select arrows next to quantity input. | Adjust value within quantity input ± 1. Do not change value to a number beyond the min/max range. | Pass |
| 1.13 | Access bag/remove/<product_id> by direct url input. | Redirect to {% url 'home %} and display error toast. | Pass [1] |
| 1.14 | Access bag/add/<product_id> by direct url input. | Redirect to {% url 'home %} and display error toast. | Pass [1] |
| 1.15 | Access bag/adjust/<product_id> by direct url input for a product that is not in the bag. | Redirect to {% url 'home %} and display error toast. | Pass [1] |
| 1.16 | Bag is empty. | Display message that bag is currently empty. Hide Checkout button. | Pass |

 - [1]: As of commit *695f495*, these tests now Pass.