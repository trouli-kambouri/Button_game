import datetime as dt

from lib.listing import Listing


def test_listing_initialises_with_expected_fields_represented_in_string():
    listing_1 = Listing(
        1,
        "A beautiful hovel by the sea",
        "Place-on-Sea",
        32,
        "12-12-1987",
        "08-01-2020",
        "hovel.png",
        1
    )

    listing_2 = Listing(
        1,
        "A hideous hovel by the sea",
        "Place-on-Sea",
        31,
        "1987-12-12",
        "2020-01-08",
        "hideous-hovel.png",
        2
    )

    assert str(listing_1) == (
        "Listing(1, 1, A beautiful hovel by the sea, "
        "Place-on-Sea, 12-12-1987, 08-01-2020, "
        "£32, hovel.png)"
    )

    assert str(listing_2) == (
        "Listing(2, 1, A hideous hovel by the sea, "
        "Place-on-Sea, 12-12-1987, 08-01-2020, "
        "£31, hideous-hovel.png)"
    )


def test_listing_compares_listings_by_attributes():
    listing_1 = Listing(
        1,
        "A beautiful hovel by the sea",
        "Place-on-Sea",
        32,
        "12-12-1987",
        "08-01-2020",
        "hovel.png",
        1
    )

    listing_2 = Listing(
        1,
        "A palace on a hill",
        "Place-on-Sea",
        71,
        "12-12-1987",
        "08-01-2020",
        "palace.png",
        2
    )

    same_as_listing_1 = Listing(
        1,
        "A beautiful hovel by the sea",
        "Place-on-Sea",
        32,
        "12-12-1987",
        "08-01-2020",
        "hovel.png",
        1
    )

    assert listing_1 != listing_2
    assert listing_1 == same_as_listing_1


def test_listing_initialises_with_date_object():
    from_date = dt.datetime.strptime(
        "12-12-1987",
        "%d-%m-%Y"
    ).date()

    to_date = dt.datetime.strptime(
        "12-12-1988",
        "%d-%m-%Y"
    ).date()

    listing = Listing(
        2,
        "A house on the hill",
        "Hilltop",
        24,
        from_date,
        to_date,
        "hilltop.png",
        3
    )

    assert str(listing) == (
        "Listing(3, 2, A house on the hill, "
        "Hilltop, 12-12-1987, 12-12-1988, "
        "£24, hilltop.png)"
    )