from lib.booking_repository import BookingRepository
from lib.bookings import Bookings


SEED_FILE = "seeds/setup_seed_tables.sql"


def expected_seeded_bookings():
    return [
        Bookings(
            "2026-01-21",
            "2026-01-22",
            1,
            3,
            "completed",
            1,
        ),
        Bookings(
            "2026-01-11",
            "2026-01-22",
            1,
            2,
            "completed",
            2,
        ),
        Bookings(
            "2026-01-13",
            "2026-01-14",
            2,
            3,
            "completed",
            3,
        ),
        Bookings(
            "2026-07-21",
            "2026-07-22",
            4,
            2,
            "confirmed",
            4,
        ),
        Bookings(
            "2026-07-19",
            "2026-07-20",
            4,
            5,
            "denied",
            5,
        ),
        Bookings(
            "2026-07-12",
            "2026-07-12",
            12,
            3,
            "requested",
            6,
        ),
        Bookings(
            "2026-07-12",
            "2026-07-12",
            10,
            4,
            "requested",
            7,
        ),
    ]


def sort_by_id(bookings):
    return sorted(bookings, key=lambda booking: booking.id)


def test_all_returns_every_booking(db_connection):
    db_connection.seed(SEED_FILE)
    repository = BookingRepository(db_connection)

    assert sort_by_id(repository.all()) == expected_seeded_bookings()


def test_find_bookings_by_listing_id_returns_matching_bookings(
    db_connection,
):
    db_connection.seed(SEED_FILE)
    repository = BookingRepository(db_connection)

    actual = sort_by_id(
        repository.find_bookings_by_listing_id(1)
    )

    assert actual == expected_seeded_bookings()[:2]


def test_find_bookings_by_guest_id_returns_matching_bookings(
    db_connection,
):
    db_connection.seed(SEED_FILE)
    repository = BookingRepository(db_connection)

    actual = sort_by_id(
        repository.find_bookings_by_guest_id(3)
    )

    expected = [
        expected_seeded_bookings()[0],
        expected_seeded_bookings()[2],
        expected_seeded_bookings()[5],
    ]

    assert actual == expected


def test_find_bookings_by_owner_id_returns_requests_for_owned_listings(
    db_connection,
):
    db_connection.seed(SEED_FILE)
    repository = BookingRepository(db_connection)

    actual = sort_by_id(
        repository.find_bookings_by_owner_id(1)
    )

    expected = expected_seeded_bookings()[:3]

    assert actual == expected


def test_find_by_status_returns_matching_bookings(
    db_connection,
):
    db_connection.seed(SEED_FILE)
    repository = BookingRepository(db_connection)

    actual = sort_by_id(
        repository.find_by_status("requested")
    )

    expected = expected_seeded_bookings()[5:7]

    assert actual == expected


def test_create_adds_a_booking(db_connection):
    db_connection.seed(SEED_FILE)
    repository = BookingRepository(db_connection)

    repository.create(
        Bookings(
            "2026-08-01",
            "2026-08-03",
            12,
            2,
        )
    )

    created = db_connection.execute(
        """
        SELECT *
        FROM bookings
        WHERE id = %s
        """,
        [8],
    )

    assert len(created) == 1
    assert str(created[0]["start_date"]) == "2026-08-01"
    assert str(created[0]["end_date"]) == "2026-08-03"
    assert created[0]["listing_id"] == 12
    assert created[0]["guest_id"] == 2
    assert created[0]["status"] == "requested"


def test_remove_booking_deletes_the_booking_with_the_given_id(
    db_connection,
):
    db_connection.seed(SEED_FILE)
    repository = BookingRepository(db_connection)

    repository.remove_booking(1)

    remaining_ids = [
        booking.id
        for booking in repository.all()
    ]

    assert 1 not in remaining_ids
    assert len(remaining_ids) == 6
