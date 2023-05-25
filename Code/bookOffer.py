import datetime
from listing import Listing, DeliveryType
from book import Book


class BookOffer(Listing):
    all = []
    def __init__(self, book: Book, price_per_day:float, delivery_type:DeliveryType, listing_date:datetime.datetime):
        super().__init__(book, price_per_day, delivery_type, listing_date)
        BookOffer.all.append(self)

    def __del__(self):
        print("deleteddddddddddddddddddddddddddddddd")
        BookOffer.all.remove(self)



    @staticmethod
    def searchBookOffer(searchTerm:str):
        result = []
        for bookOffer in BookOffer.all:
            if searchTerm in bookOffer.getBook().getName() or searchTerm in bookOffer.getBook().getAuthor():
                result.append(bookOffer)
        return result


    

