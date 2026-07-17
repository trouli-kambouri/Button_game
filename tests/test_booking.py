from lib.bookings import Bookings

def test_Booking_intialises_with_expected_fields_represented_in_string():

    booking_1 = Bookings('2026-07-12', '2026-07-13', 1, 3, "confirmed", 1)
    booking_2 = Bookings('2026-07-22', '2026-07-23', 2, 1, "requested", 2)

    assert str(booking_1) == "Booking(12-07-2026, 13-07-2026, 1, 3, confirmed, 1)"
    assert str(booking_2) == "Booking(22-07-2026, 23-07-2026, 2, 1, requested, 2)"
