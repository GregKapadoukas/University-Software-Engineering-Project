import customtkinter as ctk
import datetime
from book import Book
from bookOffer import BookOffer
from bookRequest import BookRequest
from favorite import Favorite
from listing import Listing, DeliveryType
from notification import Notification
from transaction import Transaction, Status
from review import Review
from gui import GUI
from user import User
import globals

globals.currentUser = User("Greg", "up1072484@upnet.gr", 22, "Patra", 150.0, "Mostly like non fiction", 698435686, "12345678")
xristos = User("Xristos", "xmpestis@gmail.com", 21, "Patra", 150.0, "Big Lord of the Rings fan", 698435686,"23456789")
george = User("George", "george@gmail.com", 57, "Patra", 150.0, "Enjoy reading fiction", 6928556745,"34567891")

xristos.addBookOffer("Harry Potter and the Philosopher's Stone", "J. K. Rowling", "Fantasy", 1,  "Bloomsbury", 1.0, DeliveryType.By_Post, datetime.datetime(2023,5,5))
xristos.addBookRequest("Harry Potter and the Chamber of Secrets", "J. K. Rowling", "Fantasy", 1,  "Bloomsbury", 1.0, DeliveryType.Local_Meeting, datetime.datetime(2023,5,5))

george.addBookOffer("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 1.0, DeliveryType.Local_Meeting, datetime.datetime(2023,5,5))
george.addBookRequest("The Lord of the Rings", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 1.0, DeliveryType.By_Post, datetime.datetime(2023,5,5))

globals.currentUser.addFavorite(xristos.getID())
globals.currentUser.addNotification(Notification(xristos.getID(), xristos.getBookOffers()[0]))
globals.currentUser.addNotification(Notification(xristos.getID(), xristos.getBookRequests()[0]))
globals.currentUser.addBookOffer("Software Engineering", "Ian Sommerville", "Non Fiction", 6,  "Addison-Wesley", 1.0, DeliveryType.Local_Meeting, datetime.datetime(2023,5,5))
globals.currentUser.addBookOffer("The Mythical Man-Month", "Fred Brooks", "Non Fiction", 1,  "Addison-Wesley", 1.0, DeliveryType.Local_Meeting, datetime.datetime(2023,5,5))
globals.currentUser.addBookRequest("The Pragmatic Programmer", "Andy Hunt and Dave Thomas", "Non Fiction", 1,  "Addison-Wesley", 5.0, DeliveryType.By_Post, datetime.datetime(2023,5,5))

transaction1 = Transaction(george,globals.currentUser,globals.currentUser.getBookOffers()[0],datetime.datetime(2023,5,5))
transaction2 = Transaction(globals.currentUser,xristos,xristos.getBookOffers()[0],datetime.datetime(2023,1,17))
transaction3 = Transaction(xristos,globals.currentUser,xristos.getBookRequests()[0],datetime.datetime(2022,12,20))

transaction2.addReview(globals.currentUser, xristos, 5.0, "Amazing service and book")

for transaction in Transaction.all:
	transaction.setStatus(Status.Finished)

transaction4 = Transaction(xristos,globals.currentUser,globals.currentUser.getBookOffers()[1],datetime.datetime(2023,2,27))


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
