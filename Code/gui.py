import customtkinter as ctk
import datetime
from transactionHistoryPage import TransactionHistoryPage
from searchPage import SearchPage
from dashboardPage import DashboardPage
from myBookOffersPage import MyBookOffersPage
from myBookRequestsPage import MyBookRequestsPage
from notificationsPage import NotificationsPage
from myProfilePage import MyProfilePage
from myFavoritesPage import MyFavoritesPage


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class GUI(ctk.CTk):
    def __init__(self, *args, **kwargs):

        ctk.CTk.__init__(self, *args, **kwargs)
        

        self.title("LibShare")

        self.__label=ctk.CTkLabel(self, text="LibShare", font=("Arial", 35), text_color="#3A7ABF")
        self.__label.pack(padx=10, pady=10)

        # Navigation Buttons
        self.__buttonframe = ctk.CTkFrame(self)
        self.__buttonframe.columnconfigure(0, weight=1)

        self.__navSearchButton = ctk.CTkButton(self.__buttonframe, text="Search", 
                                        command=lambda : self.show_frame(SearchPage))
        self.__navSearchButton.grid(row=0, column=0, sticky=ctk.W+ctk.E)

        self.__navDashboardButton = ctk.CTkButton(self.__buttonframe, text="Dashboard", 
                                        command=lambda : self.show_frame(DashboardPage))
        self.__navDashboardButton.grid(row=0, column=1, sticky=ctk.W+ctk.E)

        self.__navMyBookOffersButton = ctk.CTkButton(self.__buttonframe, text="My Book Offers", 
                                        command=lambda : self.show_frame(MyBookOffersPage))
        self.__navMyBookOffersButton.grid(row=0, column=2, sticky=ctk.W+ctk.E)

        self.__navMyBookRequestsButton = ctk.CTkButton(self.__buttonframe, text="My Book Requests", 
                                        command=lambda : self.show_frame(MyBookRequestsPage))
        self.__navMyBookRequestsButton.grid(row=0, column=3, sticky=ctk.W+ctk.E)

        self.__navMyFavoritesButton = ctk.CTkButton(self.__buttonframe, text="My Favorites", 
                                        command=lambda : self.show_frame(MyFavoritesPage))
        self.__navMyFavoritesButton.grid(row=0, column=4, sticky=ctk.W+ctk.E)

        self.__navNotificationsButton = ctk.CTkButton(self.__buttonframe, text="Notifications", 
                                        command=lambda : self.show_frame(NotificationsPage))
        self.__navNotificationsButton.grid(row=0, column=5, sticky=ctk.W+ctk.E)

        self.__navTransactionHistoryButton = ctk.CTkButton(self.__buttonframe, text="Transaction History", 
                                        command=lambda : self.show_frame(TransactionHistoryPage))
        self.__navTransactionHistoryButton .grid(row=0, column=6, sticky=ctk.W+ctk.E)

        self.__navMyProfileButton = ctk.CTkButton(self.__buttonframe, text="My Profile", 
                                        command=lambda : self.show_frame(MyProfilePage))
        self.__navMyProfileButton.grid(row=0, column=7, sticky=ctk.W+ctk.E)

        self.__buttonframe.pack()

        # Creating a __container
        self.__container = ctk.CTkFrame(self)
        self.__container.pack(side="top", fill="both", expand=True)
        self.__container.grid_rowconfigure(0, weight = 1)
        self.__container.grid_columnconfigure(0, weight = 1)

        # Initializing frames to an empty array
        self.__frames = {}

        # Iterating through a tuple consisting of the different page layouts

        for F in (SearchPage, DashboardPage, MyBookOffersPage, MyBookRequestsPage,
                  MyFavoritesPage, NotificationsPage, TransactionHistoryPage, MyProfilePage):
            frame = F(self.__container, self)

            self.__frames[F] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.show_frame(SearchPage)


        # To display the current frame passed as parameter
    def show_frame(self, cont):
        self.__frames = {}
        self.__frames[cont] = cont(self.__container, self)
        frame = self.__frames[cont]
        frame.grid(row = 0, column = 0, sticky="nsew")
        frame.tkraise()
