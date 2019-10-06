# Testing

## HTML

HTML validated with W3 [validator](https://www.w3schools.com/) with no errors.

### Manual Testing

The following features were checked on these pages.

#### Base.html

- Login

  Message appears after login.

  Only visible when logged out

- Logout

  Message appears after logout.

  Only visible when logged in.

- Links

  Social links open a new window. They open the respective home pages since there is no company to have an account.

- The era selectors properly filter the catalogue results.

  

#### Register

- From both login page and from register link the form displays correctly.
- The registration form returns a logged in user to the index page.
- The user details are properly passed to the database.
- On completion the registration form returns the user to the Index page already logged in. 

#### Auctions

- Pictures display correctly with relevant details displayed properly.
- Bid form present only if auction in progress.
- Bid form functions as expected. 

#### Blog

- The blog entries are correctly displayed


#### Reviews

- The reviews are correctly displayed.


#### How it Works

- Displays the correct information.


#### Payment

- Displays the forms in the correct sequence.

- Passes the information correctly through the payment flow.

- Does not retain any of the financial details, only the addresses and the success or faliure of the transaction.


#### Footer

- The social media links open correctly and in a new window,

- The information links display the correct information.

  

## CSS

CSS validated with [Jigsaw](https://jigsaw.w3.org/css-validator/validator.html.en) and passed as CSS level 3 + SVG with 6 warnings on main.css. 1 warning on the font import and 5 on vendor extensions. The numerous warnings on vendor CSS have been ignored.

## Python

The code was developed in VS Code with pylint activated, all flagged problems were rectified during development.

## JavaScript

The minimal non-vendor JavaScript has been proved by both use and testing of other features.

## Chrome Audit Ratings

Performance 61%

Accessibility 93%

Best Practices 86%

SEO 89%