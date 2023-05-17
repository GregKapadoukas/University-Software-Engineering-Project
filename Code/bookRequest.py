import datetime
from listing import Listing, ListingType
from book import Book

class BookRequest(Listing):
    all = []
    def __init__(self, book:Book, price_per_day:float, listing_type:ListingType, listing_date:datetime.datetime):
        super().__init__(book, price_per_day, listing_type, listing_date)

        BookRequest.all.append(self)

    @staticmethod
    def searchBookRequest(searchTerm:str):
        result = []
        for bookRequest in BookRequest.all:
            if searchTerm in bookRequest.getBook().getName() or searchTerm in bookRequest.getBook().getAuthor():
                result.append(bookRequest)
        result = list(set(result))
        return result
