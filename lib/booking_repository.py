from lib.bookings import Bookings

class BookingRepository():

    def __init__(self, connection):
        self._connection = connection


    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings;")
        return [Bookings(row["start_date"], row["end_date"], row["listing_id"], row["guest_id"], row["status"]) for row in rows]
    
    def find_bookings_by_listing_id(self, listing_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE listing_id = %s", [listing_id])

        return [Bookings(row["start_date"], row["end_date"], row["listing_id"], row["guest_id"], row["status"]) for row in rows]

    def find_bookings_by_guest_id(self, guest_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE guest_id = %s", [guest_id])

        return [Bookings(row["start_date"], row["end_date"], row["listing_id"], row["guest_id"], row["status"]) for row in rows]

    def find_by_status(self, status):
        rows = self._connection.execute("SELECT * FROM bookings WHERE status = %s", [status])
        
        return [Bookings(row["start_date"], row["end_date"], row["listing_id"], row["guest_id"], row["status"]) for row in rows]


    def create(self, booking):
        self._connection.execute("INSERT INTO bookings (start_date, end_date, listing_id, guest_id, status) VALUES (%s, %s, %s, %s, %s)", 
                                [booking.start_date, booking.end_date, booking.listing_id, booking.guest_id, booking.status])
        
        return None
        

    def remove_booking(self, id):
        self._connection.execute("DELETE FROM bookings WHERE id = %s", [id])
        
        return None


    def find_all_bookings_with_owner_id(self):
        # Should this do this or should it get the owner ids 
        # using all and query the owner details separately?
        query = """ SELECT
                        l.id AS property_id,
                        u.id AS owner_id,
                        u.email AS owner_email,
                        l.title,
                        l.description,
                        l.price_per_night,
                        l.available_from,
                        l.available_until,
                        l.thumbnail
                    FROM listings l
                        JOIN users u
                        ON l.owner_id = u.id;
        """