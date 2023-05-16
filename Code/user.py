import datetime
from listing import Listing
from address import Address
from city import City
from book import Book
from notification import Notification
from favorite import Favorite

class User:
    all = []
    id_incrementer = 0;
    def __init__(self, first_name:str, last_name:str, email:str, age:int, address:Address, balance:float):
        assert age >= 0, f"Age {age} is not greater or equal to zero!"
        assert balance >= 0.0, f"Age {age} is not greater or equal to zero!"

        self.__id = User.id_incrementer
        User.id_incrementer+=1
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__age = age
        self.__address = address
        self.__balance = balance
        self.__listings = []

        User.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, First Name: {self.__first_name}, Last Name: {self.__last_name}, Email: {self.__email}, Age: {self.__age}, Address: {self.__address}, Balance: {self.__balance}, Listings: {self.__listings}"

    def addListing(self, book_name:str, book_author:str, book_genre:str, book_edition:int, book_publisher:str, price_per_day:float, listing_date:datetime.datetime):
        self.__listings.append(Listing(Book(book_name, book_author, book_genre, book_edition, book_publisher), price_per_day, listing_date))

#user1 = User("Test", "Tetstson", "test@tester.com", 22, Address("Test Street", "5A", City("Patra", "Greece")), 15.0)
#user1.addListing("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 15.0, datetime.datetime.now())
#print(User.all)
