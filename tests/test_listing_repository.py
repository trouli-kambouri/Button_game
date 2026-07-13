from lib.listing_repository import ListingRepository
from lib.listing import Listing

def test_listing_repository_all_returns_list_of_all_listings(db_connection):
    db_connection.seed("seeds/listings.sql")

    repository = ListingRepository(db_connection)
    listings = [
        Listing("Property 1", "Location 1", 32, 1, 1),
        Listing("Property 2", "Location 2", 32, 1, 2),
        Listing("Property 3", "Location 3", 32, 1, 3)
    ]

    assert listings == repository.all()

    