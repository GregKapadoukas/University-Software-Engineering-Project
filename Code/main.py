
import customtkinter as ctk
import datetime
from address import Address
from book import Book
from bookOffer import BookOffer
from bookRequest import BookRequest
from city import City
from favorite import Favorite
from listing import Listing, DeliveryType
from notification import Notification
from review import Review, Score
from transaction import Transaction
from gui import GUI
from user import User
import globals

globals.currentUser=User("Greg", "Kapadoukas", "up1072484@upnet.gr", 22, "Patra", 150.0, 5.0, "scrumGuy", 698435686, "fg")
user1 = User("Xristos", "Mpestitzanos", "xmpestis@gmail.com", 21,  "Patra", 150.0, 5.0,"scrumGuy", 698435686,"wi")
user1.addBookOffer("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 1.0, DeliveryType.Local_Meeting, datetime.datetime(2023,5,5))
user1.addBookRequest("The Lord of the Rings", "J. R. R. Tolkien", "Fantasy", 1,  "George Allen and Unwin (UK) Houghton Mifflin (US)", 1.0, DeliveryType.Local_Meeting, datetime.datetime(2023,5,5))
review1 = Review(0,1,Score.FIVE,"Very Good")
review2 = Review(0,1,Score.FOUR,"Not as good")

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
