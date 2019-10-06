# Milestone 4

## [Gray and Sons Auction house]( https://ms4-auctionsite.herokuapp.com/)

Gray's is the online face of a notional auction house allowing customers to view lots, bid on them and ultimately to arrange shipping and pay for them.

A simple colour scheme coupled with straightforward navigation allow the pictures to draw viewers into the collections of antiques on offer. Taking second place to the products but clearly present are the latest blog posts advising customers of noteworthy products as they become available. For those who like these posts there is a newsletter signup link to alert them to make sure they don't miss an opportunity.

Further down the page, easily available and readily available are reviews, social media links and some background information on Gray's and their policies.

Live demo https://ms4-auctionsite.herokuapp.com/

GitHub Repository https://github.com/PeteWillmott/grays-auctionhouse



## Table of Contents

1. **UX**
2. **Features**
3. **Technologies** **Used**
4. **Testing**
5. **Database**
6. **Deployment**
7. **Credits**



### UX

#### User Goals

The customer is assumed to be an end user, for example a home owner looking for an antique for their own home or perhaps a collector looking for that special piece to finish their collection. 

Accordingly the site was designed for:

- Mobile friendly design, users don't want to have to sit at home until the auction is finished.
- Ease of navigation with broad categories available on the front page allowing for one click browsing.
- Display of individual and varied items by image not elaborate category structures to suit the private buyer rather than the trade insider.

#### Business Goals

The business is assumed to be a general antiques dealer rather than a specialist in some narrow subset of antiques.

- Mobile friendly design, customers probably won't bid if they can't stay on top of the auction regardless of where they are.
- Simple structure aimed at a wide display not narrow sets
- A secure website
- Ease of updating the catalogue and adding new blog posts.

#### Planning

Bearing these goals in mind strategically the site must allow easy entry of product details by the site owner and restrict user entry to bidding and payment forms. The site must also immediately immerse the user in the products available for purchase.

User stories were developed.

- As the site owner I want to be able to add new products.
- As the site owner I want to be able to edit products.
- As the site owner I want to be paid for my products.
- As a buyer I want to be able to browse the products.
- As a buyer I want to be able to view products of a particular type.
- As a buyer I want to be able to bid on items.
- As a buyer I wish to be able to follow the progress of my bid and know if I am being outbid.
- As a buyer I wish to pay for my purchases.

A simple structure with consistent navigation links seemed the best solution. The structure is somewhat like the hub and spoke model with **Auction**, **News**, **Review** spokes but with the constant navigation links of the template the structure appears more fluid as you can 'move' in any direction.

A relational database seemed well suited to the project and is required by the specifications of the Code Institute brief. Since I was deploying to Heroku using the Heroku-Postgres database was the obvious answer.

Navigation was designed to be obvious and intuitive with consistency a must, only the toggle between login and logout according to the user's login status changes to ensure all links are in the expected place at all times.

Balsamiq [wireframes](https://petes-gp-bucket.s3.eu-central-1.amazonaws.com/NewProject.bmpr)

### Features

The features of the website are intended to be in the background allowing the products to shine.

#### Existing Features

##### Global Features

The top navigation elements are the key to the entire site. Giving access to the the entire catalogue through **Auctions** as well as **Registration** and **Login/Logout** functions. The **Blog** and **Review** links provide valuable information and finishing off the top row of buttons the informative **How it Works** link.

As per expectation the company name, in lieu of a logo, is displayed prominently at the top of the page and functions as a link back to the home page. Again positioned exactly where you would first look for it at the foot of the page are further links with information about the company and it's policies.

##### Index

The index page is dominated by a large image of the most recently added item for sale, ensuring a constantly fresh and dynamic face to the enterprise framed in predictable navigation and familiar options. Naturally the image provides a direct link to the detail view with further information and the option to buy.

Further down the page are new blog entries ensuring the customer is kept up to date on any and all exciting new products and opportunities.

##### Auctions

Probably the heart of the enterprise the **Catalogue** app has the models and views that display the products and allow you to bid on them.

The **Auctions** link in the top navigation open a page with the newest item displayed over the main catalogue listing. Details from the database are displayed along side the image and below the picture the simple bid for is displayed allowing the user to purchase which ever antique is displayed. If the auction has not yet started or has closed the bid form will not be displayed. When the item is marked as sold in the database then it will be removed entirely from the listing. It is to be hoped there won't be issues with buyers backing out after the auction but the eventuality has been prepared for.

##### Payment

The **Payment** app and it's pages are linked since this flows better. Since Gray's is a notional company it isn't clear if this actually suits the business flow with the wildly variable shipping and insurance costs of such varied products, it may be in the real world with a partner to the process other options would have been preferred. A straight forward series of forms allow the purchaser either to select a previously used delivery address or to enter a new one, before confirming, editing or entering their billing address before going on to the final section with the addresses displayed and the Stripe payment form below. As explained above the price is not dynamically set due to the variability of shipping costs and insurance on valuable and fragile antiques.

#### Features to Implement

- A search bar incorporated into base.html displayed with the top navigation elements.
- Set up some form of processing to automatically reduce pictures sizes. Using pillow to accomplish this would of course work but puts considerable strain on the site compared to processing via AWS S3. 
- A process of permitting access to a review entry form for purchased items after delivery, effectively automating the process and putting it entirely in the hands of the users.
- The payment app could be more secure, by re-validating the connection between the address and the user after form submission.

#### A Note on Development Problems

During the end phase of development I ran into considerable problems with my migrations and then consequently onwards deployment to the heroku postgres database. As time was extremely pressing and I was at the point where my tutor support had expired I was forced into a suboptimal solution, to make a fresh start rather than to go back through my commit history and unpick my errors and move on in the normal fashion.
Accordingly the bare bones of the project were created anew in a separate environment feeding a separate repository and through the liberal application of copy paste I was able to rapidly recreate the project with fresh models without problem, complete the remain functional aspects of the site, advance to AWS S3 deployment and deployment to heroku.

The original repository with it's full development history is at https://github.com/PeteWillmott/milestone4

### Technologies used

#### Languages

The logic of the project was created in Python with HTML templates  styled with SCSS and a little JavaScript. The CSS file on AWS S3 is a minified file compiled from SCSS components, an unminified more readable file is presented on GitHub alongside the SCSS files it is complied from.

#### Framework

[Django](https://www.djangoproject.com/) the framework the project was created with.

#### Libraries

[Bootstrap](https://getbootstrap.com/) used to style the project.

[jQuery](https://jquery.com/) used to simplify DOM manipulation.

[Font Awesome](https://fontawesome.com/) used for icons.

[Google Fonts](https://fonts.google.com/) used to provide fonts.

#### Tools

[VS Code](https://code.visualstudio.com/) the IDE I developed the project in.

[Balsamiq](https://balsamiq.com/) used for planning and wireframes.

[PIP](https://pip.pypa.io/en/stable/) used to install tools.

[PostgreSQL](https://www.postgresql.org/) the database used for this project.

[StripeAPI](https://stripe.com/de/payments) used to provide secure and private payment.

#### Hosting

[GitHub](https://github.com/) hosting for the code repository.

[AWS S3](https://aws.amazon.com/s3/?sc_icampaign=consolesignout_generic_explore_s3&sc_ichannel=ha&sc_icontent=awssm-1111&sc_iplace=tile&trk=ha_awssm-1111) hosting for uploaded image files.

[Heroku](https://www.heroku.com/) hosting for the demo site.

### Testing

The site was tested using Django's built in **TestCase** functionality, by manual testing and by the use of validators. A Chrome Developer's Tools Audit was also conducted.

At the end of development `python.manage.py test` indicated all tests were passing. 

Each page was manually checked on mobile phone, tablet and laptop.

For the full test process see Testing.md.

### Database

### Deployment

#### GitHub

##### GitHub Repository - https://github.com/PeteWillmott/grays-auctionhouse

To run locally you can either download direct from GitHub, using the green "Clone or download" button, or clone by entering `git clone https://github.com/PeteWillmott/recipebook`. To sever the link to my repository use the command `git remote rm origin`.

The exact details of how to proceed from this point will depend on your IDE.

1. Unpack the downloaded files into your project folder

2. Ensure you have Python 3 installed, a download from python.org,  `sudo apt install python3-pip`, or `brew install python3`as best suits your operating system.

3. A virtual environment is recommended. 

   - Cd into your project folder and create your environment `python3 -m venv env`for macOS/Linux `python -m venv env`for windows. 
   - Open the folder in your IDE `code .` for me but varies by IDE.
   - Activate the virtual environment. (For me this meant select a Python interpreter `Strg+Shift+P`then create a new integrated terminal `Ctrl+Shift+ö`.)  However that functions for your OS and IDE you would normally see `(env)` displayed in the terminal by the command prompt.
   -  Install Django `python -m pip install django`.
   - You now have a virtual environment to deploy the project into.

   

4. When your environment is ready run `pip -r requirements.txt`.

5. Launch Django by running the command `python manage.py runserver`, the Django server should now be running as your local host,  **http://127.0.0.1:8000** .

6. Django should have created a SQLite3 database but you'll need to create the database schema. To do this run `python manage.py makemigrations`and then `python manage.py migrate`.

7. To access the admin panel of Django you will need to create a superuser. `python manage.py createsuperuser`.

8. With this done the project should be fully functional with all the proper databases created and in the proper relation with each other.

#### Heroku https://grays-auctions.herokuapp.com/

To host your static files on AWS S3 create and account if you don't already have one.

1. Create a bucket and set the CORS configuration and the bucket policy, both within the **Permissions** menu.

   `<CORSConfiguration>`

   `<CORSRule>`

   `<AllowedOrigin>*</AllowedOrigin>`

   `<AllowedMethod>GET</AllowedMethod>`

   `<AllowedMethod>HEAD</AllowedMethod>`

   `<MaxAgeSeconds>3000</MaxAgeSeconds>`

   `<AllowedHeader>Authorization</AllowedHeader>`

   `</CORSRule>`

   `</CORSConfiguration>`

   

   `{`
       `"Version":"2012-10-17",`
       `"Statement":[{`
         `"Sid":"PublicReadGetObject",`
           `"Effect":"Allow",`
         `"Principal": "*",
         "Action":["s3:GetObject"],
         "Resource":["arn:aws:s3:::YOUR BUCKET NAME/*"`
         `]`
       `}`
     `]`
   `}`

2. In AWS IAM create a group and a user for that group with programatic permissions and an S3 permissions policy.

3. In your terminal run `collectstatic`and your static files should be deployed to AWS S3.

4. Sign up for a Stripe account and add your Stripe credentials to the Configuration variable of the Heroku settings window.

To deploy to [Heroku]( https://www.heroku.com/), create an account if you don't have one.

1. Create a `requirements.txt` file using the `pip freeze > requirements.txt` command.

2. create a `Procfile` with the command `echo web: gunicorn main.wsgi:application > Procfile` in the terminal.

3. In Heroku's Resources tab select Heroku Postgres from the Add ons menu, the hobby level is free.

4. `git add ` any unstaged files, `git commit` the project and `git push` to heroku or to GitHub. Deploying to GitHub allows updates to implement directly from GitHub when pushed.

5. Create a new app on Heroku with the "New" button, name it and set the region appropriately. If deploying from GitHub select "GitHub" from "Deploy > Deployment method"

6. In the dashboard for your app select  "Settings > Reveal Config Vars" and start setting some configuration variables.

   DEBUG to FALSE

   IP to 0.0.0.0

   PORT to 5000

   SECRET_KEY 

   DATABASE URL

7. Now `pip install dj_database_url`and in settings.py of your project root change the database settings to match the new Heroku Postgres database.

8. Now rerun the migrations and recreate the superuser as per the local deployment directions.

### Credits

#### Content

I was fortunate enough to receive advice from several quarters, my mentor, the tutors, my friends and fellow students. My work was further informed by other sources, the course work, Stackoverflow and several online tutorials. However the code is my own, with one notable exception, the accounts app with its register, login and logout views and associated code come more or less verbatim from one of the 'follow along' sections of the course so the credit for that app belongs more to the Code Institute and their staff than to me. 

The privacy policy was also found with google and again no credit reflects on me from the content.

#### Media

The bulk of the images were discovered in google searches with the advanced search settings set to return only images that were "free to use or share".



