import datetime as dt
from lib.listing import Listing

class ListingRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM listings;")
        return [Listing(row["owner_id"], row["title"], row["description"], row["price_per_night"], row["available_from"], row["available_until"], row["thumbnail"], row["id"]) for row in rows]
    
    def all_with_owner_emails(self):
        # Should this do this or should it get the owner ids 
        # using all and query the owner details separately?
        query = """ SELECT
                        l.id AS property_id,
                        u.id AS owner_id,
                        u.email AS owner_email,
                        l.title,
                        l.description,
                        l.price_per_night,
                        l.available_from,
                        l.available_until,
                        l.thumbnail
                    FROM listings l
                        JOIN users u
                        ON l.owner_id = u.id;
        """

        rows = self._connection.execute(query)
        return [[Listing(row["owner_id"], row["title"], row["description"], row["price_per_night"], row["available_from"], row["available_until"], row["thumbnail"], row["property_id"]), row["owner_email"]] for row in rows]

    def find_listing_by_id(self, property_id):
        
        result = self._connection.execute("SELECT * FROM listings WHERE id = %s", [property_id])[0]

        return Listing(result["owner_id"], result["title"], result["description"], result["price_per_night"], result["available_from"], result["available_until"], result["thumbnail"], result["id"])
    
    def find_listings_by_id_list(self, id_list):

        rows = self._connection.execute("SELECT * FROM listings WHERE id = ANY(%s)", [id_list])

        return [Listing(row["owner_id"], row["title"], row["description"], row["price_per_night"], row["available_from"], row["available_until"], row["thumbnail"], row["id"]) for row in rows]


    def create(self, listing):
        # DB wants dates as YYYY-MM-DD
        self._connection.execute("INSERT INTO listings (owner_id, title, description, price_per_night, available_from, available_until, thumbnail) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                                [listing.owner_id, listing.title, listing.description, listing.price_per_night, listing.available_from, listing.available_until, listing.thumbnail])
        
        return None
        
    def remove(self, id):
        self._connection.execute("DELETE FROM listings WHERE id = %s", [id])
        return None


    def convert_date_to_string(self, date):
        return dt.datetime.strftime(date, '%d-%m-%Y')
    
