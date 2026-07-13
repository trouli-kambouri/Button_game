from lib.listing import Listing

def test_listing_intialises_with_expected_fields_represented_in_string():

    listing = Listing("A beautiful hovel by the sea", "Place-on-Sea", 32, 1, 1)

    assert str(listing) == "Listing(1, A beautiful hovel by the sea, Place-on-Sea, £32, 1)"

def test_listing_compares_listings_by_attributes():

    listing_1 = Listing("A beautiful hovel by the sea", "Place-on-Sea", 32, 1, 1)
    listing_2 = Listing("A palace on a hill", "Place-on-Sea", 71, 1, 2)

    assert listing_1 != listing_2
    assert listing_1 == Listing("A beautiful hovel by the sea", "Place-on-Sea", 32, 1, 1)
