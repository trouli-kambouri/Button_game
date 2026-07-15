from lib.listing_repository import ListingRepository
from lib.listing import Listing

def test_listing_repository_all_returns_list_of_all_listings(db_connection):
    db_connection.seed("seeds/reset_users_data.sql")
    db_connection.seed("seeds/listings.sql")


    repository = ListingRepository(db_connection)
    listings = [
            Listing(1, 'Rain-soaked shed on a mountain', 'Greenfield', 71, '01-01-2026', '31-01-2026', 1),
            Listing(1, 'Uncomfortable camper van in a lay-by', 'Newtown', 21, '01-01-2026', '31-01-2026', 2),
            Listing(2, 'Glamorous pad in fancy town', 'Hopington', 311, '01-01-2026', '31-01-2026', 3),
            Listing(2, 'Medieval castle with ghost included', 'Spooksville', 199, '01-01-2026', '31-01-2026', 4),
            Listing(3, 'Luxury treehouse with unreliable ladder', 'Treeford', 89, '01-01-2026', '31-01-2026', 5),
            Listing(1, 'Converted bus stop with panoramic traffic views', 'Roundabout-on-Sea', 34, '01-01-2026', '31-01-2026', 6),
            Listing(4, 'Medieval prison cell', 'Stonechester', 66, '01-01-2026', '31-01-2026', 7),
            Listing(2, 'Studio flat above a loud pub', 'Pintbury', 88, '01-01-2026', '31-01-2026', 8),
            Listing(5, 'Floating house that is not sinking', 'Above Mariana\'s Trench', 112, '01-01-2026', '31-01-2026', 9),
            Listing(3, 'Countryside cottage with sheep included', 'Baaxton', 93, '01-01-2026', '31-01-2026', 10),
            Listing(4, 'Tiny house that is not a shed', 'Little Houseton', 68, '01-01-2026', '31-01-2026', 11),
            Listing(5, 'Beach hut only 5 days walk from beach', 'Landlockedshire', 58, '01-01-2026', '31-01-2026', 12) 
    ]

    assert listings == repository.all()

def test_listing_repository_returns_list_of_all_properties_with_owner_emails(db_connection):
    db_connection.seed("seeds/reset_users_data.sql")
    db_connection.seed("seeds/listings.sql")

    listings = [
            Listing(1, 'Rain-soaked shed on a mountain', 'Greenfield', 71, '01-01-2026', '31-01-2026', 1),
            Listing(2, 'Glamorous pad in fancy town', 'Hopington', 311, '01-01-2026', '31-01-2026', 3),
            Listing(2, 'Medieval castle with ghost included', 'Spooksville', 199, '01-01-2026', '31-01-2026', 4),
            Listing(3, 'Luxury treehouse with unreliable ladder', 'Treeford', 89, '01-01-2026', '31-01-2026', 5),
            Listing(1, 'Converted bus stop with panoramic traffic views', 'Roundabout-on-Sea', 34, '01-01-2026', '31-01-2026', 6),
            Listing(4, 'Medieval prison cell', 'Stonechester', 66, '01-01-2026', '31-01-2026', 7),
            Listing(2, 'Studio flat above a loud pub', 'Pintbury', 88, '01-01-2026', '31-01-2026', 8),
            Listing(5, 'Floating house that is not sinking', 'Above Mariana\'s Trench', 112, '01-01-2026', '31-01-2026', 9),
            Listing(3, 'Countryside cottage with sheep included', 'Baaxton', 93, '01-01-2026', '31-01-2026', 10),
            Listing(4, 'Tiny house that is not a shed', 'Little Houseton', 68, '01-01-2026', '31-01-2026', 11),
            Listing(5, 'Beach hut only 5 days walk from beach', 'Landlockedshire', 58, '01-01-2026', '31-01-2026', 12)

    ]
    owner_emails = [
        "kayleighk@kickabout.com",
        "kayleighk@kickabout.com",
        "maming@matsforcats.co.uk",
        "maming@matsforcats.co.uk",
        "gurpgill@grillsforu.net",
        "kayleighk@kickabout.com",
        "salsal@salsalsalads.net",
        "maming@matsforcats.co.uk",
        "ttipple@taliastipples.co.uk",
        "gurpgill@grillsforu.net",
        "salsal@salsalsalads.net",
        "ttipple@taliastipples.co.uk"
    ]
    repository = ListingRepository(db_connection)
    listing_details = repository.all_with_owner_emails()

    assert [[listing, email] for (listing, email) in list(zip(listings, owner_emails))] == listing_details

def test_listing_repository_returns_listing_with_id(db_connection):
    db_connection.seed("seeds/reset_users_data.sql")
    db_connection.seed("seeds/listings.sql")

    listing = Listing(1, 'Uncomfortable camper van in a lay-by', 'Newtown', 21, 2, '01-01-2026', '31-01-2026')

    repository = ListingRepository(db_connection)

    assert listing == repository.find_by_listing_id(2)


def test_listing_adds_new_listing(db_connection):
    db_connection.seed("seeds/reset_users_data.sql")
    db_connection.seed("seeds/listings.sql")

    listing = Listing(1, 'Palacial shed in a field', 'Idyllicville', 1010, 4, '01-01-2026', '31-01-2026')

    repository = ListingRepository(db_connection)
    repository.create(listing)

    listings = [
            Listing(1, 'Rain-soaked shed on a mountain', 'Greenfield', 71, '01-01-2026', '31-01-2026', 1),
            Listing(1, 'Uncomfortable camper van in a lay-by', 'Newtown', 21, '01-01-2026', '31-01-2026', 2),
            Listing(2, 'Glamorous pad in fancy town', 'Hopington', 311, '01-01-2026', '31-01-2026', 3),
            Listing(2, 'Medieval castle with ghost included', 'Spooksville', 199, '01-01-2026', '31-01-2026', 4),
            Listing(3, 'Luxury treehouse with unreliable ladder', 'Treeford', 89, '01-01-2026', '31-01-2026', 5),
            Listing(1, 'Converted bus stop with panoramic traffic views', 'Roundabout-on-Sea', 34, '01-01-2026', '31-01-2026', 6),
            Listing(4, 'Medieval prison cell', 'Stonechester', 66, '01-01-2026', '31-01-2026', 7),
            Listing(2, 'Studio flat above a loud pub', 'Pintbury', 88, '01-01-2026', '31-01-2026', 8),
            Listing(5, 'Floating house that is not sinking', 'Above Mariana\'s Trench', 112, '01-01-2026', '31-01-2026', 9),
            Listing(3, 'Countryside cottage with sheep included', 'Baaxton', 93, '01-01-2026', '31-01-2026', 10),
            Listing(4, 'Tiny house that is not a shed', 'Little Houseton', 68, '01-01-2026', '31-01-2026', 11),
            Listing(5, 'Beach hut only 5 days walk from beach', 'Landlockedshire', 58, '01-01-2026', '31-01-2026', 12),
            Listing(1, 'Palacial shed in a field', 'Idyllicville', 1010, '01-01-2026', '31-01-2026', 13)     
        ]

    assert listings == repository.all()

def test_listing_repository_deletes_listing_with_given_id(db_connection):
    db_connection.seed("seeds/reset_users_data.sql")
    db_connection.seed("seeds/listings.sql")

    repository = ListingRepository(db_connection)

    listings = [
        Listing(1, 'Rain-soaked shed on a mountain', 'Greenfield', 71, 1 , '01-01-2026', '31-01-2026', 1),
        Listing(2, 'Glamorous pad in fancy town', 'Hopington', 311, 3, '01-01-2026', '31-01-2026', 1),
        Listing(2, 'Medieval castle with ghost included', 'Spooksville', 199, 4, '01-01-2026', '31-01-2026', 1),
        Listing(3, 'Luxury treehouse with unreliable ladder', 'Treeford', 89, 5, '01-01-2026', '31-01-2026', 1),
        Listing(1, 'Converted bus stop with panoramic traffic views', 'Roundabout-on-Sea', 34, 6, '01-01-2026', '31-01-2026', 1),
        Listing(4, 'Medieval prison cell', 'Stonechester', 66, 7, '01-01-2026', '31-01-2026', 1),
        Listing(2, 'Studio flat above a loud pub', 'Pintbury', 88, 8, '01-01-2026', '31-01-2026', 1),
        Listing(5, 'Floating house that is not sinking', 'Above Mariana\'s Trench', 112, 9, '01-01-2026', '31-01-2026', 1),
        Listing(3, 'Countryside cottage with sheep included', 'Baaxton', 93, 10, '01-01-2026', '31-01-2026', 1),
        Listing(4, 'Tiny house that is not a shed', 'Little Houseton', 68, 11, '01-01-2026', '31-01-2026', 1),
        Listing(5, 'Beach hut only 5 days walk from beach', 'Landlockedshire', 58, 12, '01-01-2026', '31-01-2026')
    ]

    repository.remove(2)

    assert listings == repository.all()
