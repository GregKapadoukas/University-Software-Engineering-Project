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
from searchPage import SearchPage
from dashboardPage import DashboardPage
from myProfilePage import MyProfilePage
import globals

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
                                        command=lambda : self.show_frame(NotificationsPage))
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
        for F in (SearchPage, DashboardPage, MyBookOffersPage, MyBookRequestsPage,
                  MyFavoritesPage, NotificationsPage, TransactionHistory, MyProfilePage):
            frame = F(self.container, self)
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
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="My Book Offers")
        label.pack(padx=10, pady=10)

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
        self.pageName = ctk.CTkLabel(self, text="Notifications", font=("Arial", 25), text_color="white",bg_color="#3A7ABF")
        self.pageName.pack(fill="x")
        
        def username1():
          
            
          Label6.destroy()
          Label7.destroy()
          Label8.destroy()
          Label9.destroy()
          Label10.destroy()
           
          
          
        
        buttf = ctk.CTkFrame(self)
        
        buttf.columnconfigure(0,weight=1)
        buttf.columnconfigure(1,weight=1)
        buttf.columnconfigure(2,weight=1)
        buttf.columnconfigure(3,weight=1)
        buttf.columnconfigure(4,weight=1)
        buttf.columnconfigure(5,weight=1)
        buttf.columnconfigure(6,weight=1)
        buttf.columnconfigure(7,weight=1)
        buttf.columnconfigure(8,weight=1)
        buttf.columnconfigure(9,weight=1)
        Button1= ctk.CTkButton(buttf,text="Remove User", text_color="red", bg_color="red",command=username1 )
        Button1.grid(row=1, column=5, sticky=ctk.E, columnspan = 1, rowspan = 1, padx=1, pady =1)
        
        Label1= ctk.CTkLabel(buttf,text="User") 
        Label1.grid(row=0, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1)
        Label2= ctk.CTkLabel(buttf,text="Book") 
        Label2.grid(row=0, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1)
        Label3= ctk.CTkLabel(buttf,text="Author") 
        Label3.grid(row=0, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=80, pady =1 )
        Label4= ctk.CTkLabel(buttf,text="Price Per Day") 
        Label4.grid(row=0, column=3, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=80, pady =1)
        Label5= ctk.CTkLabel(buttf,text="Delivery Type") 
        Label5.grid(row=0, column=4, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1) 
        Label61= ctk.CTkLabel(buttf,text="Remove us") 
        Label61.grid(row=0, column=5, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=80, pady =1)
        
        Label6= ctk.CTkLabel(buttf,text="Greg") 
        Label6.grid(row=1, column=0, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1)
        Label7= ctk.CTkLabel(buttf,text="David Cop") 
        Label7.grid(row=1, column=1, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1)
        Label8= ctk.CTkLabel(buttf,text="Charles dic") 
        Label8.grid(row=1, column=2, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=80, pady =1 )
        Label9= ctk.CTkLabel(buttf,text="4 euros") 
        Label9.grid(row=1, column=3, sticky=ctk.W, columnspan = 1, rowspan = 1, padx=80, pady =1)
        Label10= ctk.CTkLabel(buttf,text="Post") 
        Label10.grid(row=1, column=4, sticky=ctk.W, columnspan = 1, rowspan = 1, padx = 80, pady =1) 
       

         
        
        buttf.pack(side="top")


        
        
      
        
        




class TransactionHistory(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Transaction")
        label.pack(padx=10, pady=10)
      
