import datetime
from listing import Listing, DeliveryType
from book import Book

class BookOffer(Listing):
    all = []
    def __init__(self, book: Book, price_per_day:float, delivery_type:DeliveryType, listing_date:datetime.datetime):
        super().__init__(book, price_per_day, delivery_type, listing_date)
        BookOffer.all.append(self)

    def __del__(self):
        BookOffer.all.remove(self)

    def getType(self):
        return "Book Offer"

    @staticmethod
    def searchBookOffer(searchTerm:str, searching_user):
        result = []
        for bookOffer in BookOffer.all:
            if searchTerm in bookOffer.getBook().getName() or searchTerm in bookOffer.getBook().getAuthor():
                result.append(bookOffer)
        for bookOffer in searching_user.getBookOffers():
            if bookOffer in result:
                result.remove(bookOffer)
        return result
