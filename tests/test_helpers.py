from lib.helpers import (
    format_date_strings,
    get_guest_booking_info,
    get_listings_for_bookings,
    get_owner_request_info,
)
from lib.booking_repository import BookingRepository


SEED_FILE = "seeds/setup_seed_tables.sql"


def test_format_date_strings_formats_booking_dates(
    db_connection,
):
    db_connection.seed(SEED_FILE)
    repository = BookingRepository(db_connection)

    bookings = repository.find_bookings_by_guest_id(4)

    assert format_date_strings(bookings) == [
        ("12-07-2026", "12-07-2026")
    ]


def test_get_listings_for_bookings_returns_the_matching_listing(
    db_connection,
):
    db_connection.seed(SEED_FILE)
    repository = BookingRepository(db_connection)

    bookings = repository.find_bookings_by_guest_id(4)
    listings = get_listings_for_bookings(
        db_connection,
        bookings,
    )

    assert len(listings) == 1
    assert listings[0].id == 10
    assert listings[0].title == (
        "Countryside cottage with sheep included"
    )


def test_get_guest_booking_info_combines_booking_dates_and_listing(
    db_connection,
):
    db_connection.seed(SEED_FILE)

    booking_info = get_guest_booking_info(
        db_connection,
        4,
    )

    assert len(booking_info) == 1

    booking, dates, listing = booking_info[0]

    assert booking.id == 7
    assert dates == ("12-07-2026", "12-07-2026")
    assert listing.id == 10
    assert listing.title == (
        "Countryside cottage with sheep included"
    )


def test_get_owner_request_info_returns_requests_for_owned_listings(
    db_connection,
):
    db_connection.seed(SEED_FILE)

    request_info = get_owner_request_info(
        db_connection,
        5,
    )

    assert len(request_info) == 1

    booking, dates, listing = request_info[0]

    assert booking.id == 6
    assert booking.status == "requested"
    assert dates == ("12-07-2026", "12-07-2026")
    assert listing.id == 12
    assert listing.title == (
        "Beach hut only 5 days walk from beach"
    )
