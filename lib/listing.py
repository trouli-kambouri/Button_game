import datetime as dt

class Listing():
    def __init__(self, owner_id, title, description, price, available_from, available_until, id=None):
        # For MVP, description is used as proxy for location

        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.price_per_night = price
        self.available_from = dt.datetime.strptime(available_from, '%d-%m-%Y').date
        self.available_until = dt.datetime.strptime(available_until, '%d-%m-%Y').date
        self.id = id

    def __repr__(self):
        return(f"Listing({self.id}, {self.owner_id}, {self.title}, {self.description}, \
               {self.available_from}, {self.available_until}, £{self.price_per_night})")
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
