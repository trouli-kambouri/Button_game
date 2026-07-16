import datetime as dt

class Bookings():
    def __init__(self, start_date, end_date, listing_id, guest_id, status, id=None):
        self.start_date = self._get_date(start_date)
        self.end_date = self._get_date(end_date)
        self.listing_id = listing_id
        self.guest_id = guest_id
        self.status = status
        self.id = id

# change the below to bookings:
    def __repr__(self):
        return(f"Booking({self._format_date(self.start_date)}, {self._format_date(self.end_date)}, {self.listing_id}, {self.guest_id}, {self.status}")
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def _get_date(self, date):
        if type(date) == str:
            try:
                date = dt.datetime.strptime(date, '%Y-%m-%d').date()
            except ValueError:
                try:
                    date = dt.datetime.strptime(date, '%d-%m-%Y').date()
                except ValueError:
                    print("Date format unknown")
                
        return date
        

    def _format_date(self, date):
        if isinstance(date, (dt.date, dt.datetime)):
            return date.strftime("%d-%m-%Y")
