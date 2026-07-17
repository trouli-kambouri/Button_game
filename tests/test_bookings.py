import datetime as dt

from lib.bookings import Bookings


def test_booking_initialises_with_expected_attributes():
    booking = Bookings(
        "2026-07-21",
        "2026-07-22",
        4,
        2,
        "confirmed",
        1,
    )

    assert booking.start_date == dt.date(2026, 7, 21)
    assert booking.end_date == dt.date(2026, 7, 22)
    assert booking.listing_id == 4
    assert booking.guest_id == 2
    assert booking.status == "confirmed"
    assert booking.id == 1


def test_booking_uses_requested_as_its_default_status():
    booking = Bookings(
        "2026-08-01",
        "2026-08-03",
        12,
        3,
    )

    assert booking.status == "requested"
    assert booking.id is None


def test_booking_accepts_both_supported_date_formats():
    iso_booking = Bookings(
        "2026-07-21",
        "2026-07-22",
        4,
        2,
    )

    uk_booking = Bookings(
        "21-07-2026",
        "22-07-2026",
        4,
        2,
    )

    assert iso_booking.start_date == uk_booking.start_date
    assert iso_booking.end_date == uk_booking.end_date


def test_booking_representation_contains_all_fields():
    booking = Bookings(
        "2026-07-21",
        "2026-07-22",
        4,
        2,
        "confirmed",
        7,
    )

    assert str(booking) == (
        "Booking(21-07-2026, 22-07-2026, "
        "4, 2, confirmed, 7)"
    )


def test_bookings_compare_by_their_attributes():
    booking = Bookings(
        "2026-07-21",
        "2026-07-22",
        4,
        2,
        "confirmed",
        7,
    )

    assert booking == Bookings(
        "21-07-2026",
        "22-07-2026",
        4,
        2,
        "confirmed",
        7,
    )

    assert booking != Bookings(
        "2026-07-21",
        "2026-07-23",
        4,
        2,
        "confirmed",
        7,
    )