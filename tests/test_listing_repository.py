from lib.listing import Listing
from lib.listing_repository import ListingRepository


SEED_FILE = "seeds/setup_seed_tables.sql"


def expected_listings():
    return [
        Listing(
            1,
            "Rain-soaked shed on a mountain",
            "Greenfield",
            71,
            "2026-01-01",
            "2026-01-31",
            "Greenfield.png",
            1
        ),
        Listing(
            1,
            "Uncomfortable camper van in a lay-by",
            "Newtown",
            21,
            "2026-01-01",
            "2026-01-31",
            "Newton.png",
            2
        ),
        Listing(
            2,
            "Glamorous pad in fancy town",
            "Hopington",
            311,
            "2026-01-01",
            "2026-01-31",
            "Hopington.png",
            3
        ),
        Listing(
            2,
            "Medieval castle with ghost included",
            "Spooksville",
            199,
            "2025-10-31",
            "2026-11-01",
            "Spooksville.png",
            4
        ),
        Listing(
            3,
            "Luxury treehouse with unreliable ladder",
            "Treeford",
            89,
            "2025-10-01",
            "2026-06-29",
            "Treeford.png",
            5
        ),
        Listing(
            1,
            "Converted bus stop with panoramic traffic views",
            "Roundabout-on-Sea",
            34,
            "2026-07-10",
            "2026-08-31",
            "Roundabout-on-sea.png",
            6
        ),
        Listing(
            4,
            "Medieval prison cell",
            "Stonechester",
            66,
            "2026-02-03",
            "2026-07-21",
            "Stonechester.png",
            7
        ),
        Listing(
            2,
            "Studio flat above a loud pub",
            "Pintbury",
            88,
            "2026-05-01",
            "2026-09-21",
            "Pintbury.png",
            8
        ),
        Listing(
            5,
            "Floating house that is not sinking",
            "Above Mariana's Trench",
            112,
            "2026-05-01",
            "2026-11-10",
            "Above_marianas_trench.png",
            9
        ),
        Listing(
            3,
            "Countryside cottage with sheep included",
            "Baaxton",
            93,
            "2025-01-01",
            "2026-07-20",
            "Baaxton.png",
            10
        ),
        Listing(
            4,
            "Tiny house that is not a shed",
            "Little Houseton",
            68,
            "2026-01-01",
            "2026-08-31",
            "Little_Houseton.png",
            11
        ),
        Listing(
            5,
            "Beach hut only 5 days walk from beach",
            "Landlockedshire",
            58,
            "2026-03-01",
            "2026-09-30",
            "Landlockedshire.png",
            12
        )
    ]


def test_listing_repository_all_returns_list_of_all_listings(
    db_connection
):
    db_connection.seed(SEED_FILE)

    repository = ListingRepository(db_connection)

    assert repository.all() == expected_listings()


def test_listing_repository_returns_all_listings_with_owner_emails(
    db_connection
):
    db_connection.seed(SEED_FILE)

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

    expected = [
        [listing, email]
        for listing, email in zip(
            expected_listings(),
            owner_emails
        )
    ]

    repository = ListingRepository(db_connection)

    actual = repository.all_with_owner_emails()

    actual_sorted = sorted(
        actual,
        key=lambda item: item[0].id
    )

    expected_sorted = sorted(
        expected,
        key=lambda item: item[0].id
    )

    assert actual_sorted == expected_sorted


def test_listing_repository_returns_listing_with_id(
    db_connection
):
    db_connection.seed(SEED_FILE)

    expected = Listing(
        1,
        "Uncomfortable camper van in a lay-by",
        "Newtown",
        21,
        "2026-01-01",
        "2026-01-31",
        "Newton.png",
        2
    )

    repository = ListingRepository(db_connection)

    assert repository.find_listing_by_id(2) == expected

def test_listing_repository_returns_listings_with_ids_in_list(db_connection):
    db_connection.seed(SEED_FILE)

    expected_listings = [
        Listing(
            1,
            "Uncomfortable camper van in a lay-by",
            "Newtown",
            21,
            "2026-01-01",
            "2026-01-31",
            "Newton.png",
            2
        ),
        Listing(
            4,
            "Medieval prison cell",
            "Stonechester",
            66,
            "2026-02-03",
            "2026-07-21",
            "Stonechester.png",
            7
        ),
        Listing(
            5,
            "Floating house that is not sinking",
            "Above Mariana's Trench",
            112,
            "2026-05-01",
            "2026-11-10",
            "Above_marianas_trench.png",
            9
        ),
        Listing(
            3,
            "Countryside cottage with sheep included",
            "Baaxton",
            93,
            "2025-01-01",
            "2026-07-20",
            "Baaxton.png",
            10
        )
    ]

    repository = ListingRepository(db_connection)

    assert expected_listings == repository.find_listings_by_id_list([2, 7, 9, 10])


def test_listing_repository_adds_new_listing(
    db_connection
):
    db_connection.seed(SEED_FILE)

    repository = ListingRepository(db_connection)

    new_listing = Listing(
        1,
        "Palatial shed in a field",
        "Idyllicville",
        1010,
        "2026-02-01",
        "2026-02-28"
    )

    repository.create(new_listing)

    created_listing = repository.find_listing_by_id(13)

    assert created_listing == Listing(
        1,
        "Palatial shed in a field",
        "Idyllicville",
        1010,
        "2026-02-01",
        "2026-02-28",
        "placeholder.png",
        13
    )


def test_listing_repository_deletes_listing_with_given_id(
    db_connection
):
    db_connection.seed(SEED_FILE)

    repository = ListingRepository(db_connection)

    repository.remove(2)

    remaining_listings = repository.all()
    remaining_ids = [
        listing.id
        for listing in remaining_listings
    ]

    assert 2 not in remaining_ids
    assert len(remaining_listings) == 11
