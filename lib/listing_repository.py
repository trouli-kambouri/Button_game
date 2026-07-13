from listing import Listing

class ListingRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM listings;")

        return [Listing(row["title"], row["description"], row["price"], row["owner_id"], row["id"]) for row in rows]
    
    def all_with_details(self):
        pass

        


