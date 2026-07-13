class Listing():
    def __init__(self, title, description, price, owner_id ,id=None):
        # For MVP, description is used as proxy for location

        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.price = price
        self.id = id

    def __repr__(self):
        return(f"Listing({self.id}, {self.title}, {self.description}, £{self.price}, {self.owner_id})")
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    