from lib.listing import Listing

class ListingRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM listings;")

        return [Listing(row["owner_id"], row["title"], row["description"], row["price_per_night"], row["id"]) for row in rows]
    
    def all_with_owner_details(self):
        # Should this do this or should it get the owner ids 
        # using all and query the owner details separately?
        query = """ SELECT
                        l.id AS property_id,
                        u.id AS owner_id,
                        u.email AS owner_email,
                        l.title,
                        l.description,
                        l.price_per_night
                    FROM listings l
                        JOIN users u
                        ON l.owner_id = u.id;
        """

        rows = self._connection.execute(query)
        return [[Listing(row["owner_id"], row["title"], row["description"], row["price_per_night"], row["property_id"]), row["owner_email"]] for row in rows]




