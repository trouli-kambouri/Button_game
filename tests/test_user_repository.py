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