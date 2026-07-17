import pytest
from lib.booking_repository import BookingRepository
from lib.bookings import Bookings


def test_booking_repository_all_returns_list_of_all_bookings(db_connection):
    db_connection.seed("seeds/bookings.sql")

    repository = BookingRepository(db_connection)
    bookings = [

                    Bookings('2026-01-21', '2026-01-22', 1, 3, 'completed', 1),
                    Bookings('2026-01-11', '2026-01-22', 1, 2, 'completed', 2),
                    Bookings('2026-01-13', '2026-01-14', 2, 3, 'completed', 3),
                    Bookings('2026-07-21', '2026-07-22', 4, 2, 'confirmed', 4),
                    Bookings('2026-07-19', '2026-07-20', 4, 5, 'denied', 5),
                    Bookings('2026-07-12', '2026-07-12', 12, 3, 'requested', 6),
                    Bookings('2026-07-12', '2026-07-12', 10, 4, 'requested', 7)
    ]

    assert bookings == repository.all()

def test_booking_repo_returns_booking_found_by_listing_id(db_connection):
    db_connection.seed("seeds/bookings.sql")

    repository = BookingRepository(db_connection)
    bookings = [Bookings('2026-01-13', '2026-01-14', 2, 3, 'completed', 3)]

    assert repository.find_bookings_by_listing_id(2) == bookings

def test_booking_repo_returns_booking_found_by_guest_id(db_connection):
    db_connection.seed("seeds/bookings.sql")

    repository = BookingRepository(db_connection)
    bookings = [
                    Bookings('2026-01-11', '2026-01-22', 1, 2, 'completed', 2),
                    Bookings('2026-07-21', '2026-07-22', 4, 2, 'confirmed', 4)                    
    ]
    assert repository.find_bookings_by_guest_id(2) == bookings

def test_booking_repo_returns_booking_found_by_owner_id(db_connection):
    db_connection.seed("seeds/bookings.sql")

    repository = BookingRepository(db_connection)
    bookings = [
                    Bookings('2026-07-21', '2026-07-22', 4, 2, 'confirmed', 4),
                    Bookings('2026-07-19', '2026-07-20', 4, 5, 'denied', 5)
    ]
    assert repository.find_bookings_by_owner_id(2) == bookings

def test_booking_repo_returns_booking_found_by_status(db_connection):
    db_connection.seed("seeds/bookings.sql")

    repository = BookingRepository(db_connection)
    bookings = [
                    Bookings('2026-07-21', '2026-07-22', 4, 2, 'confirmed', 4)
    ]
    assert repository.find_by_status("confirmed") == bookings

def test_booking_repo_adds_new_booking_reflected_in_bookings_list(db_connection):
    db_connection.seed("seeds/bookings.sql")

    repository = BookingRepository(db_connection)

    new_booking = Bookings('2026-07-28', '2026-07-29', 11, 3, 'requested')

    bookings = [

                    Bookings('2026-01-21', '2026-01-22', 1, 3, 'completed', 1),
                    Bookings('2026-01-11', '2026-01-22', 1, 2, 'completed', 2),
                    Bookings('2026-01-13', '2026-01-14', 2, 3, 'completed', 3),
                    Bookings('2026-07-21', '2026-07-22', 4, 2, 'confirmed', 4),
                    Bookings('2026-07-19', '2026-07-20', 4, 5, 'denied', 5),
                    Bookings('2026-07-12', '2026-07-12', 12, 3, 'requested', 6),
                    Bookings('2026-07-12', '2026-07-12', 10, 4, 'requested', 7),
                    Bookings('2026-07-28', '2026-07-29', 11, 3, 'requested', 8)
    ]

    assert repository.create(new_booking) == None

    assert repository.all() == bookings


def test_booking_repo_removing_booking_reflected_in_bookings_list(db_connection):
    db_connection.seed("seeds/bookings.sql")

    repository = BookingRepository(db_connection)

    bookings = [

                Bookings('2026-01-21', '2026-01-22', 1, 3, 'completed', 1),
                Bookings('2026-01-11', '2026-01-22', 1, 2, 'completed', 2),
                Bookings('2026-07-21', '2026-07-22', 4, 2, 'confirmed', 4),
                Bookings('2026-07-19', '2026-07-20', 4, 5, 'denied', 5),
                Bookings('2026-07-12', '2026-07-12', 12, 3, 'requested', 6),
                Bookings('2026-07-12', '2026-07-12', 10, 4, 'requested', 7)
    ]

    repository.remove_booking(3)
    assert repository.all() == bookings