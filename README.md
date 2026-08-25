I am turning this into a button game. :)

Goals for MVP:

1. Integrate AUTH0 (/login)
2. One button (/home)
3. Deploy site

Right now:

0. Integrate Supabase for a remote database. Make sure everything is set up.
1. Set up Supabase Authentication and login page.
2. Maybe deploy site on something that's not github pages... but that's ok for now.
3. Learn enough JS to create one button.
4. Clean up the code.


# Python Project Seed

This repo contains the seed codebase for the MakersBnB project in Python (using 
Flask and Pytest).

> NOTE: If you encounter a `ModuleNotFound` error, deactivate and then reactivate your virtual env. If that doesn't help, please reach out to your coach.

## Setup

```shell
# Set up the virtual environment
; python -m venv makersbnb-venv

# Activate the virtual environment
; source makersbnb-venv/bin/activate 

# Install dependencies
(makersbnb-venv); pip install -r requirements.txt

# Install the virtual browser we will use for testing
(makersbnb-venv); playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
(makersbnb-venv); createdb makers_bnb
(makersbnb-venv); createdb makers_bnb_test

# Open lib/database_connection.py and change the database names
(makersbnb-venv); open lib/database_connection.py

# Run the tests (with extra logging)
(makersbnb-venv); pytest -sv

# Run the app
(makersbnb-venv); python app.py

# Now visit http://localhost:5001/index in your browser
```
