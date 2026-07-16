class Listing():
    def __init__(self, owner_id, title, description, price, thumbnail='placeholder.png', id=None):
        # For MVP, description is used as proxy for location

        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.price_per_night = price
        self.thumbnail = thumbnail
        self.id = id

    def __repr__(self):
        return(f"Listing({self.id}, {self.owner_id}, {self.title}, {self.description}, £{self.price_per_night}, {self.thumbnail})")
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
