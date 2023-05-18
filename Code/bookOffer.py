import datetime
from listing import Listing, DeliveryType
from book import Book

class BookOffer(Listing):
    all = []
    def __init__(self, book_id:int, price_per_day:float, delivery_type:DeliveryType, listing_date:datetime.datetime):
        super().__init__(book_id, price_per_day, delivery_type, listing_date)

        BookOffer.all.append(self)

    @staticmethod
    def searchBookOffer(searchTerm:str):
        result = []
        for bookOffer in BookOffer.all:
            if searchTerm in bookOffer.getBook().getName() or searchTerm in bookOffer.getBook().getAuthor():
                result.append(bookOffer)
        return result
