# Image-Repository

## Instructions

### How to create a super user
* Change the directory to the folder containing manage.py
* python manage.py createsuperuser

### How to start the Django site locally
* Change the directory to the folder containing manage.py
* python manage.py runserver will allow the server to be started locally

### How to signup as a regular user
* After starting the server, there will be a signup option that allows the user to either login or signup
![Image of Signup](https://i.imgur.com/JVeFWer.png)
![Image of Login](https://i.imgur.com/gYc3o1R.png)

## Features

### Product Page
* The product page of the image repository
* The product page contains the available images listed by the users
* There are different status for the products
  * Sell/Update: The status is shown when you are the owner of the image, you can choose to sell the image and put it up for listing or update the information for it.
  * Cancel Listing: The product is owned by you and has been listed on the market for other user to purchase.
  * Buy: The product is owned by others but they have put it up for sale.
  * No status displayed: The product is not owned by you and the owner did not put it up for sale.
![Image of Products](https://i.imgur.com/bOL295T.png)
