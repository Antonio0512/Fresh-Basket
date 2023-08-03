# Fresh Basket

<img alt="Project Logo" src="fresh_basket/staticfiles/images/fresh-basket-logo.png" width="250" height="250"/>


Welcome to my Fresh Basket online grocery shop project! This is a web application that allows users to browse and purchase a wide
range of fresh and organic products for a healthier lifestyle. The project is built using Django, a high-level Python
web framework, and integrates various apps for different functionalities.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User Registration and Login: Users can create an account, log in, and manage their profiles.
- Product Catalog: Browse and search through all available products, filter by categories, and view product details.
- Promotions and Offers: Check out the latest promotions, discounts, and exclusive offers.
- Shopping Cart: Add products to the cart, manage quantities, and proceed to checkout for payment.
- Payment Integration: Securely process payments using Stripe integration.
- Favorites: Users can easily view and manage their favorite products.
- User Reviews: Add and view product reviews and ratings.

## Installation

Follow these steps to set up the project locally:

```bash
# Clone the repository
git clone https://github.com/Antonio0512/Fresh-Basket.git
```

#### IMPORTANT! You have to configure your .env file and I have given an example env file in the project

```bash
# Create a virtual environment
python -m venv venv
```

```bash
# Activate the virtual environment (Linux/macOS)
source venv/bin/activate
```

```bash
# Activate the virtual environment (Windows)
venv\Scripts\activate
```

```bash
# Install the required packages
pip install -r requirements.txt
```

```bash
# Set up the database
python manage.py migrate
```

```bash
# Create a superuser to access the admin panel
python manage.py createsuperuser
```

```bash
# Run the development server
python manage.py runserver
```

## Usage

- Visit the website at [http://localhost:8000/](http://localhost:8000/) in your web browser.
- Register or log in to start browsing and shopping.
- Explore the product catalog, check out promotions, and add products to your cart.
- Proceed to the checkout page for payment using Stripe integration.

## Contributing

We welcome contributions to improve this project! If you find a bug, have a feature request, or want to contribute code,
please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin my-feature-branch`
5. Submit a pull request to the `main` branch.

We'll review your changes and merge them if they align with the project's goals.

## License

This project is licensed under the [MIT License](../LICENSE).

---

Thank you for checking out my Fresh Basket project! If you have any questions or feedback, feel free to reach
out to me. Happy shopping! 😊
