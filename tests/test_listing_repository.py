from lib.listing_repository import ListingRepository
from lib.listing import Listing

def test_listing_repository_all_returns_list_of_all_listings(db_connection):
    db_connection.seed("seeds/reset_users_data.sql")
    db_connection.seed("seeds/listings.sql")


    repository = ListingRepository(db_connection)
    listings = [
        Listing(1, 'Rain-soaked shed on a mountain', 'Greenfield', 71, 1 ),
        Listing(1, 'Uncomfortable camper van in a lay-by', 'Newtown', 21, 2),
        Listing(2, 'Glamorous pad in fancy town', 'Hopington', 311, 3)
    ]

    assert listings == repository.all()

def test_listing_repository_returns_list_of_all_properties_with_owner_emails(db_connection):
    db_connection.seed("seeds/reset_users_data.sql")
    db_connection.seed("seeds/listings.sql")

    listings = [
        Listing(1, 'Rain-soaked shed on a mountain', 'Greenfield', 71, 1 ),
        Listing(1, 'Uncomfortable camper van in a lay-by', 'Newtown', 21, 2),
        Listing(2, 'Glamorous pad in fancy town', 'Hopington', 311, 3)
    ]
    owner_emails = [
        "kayleighk@kickabout.com",
        "kayleighk@kickabout.com",
        "maming@matsforcats.co.uk"
    ]
    repository = ListingRepository(db_connection)
    listing_details = repository.all_with_owner_details()

    assert [[listing, email] for (listing, email) in list(zip(listings, owner_emails))] == listing_details