<h1 align="center">Welcome to PetPro 👋</h1>
<p>
</p>

> This Django-based web application named &#34;PetPro&#34; is designed to cater to a pet-related business, offering various functionalities related to managing products, a cart system, contact forms, and informative pages. Below is a breakdown of the key functionalities:

<h2>Functionalites</h2>

<h3>1. Adding Products to Cart</h3>
The add_to_cart function manages the addition of products to the cart.
Authenticated users have their cart linked to their account.
Anonymous users' carts are maintained through session-based data.

<h3>2. About Us Page</h3>
The aboutus function renders an 'aboutus.html' template, providing information about the business.

<h3>3. Cart Mangement</h3>
The cart function handles the display and management of the cart.
For authenticated users, it fetches items from the Cart model.
For anonymous users, it manages a session-based cart.

<h3>Contact Form Submission</h3>
The contactus function manages the submission of contact details.
Saves the contact information to the Contact model.

<h3>Display All Products</h3>
The products function fetches all products from the Product model.
Renders the 'all_products.html' template to display the products.

<h3>Product Details</h3>
The product_details function fetches details of a specific product based on its primary key.
Renders the 'details.html' template to display product-specific information.

<h2>Usage:</h2>

## Clone the repository: 
```sh 
git clone https://github.com/yourusername/petpro.git
```
## Set up a virtual environment and install dependencies using:
```sh 
pip install -r requirements.txt.
```
### Run migrations: 
```sh 
python manage.py migrate.
```
### Start the development server: 
```sh 
python manage.py runserver.
```
Access the application via the provided routes and functionalities described above.

## Author

👤 **Ines Alferez**

* Github: [@InesAlferez](https://github.com/InesAlferez)

* LinkedIn: [@ines-alferez-0a0881234](https://linkedin.com/in/ines-alferez-0a0881234)
