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
        self.convert_dates_to_correct_type()
        

    def __repr__(self):

        format_from = self.available_from
        format_until = self.available_until

        if isinstance(self.available_from, (dt.date, dt.datetime)):
            format_from = self.available_from.strftime("%d-%m-%Y")
            format_until = self.available_until.strftime("%d-%m-%Y")

        return(f"Listing({self.id}, {self.owner_id}, {self.title}, {self.description}, {format_from}, {format_until}, £{self.price_per_night})")
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def convert_dates_to_correct_type(self):
        if type(self.available_from) == "str":
            self.available_from = dt.datetime.strptime(self.available_from, '%d-%m-%Y').date()
        
        if type(self.available_until) == "str":
            self.available_until = dt.datetime.strptime(self.available_until, '%d-%m-%Y').date()
        
    