from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection
from app import app

"""
Test to verify session that a logged in user who has a listing can see the edit listing option
"""

def test_logged_in_user_can_see_edit_listing_option(page: Page):
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users CASCADE;")
    connection.execute("TRUNCATE TABLE listings CASCADE;")
    connection.execute("""
                       INSERT INTO users (id, name, email, phone_number, password)
                       VALUES (1, 'test_user', 'test@testemail.com', '07887887887', 'password1234');""")
    connection.execute(
                        """
                        INSERT INTO listings (id, title, description, price_per_night, available_from, available_until, owner_id, thumbnail) 
                        VALUES (1, 'Converted bus stop', 'Great traffic views.', 35, '2026-07-16', '2026-07-31', 1, 'bus_stop.jpg');
                        """)
    page.goto("http://127.0.0.1:5001/users/login")
    page.get_by_label("email").fill("test@testemail.com")
    page.get_by_label("password").fill("password1234")
    page.get_by_role("button").click()

    page.goto("http://127.0.0.1:5001/listings/1")

    expect(page.locator(".owner-controls-card")).to_contain_text("You are the owner of this listing")



"""
Tests that a logged in user is who allowed to edit their own listing can edit their own listing
"""

def test_logged_in_user_can_edit_their_listing(page: Page):
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users CASCADE;")
    connection.execute("TRUNCATE TABLE listings CASCADE;")
    connection.execute("""
                       INSERT INTO users (id, name, email, phone_number, password)
                       VALUES (1, 'test_user', 'test@testemail.com', '07887887887', 'password1234');""")
    connection.execute(
                        """
                        INSERT INTO listings (id, title, description, price_per_night, available_from, available_until, owner_id, thumbnail) 
                        VALUES (1, 'Converted bus stop', 'Great traffic views.', 35, '2026-07-16', '2026-07-31', 1, 'bus_stop.jpg');
                        """)
    page.goto("http://127.0.0.1:5001/users/login")
    page.get_by_label("email").fill("test@testemail.com")
    page.get_by_label("password").fill("password1234")
    page.get_by_role("button").click()

    page.goto("http://127.0.0.1:5001/listings/1/edit")

    page.get_by_label("Title").fill("Fully Renovated Luxury Bus Stop")
    page.get_by_label("Description").fill("Now with double-glazed windows and a velvet armchair!")
    page.get_by_label("Price per Night").fill("45")
    page.get_by_label("Available From").fill("2026-08-01")
    page.get_by_label("Available Until").fill("2026-08-31")
    page.get_by_role("button", name="Save Changes").click()

    expect(page.locator("h1")).to_contain_text("Fully Renovated Luxury Bus Stop")
    expect(page.locator("h1")).not_to_contain_text("Converted bus stop")
    
    expect(page.locator("body")).to_contain_text("£45 per night")


















