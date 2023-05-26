import datetime
from listing import Listing, DeliveryType
from address import Address
from city import City
from book import Book
from notification import Notification
from favorite import Favorite
from bookOffer import BookOffer
from bookRequest import BookRequest

class User:
    all = []
    id_incrementer = 0;
    def __init__(self, first_name:str, last_name:str, email:str, age:int, address:Address, balance:float, score:float):
        assert age >= 0, f"Age {age} is not greater or equal to zero!"
        assert balance >= 0.0, f"Age {age} is not greater or equal to zero!"
        assert score >= 0.0 and score <= 5, f"Score {score} is not greater or equal to zero and less than or equal to five!"

        self.__id = User.id_incrementer
        User.id_incrementer+=1
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__age = age
        self.__address = address
        self.__balance = balance
        self.__score = score
        self.__bookOffers = []
        self.__bookRequests = []
        self.__favorites = []

        User.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, First Name: {self.__first_name}, Last Name: {self.__last_name}, Email: {self.__email}, Age: {self.__age}, Address: {self.__address}, Balance: {self.__balance}, Score: {self.__score}, Book Offers: {self.__bookOffers}, Book Requests: {self.__bookRequests}"

    def getID(self):
        return self.__id

    def getFirstName(self):
        return self.__first_name

    def getLastName(self):
        return self.__last_name

    def getEmail(self):
        return self.__email

    def getAge(self):
        return self.__age

    def getCity(self):
        return self.__address.getCity()

    def getBalance(self):
        return self.__balance

    def getScore(self):
        return self.__score

    def getFavorites(self):
        return self.__favorites
    
    def addBookOffer(self, book_name:str, book_author:str, book_genre:str, book_edition:int, book_publisher:str, price_per_day:float, delivery_type: DeliveryType, listing_date:datetime.datetime):
        book = Book(book_name, book_author, book_genre, book_edition, book_publisher)
        book_id = Book.getBookIDFromInstance(book)
        self.__bookOffers.append(BookOffer(book, price_per_day, delivery_type, listing_date))

    def addBookRequest(self, book_name:str, book_author:str, book_genre:str, book_edition:int, book_publisher:str, price_per_day:float, delivery_type: DeliveryType, listing_date:datetime.datetime):
        book = Book(book_name, book_author, book_genre, book_edition, book_publisher)
        book_id = Book.getBookIDFromInstance(book)
        self.__bookRequests.append(BookRequest(book, price_per_day, delivery_type, listing_date))

    def addFavorite(self,favoriteUserID):
        for favorite in self.__favorites:
            if favorite.getFavoriteUserID() == favoriteUserID:
                return
        self.__favorites.append(Favorite(favoriteUserID, datetime.datetime.now()))

    def searchBookOfferByBook(self, book_id:int):
        for bookOffer in self.__bookOffers:
            if bookOffer.getBook().getBookIDFromInstance(bookOffer.getBook()) == book_id:
                return bookOffer

    def searchBookRequestByBook(self, book_id:int):
        for bookRequest in self.__bookRequests:
            if bookRequest.getBook().getBookIDFromInstance(bookRequest.getBook()) == book_id:
                return bookRequest

    def getSafetyDeposit(self):
        if self.__balance > 30.0:
            self.__balance -= 30.0
            return True
        else:
            return False

    def addBalance(self, amount):
        self.__balance += amount

    def getBookOffers(self):
        return self.__bookOffers

    def getBookRequests(self):
        return self.__bookRequests

    def getListings(self):
        Listings = []
        Listing = self.__bookRequests + self.__bookOffers
        return Listings

    @staticmethod
    def searchUserProfile(searchTerm:str):
        result = []
        for user in User.all:
            if searchTerm == user.getFirstName() or searchTerm == user.getLastName():
                result.append(user)
                break
        return result


    @staticmethod
    def searchUserProfileByID(user_id:int):
        result = []
        for user in User.all:
            if user_id == user.getID():
                result.append(user)
                break
        return result

    @staticmethod
    def findUsersOfferingBook(book_id:int):
        result = []
        for user in User.all:
            for bookOffer in user.__bookOffers:
                if bookOffer.getBook().getBookIDFromInstance(bookOffer.getBook()) == book_id:
                    result.append(user)
        result = list(set(result))
        return result

    @staticmethod
    def findUsersRequestingBook(book_id:int):
        result = []
        for user in User.all:
            for bookRequest in user.__bookRequests:
                if bookRequest.getBook().getBookIDFromInstance(bookRequest.getBook()) == book_id:
                    result.append(user)
        result = list(set(result))
        return result

#user1 = User("Test", "Tetstson", "test@tester.com", 22, Address("Test Street", "5A", City("Patra", "Greece")), 15.0)
#user1.addListing("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 15.0, datetime.datetime.now())
#print(User.all)
