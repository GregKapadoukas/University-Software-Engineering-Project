import datetime
from listing import Listing
from book import Book

class BookRequest(Listing):
    def __init__(self, book:Book, price_per_day:float, listing_date:datetime.datetime):
        super().__init__(book, price_per_day, listing_date)
