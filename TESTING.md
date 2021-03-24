# Testing

## bag

templates:
 - [Bag](bag/templates/bag/bag.html)

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

### Validation

#### CSS

stylesheets:
 - [bag.css](bag/static/css/bag.css)

*24/03/21*: 
 - All stylesheets passed validation.

#### JS

scripts:
 - [bag.js](bag/static/js/bag.js)

*24/03/21*: 
 - One undefined variable: $
 - One unused variable: $displayQuantity

## checkout

templates:
 - [Checkout Success](checkout/templates/checkout/checkout_success.html)
 - [Checkout](checkout/templates/checkout/checkout.html)

### Test events
*22/03/21*

| ID | Event | Expected Response | Pass / Fail ? |
| ---- | ----- | --------------- |    :-----:    |
| 2.01 | Anonymous User can checkout | Display {% url 'checkout_success' <order_id> %} with order confirmation. | Pass [2] |
| 2.02 | Submit form with empty required fields | Notify user to fill in required fields. | Pass |
| 2.03 | Submit form with empty payment field | Display error within the card div. | Pass |
| 2.04 | Submit form with empty optional fields | Display {% url 'checkout_success' <order_id> %} with order confirmation. | Pass |
| 2.05 | Submit form with empty optional fields | Display {% url 'checkout_success' <order_id> %} with order confirmation. | Pass |
| 2.06 | Submit form as a logged in user. | Display {% url 'checkout_success' <order_id> %} with order confirmation. | Pass |
| 2.07 | Return to checkout after successful checkout. | Redirect to {% url 'home %} | Pass [2] |
| 2.08 | Checkout with info saved. | Info should be auto filled for next checkout. | Pass |
| 2.09 | Select login as an anonymous user. | Direct user to {% url 'accounts_login' %} | Pass |
| 2.10 | Select 'adjust bag' button. | Direct user to {% url 'view_bag' %} | Pass |
| 2.11 | Select 'view order summary' button. | Toggle the order summary. (For small screen widths where order summary is hidden) | Pass |
| 2.12 | Access {% url 'checkout' %} by url with an empty bag. | Redirect the user to {% url 'home %} and display an error. | Pass [3] |
| 2.13 | Access {% url 'checkout_success' %} by url with invalid order ID. | Redirect the user to {% url 'home %} and display an error. | Pass [2] |
| 2.14 | Access {% url 'cache_checkout_data' %} by url. | Display 405 error. | Pass |
| 2.15 | Access {% url 'wh' %} by url. | Display 405 error. | Pass |
| 2.16 | Checkout with Stripe test card number: 4000002500003155. Fail authentication. | Display error within the card div. | Pass |

 - [2]: As of commit *7b5923e*, these tests now Pass.
 - [3]: As of commit *2486c93*, this test now Passes.
 - The patch to 2.12 fixed 2.07.
 - The expected response of test 2.14 & 2.15 was incorrect and has been updated. 

### Validation

#### CSS

stylesheets:
 - [checkout_success.css](checkout/static/css/checkout_success.css)
 - [checkout.css](checkout/static/css/checkout.css)

*24/03/21*: 
 - All stylesheets passed validation.

#### JS

scripts:
 - [bag.js](bag/static/js/bag.js)
 - [stripe-elements.js](bag/static/js/stripe-elements.js)

*24/03/21*:
 - bag.js:
    - One undefined variable: $

 - stripe-elements.js
    - Missing semicolon.
    - 'template literal syntax' is only available in ES6 (use 'esversion: 6').
    - undefined variable: $
    - undefined variable: Stripe

## profiles

templates:
 - [Profile Delivery Info](profiles/templates/profiles/delivery-info.html)
 - [Profile Order History](profiles/templates/profiles/order-history.html)

### Test events
*24/03/21*

| ID | Event | Expected Response | Pass / Fail ? |
| ---- | ----- | --------------- |    :-----:    |
| 3.01 | Selecting an order number | Direct user to {% url 'order_history' <order_numer> %} and display an info-message that this is a past order confirmation. | Pass |
| 3.02 | Selecting an order toggle button | Display a link to {% url 'order_history' <order_numer> %} titled 'View Order Summary.' Display a list of all products ordered. Display grand total of order. | Pass |
| 3.03 | Selecting 'View Order Summary.' | Direct user to {% url 'order_history' <order_numer> %} and display an info-message that this is a past order confirmation. | Pass |
| 3.04 | Selecting 'View Order Summary.' | Direct user to {% url 'order_history' <order_numer> %} and display an info-message that this is a past order confirmation. | Pass |
| 3.05 | Select a product name | Direct user to {% url 'product_details' <product_id> %} | Pass |
| 3.06 | Submit empty form. | Page should reload with the form containing no values. | Pass |
| 3.07 | Submit form with values added. | Page should reload with submitted fields autofilled. | Pass |
| 3.08 | Navigate to {% url 'profile_order_history' %} after updating default delivery info. | All the same orders should be displayed to the user. | Pass |
| 3.09 | Navigate to {% url 'checkout' %} after updating default delivery info. | Only the filled in fields should be automatically filled on the checkout form. | Pass |
| 3.10 | With no delivery info saved, place an order at the checkout and select 'save this delivery information' checkbox. | Default Delivery Info should now be autofilled upon returning to {% url 'profile_delivery_info %}. | Pass |

### Validation

#### CSS

stylesheets:
 - [profile.css](profiles/static/css/profile.css)

*24/03/21*: 
 - All stylesheets passed validation.

#### JS

scripts:
 - [profile.js](profiles/static/js/profile.js)

*24/03/21*:
- 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- Unnecessary semicolon.
- undefined variable: $
