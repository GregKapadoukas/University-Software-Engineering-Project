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
from transaction import Transaction
from user import User
import globals
from transactionHistoryPage import TransactionHistoryPage

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
                                        command=lambda : self.show_frame(Dashboard))
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
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

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
        frame = self.frames[cont]
        frame.tkraise()

class SearchPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.pageText = ctk.CTkLabel(self, text="Please Enter Your Search Term", font=("Arial", 25), text_color="#3A7ABF")
        self.pageText.pack(padx=20, pady=20)

        self.searchframe = ctk.CTkFrame(self)
        self.searchframe .columnconfigure(0, weight=1)

        self.searchEntry = ctk.CTkEntry(self.searchframe, placeholder_text="Enter Search Term")
        self.searchEntry.grid(row=0, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.searchButton = ctk.CTkButton(self.searchframe, text="Search", command=self.search)
        self.searchButton.grid(row=0, column=1, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.radiobutton_variable = ctk.IntVar()

        self.chooseBooks = ctk.CTkRadioButton(self.searchframe, text="Books", variable=self.radiobutton_variable, value=1)
        self.chooseBooks.grid(row=1, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.chooseUser = ctk.CTkRadioButton(self.searchframe, text="Users", variable=self.radiobutton_variable, value=2)
        self.chooseUser .grid(row=2, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.chooseRequest = ctk.CTkRadioButton(self.searchframe, text="Requests", variable=self.radiobutton_variable, value=3)
        self.chooseRequest.grid(row=3, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.searchframe.pack()

        self.results = []

        self.bookResultsFrame = ctk.CTkFrame(self)
        self.requestResultsFrame = ctk.CTkFrame(self)
        self.userResultsFrame = ctk.CTkFrame(self)

    def search(self):
        self.bookResultsFrame.pack_forget()
        self.requestResultsFrame.pack_forget()
        self.userResultsFrame.pack_forget()

        match self.radiobutton_variable.get():
            case 1:
                self.results = BookOffer.searchBookOffer(self.searchEntry.get())

                self.bookResultsFrame.columnconfigure(6, weight=1)

                titleText = ctk.CTkLabel(self.bookResultsFrame, text="Title", font=("Arial", 25))
                authorText = ctk.CTkLabel(self.bookResultsFrame, text="Author", font=("Arial", 25))
                genreText = ctk.CTkLabel(self.bookResultsFrame, text="Genre", font=("Arial", 25))
                editionText = ctk.CTkLabel(self.bookResultsFrame, text="Edition", font=("Arial", 25))
                publisherText = ctk.CTkLabel(self.bookResultsFrame, text="Publisher", font=("Arial", 25))
                listActionText = ctk.CTkLabel(self.bookResultsFrame, text="Action", font=("Arial", 25))

                titleText.grid(row=0, column=0, padx=10, pady=10)
                authorText.grid(row=0, column=1, padx=10, pady=10)
                genreText.grid(row=0, column=2, padx=10, pady=10)
                editionText.grid(row=0, column=3, padx=10, pady=10)
                publisherText.grid(row=0, column=4, padx=10, pady=10)
                listActionText.grid(row=0, column=5, padx=10, pady=10)

                i = 1
                for result in self.results:
                    ctk.CTkLabel(self.bookResultsFrame, text=result.getBook().getName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                    ctk.CTkLabel(self.bookResultsFrame, text=result.getBook().getAuthor(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                    ctk.CTkLabel(self.bookResultsFrame, text=result.getBook().getGenre(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                    ctk.CTkLabel(self.bookResultsFrame, text=result.getBook().getEdition(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                    ctk.CTkLabel(self.bookResultsFrame, text=result.getBook().getPublisher(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                    ctk.CTkButton(self.bookResultsFrame, text="List Offerers", font=("Arial", 15)).grid(row=i, column=5, padx=10, pady=10)
                    i+=1
                    

                self.bookResultsFrame.pack(padx=10, pady=10)
            case 2:
                self.results = User.searchUser(self.searchEntry.get())

                firstNameText = ctk.CTkLabel(self.userResultsFrame, text="First Name", font=("Arial", 25))
                lastNameText = ctk.CTkLabel(self.userResultsFrame, text="Last Name", font=("Arial", 25))
                emailText = ctk.CTkLabel(self.userResultsFrame, text="Email", font=("Arial", 25))
                ageText = ctk.CTkLabel(self.userResultsFrame, text="Age", font=("Arial", 25))
                cityText = ctk.CTkLabel(self.userResultsFrame, text="City", font=("Arial", 25))
                listActionText = ctk.CTkLabel(self.userResultsFrame, text="Action", font=("Arial", 25))

                firstNameText.grid(row=0, column=0, padx=10, pady=10)
                lastNameText.grid(row=0, column=1, padx=10, pady=10)
                emailText.grid(row=0, column=2, padx=10, pady=10)
                ageText.grid(row=0, column=3, padx=10, pady=10)
                cityText.grid(row=0, column=4, padx=10, pady=10)
                listActionText.grid(row=0, column=5, padx=10, pady=10)

                i = 1
                for result in self.results:
                    ctk.CTkLabel(self.userResultsFrame, text=result.getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                    ctk.CTkLabel(self.userResultsFrame, text=result.getLastName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                    ctk.CTkLabel(self.userResultsFrame, text=result.getEmail(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                    ctk.CTkLabel(self.userResultsFrame, text=result.getAge(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                    ctk.CTkLabel(self.userResultsFrame, text=result.getCity(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                    ctk.CTkButton(self.userResultsFrame, text="Add Favorite", font=("Arial", 15)).grid(row=i, column=5, padx=10, pady=10)
                    i+=1

                self.userResultsFrame.pack(padx=10, pady=10)
            case 3:
                self.results = BookRequest.searchBookRequest(self.searchEntry.get())

                self.requestResultsFrame.columnconfigure(6, weight=1)

                titleText = ctk.CTkLabel(self.requestResultsFrame, text="Title", font=("Arial", 25))
                authorText = ctk.CTkLabel(self.requestResultsFrame, text="Author", font=("Arial", 25))
                genreText = ctk.CTkLabel(self.requestResultsFrame, text="Genre", font=("Arial", 25))
                editionText = ctk.CTkLabel(self.requestResultsFrame, text="Edition", font=("Arial", 25))
                publisherText = ctk.CTkLabel(self.requestResultsFrame, text="Publisher", font=("Arial", 25))
                listActionText = ctk.CTkLabel(self.requestResultsFrame, text="Action", font=("Arial", 25))

                titleText.grid(row=0, column=0, padx=10, pady=10)
                authorText.grid(row=0, column=1, padx=10, pady=10)
                genreText.grid(row=0, column=2, padx=10, pady=10)
                editionText.grid(row=0, column=3, padx=10, pady=10)
                publisherText.grid(row=0, column=4, padx=10, pady=10)
                listActionText.grid(row=0, column=5, padx=10, pady=10)

                i = 1
                for result in self.results:
                    ctk.CTkLabel(self.requestResultsFrame, text=result.getBook().getName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                    ctk.CTkLabel(self.requestResultsFrame, text=result.getBook().getAuthor(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                    ctk.CTkLabel(self.requestResultsFrame, text=result.getBook().getGenre(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                    ctk.CTkLabel(self.requestResultsFrame, text=result.getBook().getEdition(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                    ctk.CTkLabel(self.requestResultsFrame, text=result.getBook().getPublisher(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                    ctk.CTkButton(self.requestResultsFrame, text="List Requesters", font=("Arial", 15)).grid(row=i, column=5, padx=10, pady=10)
                    i+=1

                self.requestResultsFrame.pack(padx=10, pady=10)
            case _:
                self.results = []


class Dashboard(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.pageRentFromText = ctk.CTkLabel(self, text="Renting From Other Users", font=("Arial", 25), text_color="#3A7ABF")
        self.pageRentFromText.pack(padx=10, pady=10)


        self.rentFromGrid = ctk.CTkFrame(self)
        self.rentFromGrid.columnconfigure(7, weight=1)


        self.rentFromOwnerText = ctk.CTkLabel(self.rentFromGrid, text="Owner", font=("Arial", 25))
        self.rentFromScoreText = ctk.CTkLabel(self.rentFromGrid, text="Score", font=("Arial", 25))
        self.rentFromBookText = ctk.CTkLabel(self.rentFromGrid, text="Book", font=("Arial", 25))
        self.rentFromStatusText = ctk.CTkLabel(self.rentFromGrid, text="Status", font=("Arial", 25))
        self.rentFromDateText = ctk.CTkLabel(self.rentFromGrid, text="Date", font=("Arial", 25))
        self.rentFromAmountText = ctk.CTkLabel(self.rentFromGrid, text="Total Amount", font=("Arial", 25))
        self.rentFromToggleText = ctk.CTkLabel(self.rentFromGrid, text="Toggle Possesion", font=("Arial", 25))


        self.rentFromOwnerText.grid(row=0, column=0, padx=10, pady=10)
        self.rentFromScoreText.grid(row=0, column=1, padx=10, pady=10)
        self.rentFromBookText.grid(row=0, column=2, padx=10, pady=10)
        self.rentFromStatusText.grid(row=0, column=3, padx=10, pady=10)
        self.rentFromDateText.grid(row=0, column=4, padx=10, pady=10)
        self.rentFromAmountText.grid(row=0, column=5, padx=10, pady=10)
        self.rentFromToggleText.grid(row=0, column=6, padx=10, pady=10)
        
        self.rentFromGrid.pack()

        self.pageRentToText = ctk.CTkLabel(self, text="Renting To Other Users", font=("Arial", 25), text_color="#3A7ABF")
        self.pageRentToText.pack(padx=10, pady=10)

        self.rentToGrid = ctk.CTkFrame(self)
        self.rentToGrid.columnconfigure(7, weight=1)

        self.rentToOwnerText = ctk.CTkLabel(self.rentToGrid, text="Owner", font=("Arial", 25))
        self.rentToScoreText = ctk.CTkLabel(self.rentToGrid, text="Score", font=("Arial", 25))
        self.rentToBookText = ctk.CTkLabel(self.rentToGrid, text="Book", font=("Arial", 25))
        self.rentToStatusText = ctk.CTkLabel(self.rentToGrid, text="Status", font=("Arial", 25))
        self.rentToDateText = ctk.CTkLabel(self.rentToGrid, text="Date", font=("Arial", 25))
        self.rentToAmountText = ctk.CTkLabel(self.rentToGrid, text="Total Amount", font=("Arial", 25))
        self.rentToToggleText = ctk.CTkLabel(self.rentToGrid, text="Toggle Possesion", font=("Arial", 25))

        self.rentToScoreText.grid(row=0, column=1, padx=10, pady=10)
        self.rentToBookText.grid(row=0, column=2, padx=10, pady=10)
        self.rentToStatusText.grid(row=0, column=3, padx=10, pady=10)
        self.rentToDateText.grid(row=0, column=4, padx=10, pady=10)
        self.rentToAmountText.grid(row=0, column=5, padx=10, pady=10)
        self.rentToToggleText.grid(row=0, column=6, padx=10, pady=10)
        self.rentToOwnerText.grid(row=0, column=0, padx=10, pady=10)

        self.rentToGrid.pack()


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
