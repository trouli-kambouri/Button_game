import pytest
from lib.user_repository import UserRepository
from lib.users import User


def test_user_repository_all_returns_list_of_all_users(db_connection):
    db_connection.seed("seeds/reset_users_data.sql")


    repository = UserRepository(db_connection)
    users = [
        User('kayleighkarpal', 'kayleighk@kickabout.com', '07635183911', 'badpassword', 1),
        User('mingma', 'maming@matsforcats.co.uk', '07876543909', '-*76sjfyemv', 2),
        User('gurpeetgill', 'gurpgill@grillsforu.net', '07652987709', 'youcantguess', 3)
    ]

    assert users == repository.all()

def test_create_user_adds_user_to_users(db_connection):
    db_connection.seed("seeds/reset_users_data.sql")
    db_connection.seed("seeds/listings.sql")

    new_user = User('urmauppal', 'urmau@umbrellasftw.com', '076352183911', 'terriblepwd')

    users = [
            User('kayleighkarpal', 'kayleighk@kickabout.com', '07635183911', 'badpassword', 1),
            User('mingma', 'maming@matsforcats.co.uk', '07876543909', '-*76sjfyemv', 2),
            User('gurpeetgill', 'gurpgill@grillsforu.net', '07652987709', 'youcantguess', 3),
            User('urmauppal', 'urmau@umbrellasftw.com', '076352183911', 'terriblepwd', 4)
            ]

    repository = UserRepository(db_connection)
    repository.create(new_user)

    assert repository.all() == users

def test_create_user_adds_user_with_existing_email_raises_value_error(db_connection):
    db_connection.seed("seeds/reset_users_data.sql")
    db_connection.seed("seeds/listings.sql")

    new_user = User('urmauppal', 'kayleighk@kickabout.com', '076352183911', 'terriblepwd')

    repository = UserRepository(db_connection)
    with pytest.raises(ValueError) as err :
        repository.create(new_user)
    

    assert str(err.value) == "Email already exists. Please log-in."

def test_find_by_email_returns_user_with_passed_email_address(db_connection):
    db_connection.seed("seeds/reset_users_data.sql")
    db_connection.seed("seeds/listings.sql")

    repository = UserRepository(db_connection)
    user = repository.find_by_email("gurpgill@grillsforu.net")

    

    assert user == User('gurpeetgill', 'gurpgill@grillsforu.net', '07652987709', 'youcantguess', 3)