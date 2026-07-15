import datetime as dt

class Listing():
    def __init__(self, owner_id, title, description, price, available_from, available_until, id=None):
        # Added dates for available from and until

        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.price_per_night = price
        self.id = id
        self.available_from = available_from
        self.available_until = available_until
        self._convert_datestrings_to_dates()
        
    def __repr__(self):

        return(f"Listing({self.id}, {self.owner_id}, {self.title}, {self.description}, {self._format_date(self.available_from)}, {self._format_date(self.available_until)}, £{self.price_per_night})")
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def _convert_datestrings_to_dates(self):
        if type(self.available_from) == str:
            self.available_from = dt.datetime.strptime(self.available_from, '%d-%m-%Y').date()
        
        if type(self.available_until) == str:
            self.available_until = dt.datetime.strptime(self.available_until, '%d-%m-%Y').date()

    def _format_date(self, date):
        if isinstance(date, (dt.date, dt.datetime)):
            return date.strftime("%d-%m-%Y")