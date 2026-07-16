import os
from flask import Flask, render_template, request, redirect, session, flash
from lib.database_connection import DatabaseConnection
from lib.users import User
from lib.user_repository import UserRepository
from lib.listing import Listing
from lib.listing_repository import ListingRepository

import calendar
from datetime import datetime

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
    listings_emails = listing_repository.all_with_owner_emails()
    return render_template('index.html', listings=listings_emails)


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
    try:
        user_repository.create(new_user)
        flash("Sign up successful!", "success")
        return redirect('users/login')
    except ValueError as e:
        flash(str(e), "error")
        return redirect("/users/new")

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
    user = user_repository.find_by_email(email)

    if user and user.password == password:
        session["user_id"] = user.id
        session["email"] = user.email
        return redirect("/")
    else:
        return redirect("/users/login")
    
"""
Listings page GET(get listings page) POST(get create listings page) POST(create listing)
"""

@app.route('/listings', methods=['GET'])
def get_all_listings():
    connection = DatabaseConnection()
    connection.connect()
    listing_repository = ListingRepository(connection)
    listings_emails = listing_repository.all_with_owner_emails()
    return render_template('listings.html', listings=listings_emails)

# Start
# This route gets /listings/new (renders create_listing.html).
# Added by Trouli, to check that she made the html file correctly.
# Please feel free to edit/change.
@app.route('/listings/new', methods=['GET'])
def get_create_listing():
    return render_template("create_listing.html")
# End

@app.route('/listings/new', methods=['POST'])
def create_listing():
    connection = DatabaseConnection()
    connection.connect()
    listing_repository = ListingRepository(connection)
    listing_details = request.form
    new_listing = Listing(title=listing_details["title"], description=listing_details["description"],
                          price=listing_details['price'], available_from=listing_details['available_from'],
                          available_until=listing_details['available_until'], owner_id=listing_details['owner_id'])
    listing_repository.create(new_listing)
    return redirect("/listings")

"""
Individual listing page. GET(get listing page)
"""

# @app.get('/listings/<int:property_id>')
# def get_individual_listin_converter(property_id):
#     connection = DatabaseConnection()
#     connection.connect()
#     listing_repository = ListingRepository(connection)

#     listing = listing_repository.find_by_listing_id(property_id)
#     return render_template('property_page.html', listing=listing)
    
@app.get('/listings/<int:property_id>')
def get_individual_listin_converter_with_calendar(property_id):
    connection = DatabaseConnection()
    connection.connect()
    listing_repository = ListingRepository(connection)
    listing = listing_repository.find_listing_by_id(property_id)

    now = datetime.now()
    year = request.args.get('year', default=now.year, type=int)
    month = request.args.get('month', default=now.month, type=int)

    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year
    
    if month == 12:
        next_month = 1
        next_year = year +1
    else:
        next_month = month + 1
        next_year = year



    cal_matrix = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    return render_template('property_page.html', listing=listing, cal_matrix=cal_matrix, month_name=month_name, month=month, year=year, prev_month = prev_month, prev_year = prev_year, next_month = next_month, next_year = next_year)

# The POST route: Processes the booking submission for that listing
# @app.post('/listings/<int:listing_id>')
# def create_booking(listing_id):
#     selected_date = request.form.get('selected_date') # Format: "YYYY-MM-DD"
    
#     # 1. Validation: Make sure they actually clicked a date
#     if not selected_date:
#         flash("Please select a date on the calendar.", "error")
#         return redirect(f'/listings/{listing_id}')
        
#     # 2. Database Integration
#     connection = DatabaseConnection()
#     connection.connect()
#     booking_repository = BookingRepository(connection)
    
#     try:
#         # Mocking user_id = 1 for now (replace this with session['user_id'] once login is set up)
#         booker_id = 1
        
#         # 3. USE the selected_date variable to write a new row to your bookings table!
#         booking_repository.create(listing_id=listing_id, user_id=booker_id, date=selected_date)
        
#         # 4. Success feedback
#         flash(f"Successfully booked for {selected_date}!", "success")
#         return redirect(f'/listings/{listing_id}')
        
#     except Exception as e:
#         flash(f"Could not complete booking: {str(e)}", "error")
#         return redirect(f'/listings/{listing_id}')

@app.after_request
def add_header(response):
    # This tells the browser: "Do not save a frozen snapshot of this page!"
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


