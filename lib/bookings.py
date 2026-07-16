class Bookings():
    def __init__(self, start_date, end_date, listing_id, guest_id, status, id=None):
        self.start_date = start_date
        self.end_date = end_date
        self.listing_id = listing_id
        self.guest_id = guest_id
        self.status = status
        self.id = id

# change the below to bookings:
    def __repr__(self):
        return(f"Booking({self.start_date}, {self.end_date}, {self.listing_id}, {self.guest_id}, {self.status}")
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
