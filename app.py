import os
from flask import Flask, render_template, request, redirect
from lib.database_connection import DatabaseConnection
from lib.users import User
from lib.user_repository import UserRepository
from lib.listing import Listing
# from lib.listing_repository import ListingRepository
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/', methods=['GET'])
def get_landing_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def create_listing():
    connection = DatabaseConnection()
    connection.connect()
    listing_repository = ListingRepository(connection)
    listing_details = request.form
    new_listing = Listing(title=listing_details["title"], description=listing_details["description"], price=listing_details['price'])
    listing_repository.create(new_listing)
    return redirect("/")



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
