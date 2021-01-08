# Image-Repository

Shopify Developer Intern Challenge for Back End Internship during Summer 2021. 

The Image Repository allows user to upload and showcase their images, they also have the choice to list it up for sale for other useres. Each user starts out with 10,000 credits and can use to trade images from other users. The user can also upload their personal images that can be traded or displayed. 

For any inquiries please contact erichungyu.lin@mail.utoronto.ca

## Instructions

### How to create a super user
* Change the directory to the folder containing manage.py
* python manage.py createsuperuser

### How to start the Django site locally
* Change the directory to the folder containing manage.py
* python manage.py runserver will allow the server to be started locally

### How to signup as a regular user
* After starting the server, there will be a signup option that allows the user to either login or signup
* Each user starts out with 10,000 credits

![Image of Signup](https://i.imgur.com/JVeFWer.png)
![Image of Login](https://i.imgur.com/gYc3o1R.png)

## Features

### Product Page (/products)
* The product page of the image repository
* The product page contains the available images listed by the users
* There are different status for the products
  * Sell/Update: The status is shown when you are the owner of the image, you can choose to sell the image and put it up for listing or update the information for it.
  * Cancel Listing: The product is owned by you and has been listed on the market for other user to purchase.
  * Buy: The product is owned by others but they have put it up for sale.
  * No status displayed: The product is not owned by you and the owner did not put it up for sale.
![Image of Products](https://i.imgur.com/bOL295T.png)

### Selling a Product (/products/{id}/sell)
* A user can put their own image up for sale for website currency
* The user can change their list price before confirming to sell an image
* After the image is listed, the user has the ability to cancel the listing
* The user cannot update any information while the product is listed, the listing has to be cancelled first in able to be modified
![Image of Products](https://i.imgur.com/RdGu87q.png)

### Updating an Image (/products/{id}/update)
* User can update information on their own images
* The available fields for updating are:
  * Name
  * Description
  * Tags
  * Price
![Image of Products](https://i.imgur.com/CLkFgni.png)

### Cancelling a Listing (/products/{id}/cancel)
* User can cancel their listing if the image has not been purchased by other users
* There will be a confirmation page for cancelling listing
* Cancelling listing is requierd to modify any information
![Image of Products](https://i.imgur.com/mM1Wq2o.png)

### Buying a Product (/products/{id}/buy)
* User can purchase products that are listed by other users
* User must have enough credit in order to purchase the product listed
* The credit will be deducted if the product has been purchased successfully and the image will be added to your inventory
![Image of Products](https://i.imgur.com/LxzUcLj.png)
![Image of Products](https://i.imgur.com/LjUQJw3.png)

### Searching a Product (/products)
* The search bar is available on the products page
* The search result will display the images that contains tags that matches the query
![Image of Products](https://i.imgur.com/ehqhGKL.png)

### Adding an Image (/products/add)
* User can upload their own image for sale or for display
* The available fields for adding an image are:
  * Name
  * Image: Upload an image
  * Description
  * Tags
  * Price
  * Status: Owned or Listed, Owned keeps the image for display for now, listed lists the product for sale
![Image of Products](https://i.imgur.com/nRyAWCS.png)

### User Profile - Information (/profiles/myprofile)
* The profile contains a section with basic user information
  * Username
  * First Name
  * Last Name
  * Country
  * Bio
  * Credit
  * User Profile Picture
* Some of the information can be edited with Edit Profile
  * First Name
  * Last Name
  * Bio
  * Profile Picture
![Image of Products](https://i.imgur.com/we7QulP.png)
 
 ### User Profile - Inventory (/profiles/myprofile)
 * User's Inventory displays the images that they currently own
 * The images in the inventory cannot be updated on profile, all proccesses are done under the product page (/products), the inventory is for display purpose
 ![Image of Products](https://i.imgur.com/zlQ4n73.png)
