# SDEV_220_Final_Project_6
Final Project - Recipe and profit hub

RecipeHub

RecipeHub is a Django-based web application that allows users to create, view, edit, and delete recipes. Each recipe has a title, ingredients, steps for preparation, and related cost information. Users can also calculate the profit for each dish.

Features

	•	User registration and login system.
	•	CRUD operations for recipes:
	•	Create new recipes.
	•	View a list of recipes or detailed views of individual recipes.
	•	Edit existing recipes.
	•	Delete recipes.
	•	Profit calculation for each dish based on selling price and cost price.

Installation & Setup

	1.	Clone the Repository

git clone https://github.com/amarin20/SDEV_220_Final_Project_6.git
cd RecipeHub

	2.	Set Up Virtual Environment

python -m venv myvenv
source myvenv/bin/activate  # On Windows use `myvenv\Scripts\activate`

	3.	Install Dependencies

pip install -r requirements.txt

	4.	Run Migrations

python manage.py migrate

	5.	Start the Development Server

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to access the application.

Testing the Application

To ensure the application is working as expected, follow these test cases:

	1.	User Registration & Login
	•	Navigate to the login page.
	•	Register a new user and verify registration success.
	•	Login with the new user credentials and verify login success.
	2.	Recipe CRUD Operations
	•	Create a new recipe and verify it appears in the recipe list.
	•	View the detailed page of a recipe.
	•	Edit an existing recipe and verify changes are reflected.
	•	Delete a recipe and verify it’s removed from the list.
	3.	Profit Calculation
	•	For a given recipe, input the selling price and cost price.
	•	Verify that the profit calculation is correct.
