import customtkinter as ctk
import datetime
from address import Address
from book import Book
from bookOffer import BookOffer
from bookRequest import BookRequest
from city import City
from favorite import Favorite
from listing import Listing, ListingType
from notification import Notification
from review import Review
from transaction import Transaction, Status
from gui import GUI
from user import User
import globals

globals.currentUser=User("Greg", "Kapadoukas", "up1072484@upnet.gr", 22, Address("MyStreet", "15", City("Patra", "Greece")), 150.0, 5.0)
user1 = User("Xristos", "Mpestitzanos", "xmpestis@gmail.com", 21, Address("Street2", "15", City("Patra", "Greece")), 150.0, 5.0)
user1.addBookOffer("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 15.0, ListingType.Local_Meeting, datetime.datetime(2023,5,5))
user1.addBookRequest("The Lord of the Rings", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 15.0, ListingType.Local_Meeting, datetime.datetime(2023,5,5))

transaction1 = Transaction(user1,globals.currentUser,user1.getBookOffers()[0],datetime.datetime.now())
transaction2 = Transaction(globals.currentUser,user1,user1.getBookOffers()[0],datetime.datetime.now())
transaction3 = Transaction(user1,globals.currentUser,user1.getBookOffers()[0],datetime.datetime.now())
transaction3 = Transaction(globals.currentUser,user1,user1.getBookOffers()[0],datetime.datetime.now())

for transaction in Transaction.all:
	transaction.setStatus(Status.Finished)


#result = User.findUsersOfferingBook(Book("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)"))
#print(result)
#result = User.findUsersRequestingBook(Book("The Lord of the Rings", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)"))
#print(result)
#print(Book("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)").isSame(Book("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)")))

app = GUI()
app.mainloop()
