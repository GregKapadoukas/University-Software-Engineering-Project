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
from review import Review
from transaction import Transaction
from user import User
import globals
from transactionHistoryPage import TransactionHistoryPage
from searchPage import SearchPage
from dashboardPage import DashboardPage


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class GUI(ctk.CTk):
    def __init__(self, *args, **kwargs):

        ctk.CTk.__init__(self, *args, **kwargs)
        

        self.title("LibShare")

        label=ctk.CTkLabel(self, text="LibShare", font=("Arial", 35), text_color="#3A7ABF")
        label.pack(padx=10, pady=10)

        # Navigation Buttons
        buttonframe = ctk.CTkFrame(self)
        buttonframe.columnconfigure(0, weight=1)

        navSearchButton = ctk.CTkButton(buttonframe, text="Search", 
                                        command=lambda : self.show_frame(SearchPage))
        navSearchButton.grid(row=0, column=0, sticky=ctk.W+ctk.E)

        navDashboardButton = ctk.CTkButton(buttonframe, text="Dashboard", 
                                        command=lambda : self.show_frame(DashboardPage))
        navDashboardButton.grid(row=0, column=1, sticky=ctk.W+ctk.E)

        navMyBookOffersButton = ctk.CTkButton(buttonframe, text="My Book Offers", 
                                        command=lambda : self.show_frame(MyBookOffersPage))
        navMyBookOffersButton.grid(row=0, column=2, sticky=ctk.W+ctk.E)

        navMyBookRequestsButton = ctk.CTkButton(buttonframe, text="My Book Requests", 
                                        command=lambda : self.show_frame(MyBookRequestsPage))
        navMyBookRequestsButton.grid(row=0, column=3, sticky=ctk.W+ctk.E)

        navMyFavoritesButton = ctk.CTkButton(buttonframe, text="My Favorites", 
                                        command=lambda : self.show_frame(MyFavoritesPage))
        navMyFavoritesButton.grid(row=0, column=4, sticky=ctk.W+ctk.E)

        navNotificationsButton = ctk.CTkButton(buttonframe, text="Notifications", 
                                        command=lambda : self.show_frame(NotificationsPage))
        navNotificationsButton.grid(row=0, column=5, sticky=ctk.W+ctk.E)

        navTransactionHistory = ctk.CTkButton(buttonframe, text="Transaction History", 
                                        command=lambda : self.show_frame(TransactionHistoryPage))
        navTransactionHistory .grid(row=0, column=6, sticky=ctk.W+ctk.E)

        navMyProfileButton = ctk.CTkButton(buttonframe, text="My Profile", 
                                        command=lambda : self.show_frame(MyProfilePage))
        navMyProfileButton.grid(row=0, column=7, sticky=ctk.W+ctk.E)

        buttonframe.pack()

        # Creating a container
        self.container = ctk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        # Initializing frames to an empty array
        self.frames = {}

        # Iterating through a tuple consisting of the different page layouts

        for F in (SearchPage, Dashboard, MyBookOffersPage, MyBookRequestsPage,
                  MyFavoritesPage, NotificationsPage, TransactionHistoryPage, MyProfilePage):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.show_frame(SearchPage)


        # To display the current frame passed as parameter
    def show_frame(self, cont):
        self.frames = {}
        for F in (SearchPage, DashboardPage, MyBookOffersPage, MyBookRequestsPage,
                  MyFavoritesPage, NotificationsPage, TransactionHistory, MyProfilePage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")
        frame = self.frames[cont]
        frame.tkraise()

class MyBookOffersPage(ctk.CTkFrame):

    def getBookOfferData(self):
        bookData = []
        bookData.append(ctk.CTkEntry(self,placeholder_text="Book Name"))
        bookData[0].pack()  
        return bookData

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="My Book Offers")
        label.pack(padx=10, pady=10)
        BookOfferButtons = []
        BookOfferButtons.append(ctk.CTkButton(self,text="Add Book Offer",command=self.getBookOfferData))
        BookOfferButtons.append(ctk.CTkButton(self,text="Delete Book Offer"))
        BookOfferButtons.append(ctk.CTkButton(self,text="Select Book Offer"))
        for button in BookOfferButtons:
            button.pack()




class MyBookRequestsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="My Book Requests")
        label.pack(padx=10, pady=10)

class MyFavoritesPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="My Favorites")
        label.pack(padx=10, pady=10)

class NotificationsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Notifications")
        label.pack(padx=10, pady=10)



        

        

class MyProfilePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="My Profile")
        label.pack(padx=10, pady=10)
