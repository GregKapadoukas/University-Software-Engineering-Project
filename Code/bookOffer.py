import datetime
from listing import Listing, ListingType
from book import Book

class BookOffer(Listing):
    all = []
    def __init__(self, book:Book, price_per_day:float, listing_type:ListingType, listing_date:datetime.datetime):
        super().__init__(book, price_per_day, listing_type, listing_date)

        BookOffer.all.append(self)

    @staticmethod
    def searchBookOffer(searchTerm:str):
        result = []
        for bookOffer in BookOffer.all:
            if searchTerm in bookOffer.getBook().getName() or searchTerm in bookOffer.getBook().getAuthor():
                result.append(bookOffer)
        result = list(set(result))
        return result


    

