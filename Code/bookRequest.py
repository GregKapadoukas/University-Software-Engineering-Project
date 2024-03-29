import datetime
from listing import Listing, DeliveryType
from book import Book

class BookRequest(Listing):
    all = []
    def __init__(self, book:Book, price_per_day:float, delivery_type:DeliveryType, listing_date:datetime.datetime):
        super().__init__(book, price_per_day, delivery_type, listing_date)

        BookRequest.all.append(self)

    def __del__(self):
        BookRequest.all.remove(self)

    def getType(self):
        return "Book Request"

    @staticmethod
    def searchBookRequest(searchTerm:str, searching_user):
        result = []
        for bookRequest in BookRequest.all:
            if searchTerm in bookRequest.getBook().getName() or searchTerm in bookRequest.getBook().getAuthor():
                result.append(bookRequest)
        for bookRequest in searching_user.getBookOffers():
            if bookRequest in result:
                result.remove(bookRequest)
        return result
