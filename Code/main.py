import customtkinter as ctk
import datetime
from book import Book
from bookOffer import BookOffer
from bookRequest import BookRequest
from favorite import Favorite
from listing import Listing, DeliveryType
from notification import Notification
from transaction import Transaction, Status
from review import Review, Score
from gui import GUI
from user import User
import globals

globals.currentUser = User("Greg", "Kapadoukas", "up1072484@upnet.gr", 22, "Patra", 150.0, 5.0, "Mostly like non fiction", 698435686, "12345678")
user1 = User("Xristos", "Mpestitzanos", "xmpestis@gmail.com", 21, "Patra", 150.0, 5.0, "Big Harry Potter fan", 698435686,"23456789")
user1.addBookOffer("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 1.0, DeliveryType.Local_Meeting, datetime.datetime(2023,5,5))
user1.addBookRequest("The Lord of the Rings", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 1.0, DeliveryType.Local_Meeting, datetime.datetime(2023,5,5))
globals.currentUser.addFavorite(user1.getID())
globals.currentUser.addNotification(Notification(user1.getID(), user1.getBookOffers()[0]))
globals.currentUser.addNotification(Notification(user1.getID(), user1.getBookRequests()[0]))
review1 = Review(0,1,Score.FIVE,"Very Good")
review2 = Review(0,1,Score.FOUR,"Not as good")
globals.currentUser.addBookOffer("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 1.0, DeliveryType.Local_Meeting, datetime.datetime(2023,5,5))
globals.currentUser.addBookOffer("The Lord of the Rings", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 1.0, DeliveryType.Local_Meeting, datetime.datetime(2023,5,5))
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
#print(User.all)
#print(Book.unique)
#print(BookOffer.all)
#print(BookRequest.all)

app = GUI()
app.mainloop()
