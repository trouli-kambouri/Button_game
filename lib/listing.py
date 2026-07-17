import datetime as dt

class Listing():
    def __init__(self, owner_id, title, description, price, available_from, available_until, thumbnail='placeholder.png', id=None):
        # Added dates for available from and until

        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.price_per_night = price
        self.available_from = self._get_date(available_from)
        self.available_until = self._get_date(available_until)
        self.thumbnail = thumbnail
        self.id = id
        
    def __repr__(self):

        return(f"Listing({self.id}, {self.owner_id}, {self.title}, {self.description}, {self._format_date(self.available_from)}, {self._format_date(self.available_until)}, £{self.price_per_night}, {self.thumbnail})")
    
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
        