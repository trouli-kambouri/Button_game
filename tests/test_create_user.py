from lib.users import User
from lib.user_repository import UserRepository

# from lib.listing_repository import ListingRepository

from app import app
from lib.database_connection import DatabaseConnection

"""
Test creating a new user and testing that all elements of the parameters match the output
"""

def test_create_a_user():
    new_user = User('Test', 'testuser@testemail.com', '07000000000', 'password1234', 1)
    assert new_user.name == "Test"
    assert new_user.email == "testuser@testemail.com"
    assert new_user.phone_number == "07000000000"
    assert new_user.password == "password1234"
    assert new_user.id == 1



# def test_create_user_is_saved_to_database():
#     # create the test client to send requests without using Playwright and a browser
#     client = app.test_client()

#     # set up a DB connection
#     connection = DatabaseConnection()
#     connection.connect()

#     # connection.execute("TRUNCATE TABLE users;")

#    # send the request
#     response = client.post('/users', data={
#         'name': 'testuser',
#         'email': 'testuser@test.com',
#         'phone_number': "07000000000",
#         'password': 'password1234',
# })

#     # assert that the redirect happened
#     assert response.status_code == 302

#     # read from the DB
#     result = connection.execute("SELECT * FROM users WHERE username = 'testuser'")

#     # assert that the user was created
#     assert len(result) == 1
#     assert result[0]['username'] == 'testuser'