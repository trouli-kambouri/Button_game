class User():
    def __init__(self, name, email, phone_number, password, id =None):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.id = id

    def __repr__(self):
        return(f"User({self.id}, {self.name}, {self.email}, {self.phone_number}, £{self.password})")
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    