import os
from flask import Flask, render_template, request, redirect, session, flash
from lib.database_connection import DatabaseConnection
from lib.helpers import get_guest_booking_info, get_owner_request_info 
from lib.users import User
from lib.user_repository import UserRepository
from lib.listing import Listing
from lib.listing_repository import ListingRepository
from lib.booking_repository import BookingRepository
from lib.bookings import Bookings

import uuid
import calendar
from datetime import datetime
from werkzeug.utils import secure_filename



# Create a new Flask app
app = Flask(__name__)
app.secret_key = "some_really_secret_key"

UPLOAD_FOLDER = 'static/thumbnails'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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


# @app.route('/', methods=['POST'])
# def remove_listing():
#     connection = DatabaseConnection()
#     connection.connect()
#     listing_repository = ListingRepository(connection)
#     listing_details = request.form
#     listing = Listing(title=listing_details["title"], description=listing_details["description"], price=listing_details['price'], thumbnail=listing_details['thumbnail'], owner_id=listing_details['owner_id'])
#     listing_repository.remove(listing)
#     return redirect("/")    


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
        return redirect('/users/login')
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
    if "user_id" not in session:
        return redirect("/users/login")
    return render_template("create_listing.html")
# End

@app.route('/listings/new', methods=['POST'])
def create_listing():
    if "user_id" not in session:
        return redirect("/users/login")

    connection = DatabaseConnection()
    connection.connect()
    listing_repository = ListingRepository(connection)
    listing_details = request.form
    new_listing = Listing(title=listing_details["title"].strip(), description=listing_details["description"].strip(),
                          price=listing_details['price'], available_from=listing_details['available_from'],
                          available_until=listing_details['available_until'], owner_id=session["user_id"])
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
def get_individual_listing_converter_with_calendar(property_id):
    connection = DatabaseConnection()
    connection.connect()
    listing_repository = ListingRepository(connection)
    listing = listing_repository.find_listing_by_id(property_id)
    
    gallery_images = connection.execute(
        "SELECT image_url FROM listing_images WHERE listing_id = %s ORDER BY position;", 
        [property_id]
    )

    user_repository = UserRepository(connection)
    owner = user_repository.find_by_user_id(listing.owner_id)

# 💡 1. INITIALIZE BOOKING REPOSITORY & FIND BOOKINGS
    # (Adjust 'BookingRepository' and 'find_by_listing_id' to match your class/method names)
    booking_repository = BookingRepository(connection)
    bookings = booking_repository.find_bookings_by_listing_id(property_id) 

    # 💡 2. FORMAT BOOKINGS TO A JAVASCRIPT-FRIENDLY DICTIONARY LIST
    # This formats the Python date/datetime objects to "YYYY-MM-DD" strings
    booked_ranges = [
        {
            "start": b.start_date.strftime('%Y-%m-%d'), 
            "end": b.end_date.strftime('%Y-%m-%d')
        }
        for b in bookings
    ]

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

    return render_template('property_page.html', listing=listing, gallery_images=gallery_images, cal_matrix=cal_matrix, month_name=month_name, month=month, year=year, prev_month = prev_month, prev_year = prev_year, next_month = next_month, next_year = next_year, owner_email = owner.email, booked_ranges=booked_ranges)

# The POST route: Processes the booking submission for that listing
@app.post('/listings/<int:listing_id>/my_bookings')
def create_booking(listing_id):
    if "user_id" not in session:
        return redirect("/users/login")

    connection = DatabaseConnection()
    connection.connect()
    booking_repository = BookingRepository(connection)
    
    # 1. Get the dates from the submitted form
    start_date = request.form.get('check_in')
    end_date = request.form.get('check_out')
    
    # Simple validation: ensure both dates were actually selected
    if not start_date or not end_date:
        flash("Please select both check-in and check-out dates.", "error")
        return redirect(f"/listings/{listing_id}")
        
    # 2. Get the logged-in user's ID 

    current_user_id = session["user_id"] 
    
    # 3. Create a new Booking instance (status defaults to 'pending')
    new_booking = Bookings(
        start_date=start_date,
        end_date=end_date,
        listing_id=listing_id,
        guest_id=current_user_id,
        status="requested"
    )
    
    booking_repository.create(new_booking)
    flash("Booking request sent successfully!", "success")
    return redirect('/my_bookings')

"""
Manage bookings page: GET /my_bookings
"""
@app.route("/my_bookings", methods=["GET"])
def get_manage_bookings_page():
    if "user_id" not in session:
        return redirect("/users/login")
    connection = DatabaseConnection()
    connection.connect()

    user_id = session["user_id"]

    guest_bookings = get_guest_booking_info(connection, user_id)
    owner_requests = get_owner_request_info(connection, user_id)

    return render_template("my_bookings.html", user_id=user_id, guest_list=guest_bookings, owner_list=owner_requests)


"""
Route for editing the listing to be used after initial creation of a listing
"""

@app.route('/listings/<int:property_id>/edit', methods=['GET'])
def get_edit_listing_page(property_id):
    if "user_id" not in session:
        return redirect("/users/login")

    connection = DatabaseConnection()
    connection.connect()
    
    listing_repo = ListingRepository(connection)
    listing = listing_repo.find_listing_by_id(property_id)

    gallery_images = connection.execute(
        "SELECT image_url FROM listing_images WHERE listing_id = %s ORDER BY position;",
        [property_id]
    )
    

    if listing.owner_id != session["user_id"]:
        flash("You are not authorized to edit this listing.", "error")
        return redirect("/")

    return render_template('edit_listing.html', listing=listing, gallery_images=gallery_images)


"""
Route for file uploads to the database
"""

@app.route('/listings/<int:property_id>/edit', methods=['POST'])
def update_listing_and_add_images(property_id):
    if "user_id" not in session:
        return redirect("/users/login")

    connection = DatabaseConnection()
    connection.connect()
    listing_repo = ListingRepository(connection)
    listing = listing_repo.find_listing_by_id(property_id)

    if listing.owner_id != session["user_id"]:
        flash("Unauthorized action.", "error")
        return redirect("/")


    listing_details = request.form

    connection.execute(
        """
        UPDATE listings 
        SET title = %s, description = %s, price_per_night = %s, 
            available_from = %s, available_until = %s
        WHERE id = %s;
        """,
        [
            listing_details["title"], 
            listing_details["description"], 
            int(listing_details["price"]),
            listing_details["available_from"], 
            listing_details["available_until"],
            property_id
        ]
    )

    uploaded_files = request.files.getlist("additional_images")

    for file in uploaded_files:
        if file and allowed_file(file.filename):
            # Secure the filename and make it unique using a UUID
            original_filename = secure_filename(file.filename)
            unique_name = f"{uuid.uuid4()}_{original_filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_name)
            
            # Save the file physically to static/thumbnails/
            file.save(file_path)

            # Construct the relative url path
            relative_url = f"/static/thumbnails/{unique_name}"

            # 3. Write to the database
            # (Executing raw SQL inside your connection object)
            connection.execute(
                "INSERT INTO listing_images (listing_id, image_url) VALUES (%s, %s);",
                [property_id, relative_url]
            )

    flash("Listing updated successfully!", "success")
    return redirect(f"/listings/{property_id}")

@app.get('/listings/<int:listing_id>/images/delete')
def delete_listing_image(listing_id):
    if "user_id" not in session:
        return redirect("/users/login")
        
    connection = DatabaseConnection()
    connection.connect()

    listing_repo = ListingRepository(connection)
    listing = listing_repo.find_listing_by_id(listing_id)
    if listing.owner_id != session["user_id"]:
        flash("Unauthorized action.", "error")
        return redirect(f"/listings/{listing_id}")
    
    image_url = request.args.get("image_url")

    if image_url:
        relative_path = image_url.lstrip('/')
        if os.path.exists(relative_path):
            os.remove(relative_path)

        connection.execute(
            "DELETE FROM listing_images WHERE listing_id = %s AND image_url = %s;",
            [listing_id, image_url]
        )
        flash("Image deleted successfully!", "success")

    return redirect(f"/listings/{listing_id}/edit")


@app.after_request
def add_header(response):
    # This tells the browser: "Do not save a frozen snapshot of this page!"
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route('/users/logout', methods=['GET'])
def logout_user():
    session.clear() 
    flash("You have been logged out.", "success")
    return redirect('/')

@app.context_processor
def inject_user_email():
    return dict(email=session.get('email'))

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))




