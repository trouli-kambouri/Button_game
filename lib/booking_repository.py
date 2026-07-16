from lib.bookings import Bookings

class BookingRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings;")
        return [Bookings(row["start_date"], row["end_date"], row["listing_id"], row["guest_id"], row["status"]) for row in rows]
    
    def find_by_listing_id(self, listing_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE listing_id = %s", [listing_id])

        return [Bookings(row["start_date"], row["end_date"], row["listing_id"], row["guest_id"], row["status"]) for row in rows]

    def find_by_guest_id(self, guest_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE guest_id = %s", [guest_id])

        return [Bookings(row["start_date"], row["end_date"], row["listing_id"], row["guest_id"], row["status"]) for row in rows]

    def find_by_status(self, status):
        rows = self._connection.execute("SELECT * FROM bookings WHERE status = %s", [status])
        
        return [Bookings(row["start_date"], row["end_date"], row["listing_id"], row["guest_id"], row["status"]) for row in rows]


    def create(self, booking):
        self._connection.execute("INSERT INTO booking (start_date, end_date, listing_id, guest_id, status) VALUES (%s, %s, %s, %s, %s)", 
                                [booking.start_date, booking.end_date, booking.listing_id, booking.guest_id, booking.status])
        
        return None
        

    def remove_booking(self, id):
        self._connection.execute("DELETE FROM bookings WHERE id = %s", [id])
        
        return None
