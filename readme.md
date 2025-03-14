# Northwind - A database problem to learn Django

This is an introductory project I started to teach myself Django. It includes a fully populated database that can be found [here](https://github.com/pthom/northwind_psql) that I've used to create an example website for handling said data. After spending a week and a half on example exercises and guides (mostly [W3schools](https://www.w3schools.com/django/index.php) and [Tech with tim](https://www.techwithtim.net/tutorials/django)), I spend this week coding the project found here. 


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Improvements](#improvements)
- [License](#license) 


## Introduction

This project is a Django-based web application that utilizes the Northwind database. It serves as a learning platform for Django, demonstrating how to connect to a database, create views, handle user authentication, and implement various functionalities for data display and manipulation. The application provides basic CRUD (Create, Read, Update, Delete) operations, user authentication, and custom list creation features.

## Features

-   **Database Integration:** Uses the Northwind database as a populated example.
-   **User Authentication:** Includes user registration, login, and logout functionalities.
-   **Data Display:** Displays data from various tables (orders, suppliers, products, categories, customers, employees, shippers) in a user-friendly format.
-   **Admin Interface:** Django's built-in admin interface is available for managing data.
-   **Custom Product Lists:** Users can create and save custom product lists.
-   **User-Specific Product Lists:** Users can view and manage their own created product lists.
-   **Basic Data Views:** Displays information for various tables like suppliers, products, shippers, and customers.
-   **Employee and Customer Views:** Restricted views for logged in users to see employee, order and customer information.
-   **Misc Functions:** A place for functions that are not yet fully implemented or linked to.
-   **Account Management:** Users can access their product lists through the account section.

## Installation

**1. Repository:**

```bash
git clone [https://github.com/helland/Northwind-database-project.git](https://www.google.com/search?q=https://github.com/helland/Northwind-database-project.git)
cd Northwind-database-project
```

**2. Create a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On macOS and Linux
venv\Scripts\activate  # On Windows
```

**3. Install the required packages:**

```bash
pip install -r requirements.txt


```

**4. Database Setup:**

-   Ensure you have PostgreSQL installed and running.
-   Create a database named northwind.
-   Restore the Northwind database from the provided SQL file (available in the linked GitHub repository).
-   Update the DATABASES setting in northwind/settings.py with your database credentials.


**5. Run Migrations:**

```bash
python manage.py migrate
```

**6. Create a Superuser:**

```Bash

python manage.py createsuperuser

```

**7. Run the Development Server:**

```Bash

python manage.py runserver
```


## Usage

* Open your web browser and navigate to http://127.0.0.1:8000/.
* Use the login/sign-up links to create an account or log in.
* Navigate through the various links to explore the data.
* Create custom product lists via the "misc" page.
* View user-specific product lists via the "account" page.
* Use the admin interface (/admin/) to manage data.


## Code Structure
Northwind-database-project/

├── northwind/

│   ├── __init__.py

│   ├── asgi.py

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

├── main/

│   ├── __init__.py

│   ├── admin.py

│   ├── apps.py

│   ├── migrations/

│   ├── templates/

|	&emsp;&emsp;	├── main/

|	&emsp;&emsp;&emsp;&emsp;		├── base.html	

|	&emsp;&emsp;&emsp;&emsp;		├── categories_view.html	

|	&emsp;&emsp;&emsp;&emsp;		├── custormer_demograpgics_view.html	

|	&emsp;&emsp;&emsp;&emsp;		├── customers_view.html	

|	&emsp;&emsp;&emsp;&emsp;		├── employees_view.html	

|	&emsp;&emsp;&emsp;&emsp;		├── home.html	

|	&emsp;&emsp;&emsp;&emsp;		├── misc.html	

|	&emsp;&emsp;&emsp;&emsp;		├── order_detals_view.html	

|	&emsp;&emsp;&emsp;&emsp;		├── orders_view.html	

|	&emsp;&emsp;&emsp;&emsp;		├── product_selection_success.html	

|	&emsp;&emsp;&emsp;&emsp;		├── prouct_selection.html	

|	&emsp;&emsp;&emsp;&emsp;		├── products_view.html	

|	&emsp;&emsp;&emsp;&emsp;		├── shippers_view.html	

|	&emsp;&emsp;&emsp;&emsp;		└── suppliers_view.html	

|	&emsp;&emsp;	├── registration/

|	&emsp;&emsp;&emsp;&emsp;		├── login.html	

|	&emsp;&emsp;&emsp;&emsp;		├── logout.html	

|	&emsp;&emsp;&emsp;&emsp;		└── sign_up.html	

│   ├── static/

|	&emsp;&emsp;	└── style.css

│   ├── __init__.py

│   ├── apps.py

│   ├── admin.py

│   ├── models.py

│   ├── tests.py

│   ├── urls.py

│   └── views.py

├── account/

│   ├── migrations/

│   ├── templates/

|	&emsp;&emsp;	├── account/

|	&emsp;&emsp;&emsp;&emsp;		├── product_list_detail.html	

|	&emsp;&emsp;&emsp;&emsp;		└── product_lists.html	

│   ├── __init__.py

│   ├── models.py

│   ├── apps.py

│   ├── admin.py

│   ├── tests.py

│   ├── urls.py

│   └── views.py

├── venv/

├── manage.py

├── requirements.txt

└── README.md

* northwind/: Contains the project's settings and main URLs.
* main/: Contains the main application logic, views, models, and URLs.
* account/: Contains the account related logic, specifically user product lists.
* venv/: The virtual environment.
* manage.py: Django's command-line utility.
* requirements.txt: Lists the project's dependencies.

## Improvements
As this project was canceled before it was finished, the improvements that can be made are numerous. I will only list the functions that were not implemented yet, but asked for in the problem text.


* Employees: Retrieve employee number, name, position, and hire date. Use JOIN to combine data from Employee and Orders. Use GROUP BY to find which employees have sold the most and the least. 


* Inventory and sales statistics: Retrieve information about inventory and the number of units sold for each item. Use GROUP BY to aggregate data and show which items are selling the most. 


* Sales by category: Find how many products have been sold within each category using JOIN and GROUP BY. Vendor revenue: Find which vendors generate the most revenue, based on sales of their products. 


**Optional additional queries:** 
* Monthly sales: Find how much sales have been made each month. Average order value per customer: Find the average earnings of each order and customer. 


* Delivery times per carrier: Find the average delivery time for each carrier (calculated as the difference between the order date and the delivery date). 


* Demand Over Time: Analyze how demand for different products has changed over time (use time-based SQL queries) 


* Analyze Seasonal Sales Trends: Use monthly and quarterly queries to identify seasonal peaks in product sales. (Which seasons/months sell the most and which months sell the least). 


* Compare Prices and Sales: Compare average prices for products with sales data to see if there is a correlation between the price of a product and how much it sells. 


* Lastly, make the site actually look good with proper styling and UI improvements

## License
	public domain	
