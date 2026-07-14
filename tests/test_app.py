import sys
import os

from playwright.sync_api import Page, expect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Tests for your routes go here

from app import app

# a descriptive test name
def test_get_homepage_returns_a_200():
    # here's where we make the test client
    client = app.test_client()

    # here's where we make the request
    response = client.get("/")

    # here's where we assert that the response's status code is 200
    assert response.status_code == 200


# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://localhost:5001/")

#     # We look at the <p> tag
#     p_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(p_tag).to_have_text("MakersBNB")