import datetime
from book import Book
from enum import Enum

class ListingType(Enum):
    Local_Meeting = 1
    By_Post = 2

class Listing:
    #all = []
    id_incrementer = 0;
    def __init__(self, book:Book, price_per_day:float, listing_type:ListingType, listing_date:datetime.datetime):
        assert price_per_day >= 0.0, f"Age {price_per_day} is not greater or equal to zero!"

        self.__id = Listing.id_incrementer
        Listing.id_incrementer+=1
        self.__book = book
        self.__price_per_day = price_per_day
        self.__listing_type = type
        self.__listing_date = listing_date

        #Listing.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Book: {self.__book}, Price Per Day: {self.__price_per_day}, Listing Type: {self.__listing_type}, Listing Date: {self.__listing_date}"

    def getBook(self):
        return self.__book

#book1 = Book("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1, "George Allen and Unwin (UK) Houghton Mifflin (US)")
#listing1 = Listing(book1, 15.0, ListingType.Local_Meeting, datetime.datetime(2023,5,6))
#listing2 = Listing(book1, 15.0, ListingType.By_Post, datetime.datetime(2023,5,7))
#print(Listing.all)
