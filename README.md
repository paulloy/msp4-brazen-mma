# Brazen MMA

The main goal of this project is the development of an e-commerce website with the full stack framework Django. Brazen Martial Arts 
sells martial arts equipment for Brazilian Jiu Jitsu, Muay Thai, and Mixed Martial Arts currently. Brazen Martial Arts is built with user expeierence
as one of our central goals. The user can search the website for products they would like to purchase, add them to a bag, and checkout using stripe payment.
When a user creates a profile all their past orders will be saved for them. Brazen Martial Arts hopes to provide a fulfilling user experience so as to 
encourage returning customers.

## UX

### Strategy

For this project the focus is on developing a MVP (Minimum Viable Product). After users interact with the project
and feedback is received a new plan can be developed for implementing additional features to the project.

#### Product Objectives

This project provides value to the retailer by:
    - Providing sales to consumers not lcoated within travel distince to the retailer.
    - Providing consumers with a good user expierience that aims to generate repeat purchases by returning customers.
    - The website can help the retailer with understanding their consumers needs.

#### User needs

    - A satisfying user expierience through apropriate use of content, interactivity, navigation, and feedback.
    - Easy checkout.
    - Access to previous order details.
    - A well designed database that allows customers to quickly find the product they are searching for.
    - Anonymous checkout.
    - Ability to create an account so user delivery details can be saved for a quicker future checkout.

### Scope

#### Functional Requirements

Browsing experience:
- The website should feature a search form so users can easily search for the product they are lokking for.
- A product menu should be added as an additonal method of searching through products.
- There should be functionality present for filtering products by gender, and sorting products by name or price.
- As more users visit the website their feedback can be used to improve the browsing experience.

Shopping bag & checkout
- Include functionality for adding products to a shopping bag that a user can view and adjust until they are ready to checkout with their selected products.
- There must be a secure checkout page with sufficient feedback so that few errors occur during this process.

Database:
- There must be a database for storing product information, user details, and orders.

Feedback:
- User actions should be met with feedback from the product so a user is confident wether or not their actions have be successfully performed.

Registration:
- There should be a form for new users to register an account. The user should receive an email confirming that their account has been created and welcoming them to our website.

Login:
- There should be a form for registered users to log into their accounts. There should be an option for users to stay logged in so if they are regular users, they will not have to continuously log in.

Profile Update:
- Users should be able to view all their past orders, and update user information.

#### Content Requirements

Branding:
- Website surface should conform to retailer branding.

Browsing:
- The display page for search results should display information on products that influence buying decisions. Prices, discounts, images, product name, product summary should be included so a user can easily compare products and decide what they want to purchase.

Cart & Checkout:
- The cart should display the same content as the search result display pages for products the user has added to the cart. The total cost of the order should be displayed, and the number of items in the cart.
The checkout should have the same content as the cart with additional fields for entering contact details, delivery details, and billing details.

Cart & Checkout Feedback:
- Messages should appear informing the user what item has been added to cart if it was successful. If there is an error, an error message should appear with a possible fix; if no fix is possible then contact the retailer.
- The user should be informed if their checkout has been successful and receive an email with a copy of their order details.







## Testing

[View Tests](TESTING.md)