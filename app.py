import os
from flask import Flask, render_template, request, redirect, session
from lib.database_connection import DatabaseConnection
from lib.users import User
from lib.user_repository import UserRepository
from lib.listing import Listing
from lib.listing_repository import ListingRepository
# Create a new Flask app
app = Flask(__name__)
app.secret_key = "some_really_secret_key"

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index

"""
Landing page GET(get landing page) POST(create listig) POST(remove listing)
"""

@app.route('/', methods=['GET'])
def get_landing_page():
    connection = DatabaseConnection()
    connection.connect()
    listing_repository = ListingRepository(connection)
    listings = listing_repository.all()
    return render_template('index.html', listings=listings)


@app.route('/', methods=['POST'])
def create_listing():
    connection = DatabaseConnection()
    connection.connect()
    listing_repository = ListingRepository(connection)
    listing_details = request.form
    new_listing = Listing(title=listing_details["title"], description=listing_details["description"], price=listing_details['price'], owner_id=listing_details['owner_id'])
    listing_repository.create(new_listing)
    return redirect("/")

@app.route('/', methods=['POST'])
def remove_listing():
    connection = DatabaseConnection()
    connection.connect()
    listing_repository = ListingRepository(connection)
    listing_details = request.form
    listing = Listing(title=listing_details["title"], description=listing_details["description"], price=listing_details['price'], owner_id=listing_details['owner_id'])
    listing_repository.remove(listing)
    return redirect("/")    


"""
Sign up page GET(get signin page) POST(signup user)
"""


@app.route("/users/new", methods=["GET"])
def get_sign_up_page():
    return render_template('signup.html')

@app.route('/users', methods=['POST'])
def signup_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    new_user = User(name=user_details["name"], email=user_details["email"], phone_number=user_details["phone_number"], password=user_details["password"])
    user_repository.create(new_user)
    return redirect("/users/login")

"""
Login Page GET(get login page) POST(create session)
"""


@app.route("/users/login", methods=["GET"])
def get_login_page():
    return render_template('login.html')


@app.route('/sessions', methods=['POST'])
def create_session():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    email = request.form["email"]
    password = request.form["password"]
    user = user_repository.find_by_name(email)

    if user and user.password == password:
        session["user_id"] = user.id
        session["email"] = user.email
        return redirect("/")
    else:
        return redirect("/users/login")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
