import datetime
from book import Book
from enum import Enum

class DeliveryType(Enum):
    Local_Meeting = 1
    By_Post = 2

class Listing:
    all = []
    id_incrementer = 0;
    def __init__(self, book: Book, price_per_day:float, delivery_type:DeliveryType, listing_date:datetime.datetime):


        self.__id = Listing.id_incrementer
        Listing.id_incrementer+=1
        self.__book= book
        self.__price_per_day = price_per_day
        self.__delivery_type = delivery_type
        self.__listing_date = listing_date

        Listing.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Book ID: {self.__book.getName()}, Price Per Day: {self.__price_per_day}, Listing Type: {self.__delivery_type}, Listing Date: {self.__listing_date}"
    
    def getID(self):
        return self.__id

    def getBook(self):
        return self.__book

    def getPricePerDay(self):
        return self.__price_per_day

    def getDeliveryType(self):
        return self.__delivery_type

    @staticmethod
    def getListingByID(listing_id:int):
        result = []
        for listing in Listing.all:
            if listing.getID() == listing_id:
                result.append(listing)
        return result

    def setPricePerDay(self,price):
        self.__price_per_day=price
    

#book1 = Book("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1, "George Allen and Unwin (UK) Houghton Mifflin (US)")
#listing1 = Listing(book1, 15.0, DeliveryType.Local_Meeting, datetime.datetime(2023,5,6))
#listing2 = Listing(book1, 15.0, DeliveryType.By_Post, datetime.datetime(2023,5,7))
#print(Listing.all)
