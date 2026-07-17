import datetime as dt
from lib.listing_repository import ListingRepository
from lib.booking_repository import BookingRepository

def get_guest_booking_info(connection, user_id):
    
    booking_repo = BookingRepository(connection)
    bookings = booking_repo.find_bookings_by_guest_id(user_id)
    listings = get_listings_for_bookings(connection, bookings)
    booking_dates = format_date_strings(bookings)

    return [(booking, dates, listing) for booking, dates, listing in zip(bookings, booking_dates, listings)]

def get_owner_request_info(connection, user_id):

    booking_repo = BookingRepository(connection)
    bookings = booking_repo.find_bookings_by_owner_id(user_id)
    listings = get_listings_for_bookings(connection, bookings)
    booking_dates = format_date_strings(bookings)

    return [(booking, dates, listing) for booking, dates, listing in zip(bookings, booking_dates, listings)]

def get_listings_for_bookings(connection, booking_list):
    listing_repo = ListingRepository(connection)
    return [listing_repo.find_listing_by_id(booking.listing_id) for booking in booking_list]
    # ids = [booking.listing_id for booking in booking_list]

    # return listing_repo.find_listings_by_id_list(ids)

def format_date_strings(booking_list):
    dt_to_str = lambda d: dt.datetime.strftime(d,"%d-%m-%Y" )
    dates = [(dt_to_str(booking.start_date), dt_to_str(booking.end_date)) for booking in booking_list]
    return dates