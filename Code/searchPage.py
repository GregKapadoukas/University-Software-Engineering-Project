import customtkinter as ctk
import datetime
from book import Book
from bookOffer import BookOffer
from bookRequest import BookRequest
from favorite import Favorite
from listing import Listing, DeliveryType
from notification import Notification
from review import Review
from transaction import Transaction
from user import User
from CTkMessagebox import CTkMessagebox
import globals

class SearchPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.__pageText = ctk.CTkLabel(self, text="Please Enter Your Search Term", font=("Arial", 25), text_color="#3A7ABF")
        self.__pageText.pack(padx=20, pady=20)

        self.__searchframe = ctk.CTkFrame(self)
        self.__searchframe .columnconfigure(0, weight=1)

        self.__searchEntry = ctk.CTkEntry(self.__searchframe, placeholder_text="Enter Search Term")
        self.__searchEntry.grid(row=0, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__searchButton = ctk.CTkButton(self.__searchframe, text="Search", command=self.search)
        self.__searchButton.grid(row=0, column=1, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__radiobutton_variable = ctk.IntVar()

        self.__chooseBooks = ctk.CTkRadioButton(self.__searchframe, text="Books", variable=self.__radiobutton_variable, value=1)
        self.__chooseBooks.grid(row=1, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__chooseUser = ctk.CTkRadioButton(self.__searchframe, text="Users", variable=self.__radiobutton_variable, value=2)
        self.__chooseUser .grid(row=2, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__chooseRequest = ctk.CTkRadioButton(self.__searchframe, text="Requests", variable=self.__radiobutton_variable, value=3)
        self.__chooseRequest.grid(row=3, column=0, sticky=ctk.W+ctk.E, padx=10, pady=10)

        self.__searchframe.pack()

        self.__searchResults = []

        self.__bookResultsFrame = ctk.CTkFrame(self)
        self.__userResultsFrame = ctk.CTkFrame(self)
        self.__requestResultsFrame = ctk.CTkFrame(self)

        self.__bookOfferersFrame = ctk.CTkFrame(self)
        self.__userProfileFrame = ctk.CTkFrame(self)
        self.__bookRequestersFrame = ctk.CTkFrame(self)

        self.__reviewsFrame = ctk.CTkFrame(self)

        self.__listSelectionButtons = []
    
    def clearFrames(self):
        for widget in self.__bookResultsFrame.winfo_children():
            widget.destroy()
        for widget in self.__userResultsFrame.winfo_children():
            widget.destroy()
        for widget in self.__requestResultsFrame.winfo_children():
            widget.destroy()
        for widget in self.__bookOfferersFrame.winfo_children():
            widget.destroy()
        for widget in self.__bookRequestersFrame.winfo_children():
            widget.destroy()
        for widget in self.__reviewsFrame.winfo_children():
            widget.destroy()

    def search(self):
        self.__bookResultsFrame.pack_forget()
        self.__userResultsFrame.pack_forget()
        self.__requestResultsFrame.pack_forget()

        self.__bookOfferersFrame.pack_forget()
        self.__userProfileFrame.pack_forget()
        self.__bookRequestersFrame.pack_forget()

        self.__reviewsFrame.pack_forget()

        self.clearFrames()
        
        self.__listSelectionButtons = []

        match self.__radiobutton_variable.get():
            case 1:
                self.__searchResults = BookOffer.searchBookOffer(self.__searchEntry.get(), globals.currentUser)

                self.__bookResultsFrame.columnconfigure(6, weight=1)

                titleText = ctk.CTkLabel(self.__bookResultsFrame, text="Title", font=("Arial", 25))
                authorText = ctk.CTkLabel(self.__bookResultsFrame, text="Author", font=("Arial", 25))
                genreText = ctk.CTkLabel(self.__bookResultsFrame, text="Genre", font=("Arial", 25))
                editionText = ctk.CTkLabel(self.__bookResultsFrame, text="Edition", font=("Arial", 25))
                publisherText = ctk.CTkLabel(self.__bookResultsFrame, text="Publisher", font=("Arial", 25))
                listActionText = ctk.CTkLabel(self.__bookResultsFrame, text="Action", font=("Arial", 25))

                titleText.grid(row=0, column=0, padx=10, pady=10)
                authorText.grid(row=0, column=1, padx=10, pady=10)
                genreText.grid(row=0, column=2, padx=10, pady=10)
                editionText.grid(row=0, column=3, padx=10, pady=10)
                publisherText.grid(row=0, column=4, padx=10, pady=10)
                listActionText.grid(row=0, column=5, padx=10, pady=10)

                i = 1
                for result in self.__searchResults:
                    ctk.CTkLabel(self.__bookResultsFrame, text=result.getBook().getName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                    ctk.CTkLabel(self.__bookResultsFrame, text=result.getBook().getAuthor(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                    ctk.CTkLabel(self.__bookResultsFrame, text=result.getBook().getGenre(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                    ctk.CTkLabel(self.__bookResultsFrame, text=result.getBook().getEdition(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                    ctk.CTkLabel(self.__bookResultsFrame, text=result.getBook().getPublisher(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                    self.__listSelectionButtons.append(ctk.CTkButton(self.__bookResultsFrame, text="List Offerers", font=("Arial", 15), command=lambda i=i :self.selectOffer(i-1)))
                    self.__listSelectionButtons[i-1].grid(row=i, column=5, padx=10, pady=10)
                    i+=1

                self.__bookResultsFrame.pack(padx=10, pady=10)

            case 2:
                self.__searchResults = User.searchUserProfile(self.__searchEntry.get(), globals.currentUser)

                self.__userResultsFrame.columnconfigure(9, weight=1)

                usernameText = ctk.CTkLabel(self.__userResultsFrame, text="Username", font=("Arial", 25))
                emailText = ctk.CTkLabel(self.__userResultsFrame, text="Email", font=("Arial", 25))
                ageText = ctk.CTkLabel(self.__userResultsFrame, text="Age", font=("Arial", 25))
                cityText = ctk.CTkLabel(self.__userResultsFrame, text="City", font=("Arial", 25))
                phoneNumberText = ctk.CTkLabel(self.__userResultsFrame, text="Phone Number", font=("Arial", 25))
                descriptionText = ctk.CTkLabel(self.__userResultsFrame, text="Description", font=("Arial", 25))
                scoreText = ctk.CTkLabel(self.__userResultsFrame, text="Score", font=("Arial", 25))
                listActionText = ctk.CTkLabel(self.__userResultsFrame, text="Action", font=("Arial", 25))

                usernameText.grid(row=0, column=0, padx=10, pady=10)
                emailText.grid(row=0, column=1, padx=10, pady=10)
                ageText.grid(row=0, column=2, padx=10, pady=10)
                cityText.grid(row=0, column=3, padx=10, pady=10)
                phoneNumberText.grid(row=0, column=4, padx=10, pady=10)
                descriptionText.grid(row=0, column=5, padx=10, pady=10)
                scoreText.grid(row=0, column=6, padx=10, pady=10)
                listActionText.grid(row=0, column=7, padx=10, pady=10)

                ctk.CTkLabel(self.__userResultsFrame, text=self.__searchResults[0].getUsername(), font=("Arial", 15)).grid(row=1, column=0, padx=10, pady=10)
                ctk.CTkLabel(self.__userResultsFrame, text=self.__searchResults[0].getEmail(), font=("Arial", 15)).grid(row=1, column=1, padx=10, pady=10)
                ctk.CTkLabel(self.__userResultsFrame, text=self.__searchResults[0].getAge(), font=("Arial", 15)).grid(row=1, column=2, padx=10, pady=10)
                ctk.CTkLabel(self.__userResultsFrame, text=self.__searchResults[0].getCity(), font=("Arial", 15)).grid(row=1, column=3, padx=10, pady=10)
                ctk.CTkLabel(self.__userResultsFrame, text=self.__searchResults[0].getPhoneNumber(), font=("Arial", 15)).grid(row=1, column=4, padx=10, pady=10)
                ctk.CTkLabel(self.__userResultsFrame, text=self.__searchResults[0].getDescription(), font=("Arial", 15)).grid(row=1, column=5, padx=10, pady=10)
                ctk.CTkLabel(self.__userResultsFrame, text=self.__searchResults[0].getScore(), font=("Arial", 15)).grid(row=1, column=6, padx=10, pady=10)
                self.__listSelectionButtons.append(ctk.CTkButton(self.__userResultsFrame, text="Add Favorite", font=("Arial", 15), command=lambda:self.selectUser(0)))
                self.__listSelectionButtons[0].grid(row=1, column=7, padx=10, pady=10)

                self.__userResultsFrame.pack(padx=10, pady=10)

                userReviews = Review.getUserReviews(self.__searchResults[0])
                #print(userReviews)

                self.__reviewsFrame.columnconfigure(4, weight=1)

                reviewerUsernameText = ctk.CTkLabel(self.__reviewsFrame, text="Reviewer Username", font=("Arial", 25))
                scoreText = ctk.CTkLabel(self.__reviewsFrame, text="Score", font=("Arial", 25))
                reviewCommentText = ctk.CTkLabel(self.__reviewsFrame, text="Review Comment", font=("Arial", 25))

                reviewerUsernameText.grid(row=0, column=0, padx=10, pady=10)
                scoreText.grid(row=0, column=1, padx=10, pady=10)
                reviewCommentText.grid(row=0, column=2, padx=10, pady=10)

                i = 1
                for result in userReviews:
                    ctk.CTkLabel(self.__reviewsFrame, text=result.getReviewer().getUsername(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                    ctk.CTkLabel(self.__reviewsFrame, text=result.getScore(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                    ctk.CTkLabel(self.__reviewsFrame, text=result.getReviewText(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                    i += 1

                self.__reviewsFrame.pack(padx=10, pady=10)
            case 3:
                self.__searchResults = BookRequest.searchBookRequest(self.__searchEntry.get(), globals.currentUser)

                self.__requestResultsFrame.columnconfigure(7, weight=1)

                titleText = ctk.CTkLabel(self.__requestResultsFrame, text="Title", font=("Arial", 25))
                authorText = ctk.CTkLabel(self.__requestResultsFrame, text="Author", font=("Arial", 25))
                genreText = ctk.CTkLabel(self.__requestResultsFrame, text="Genre", font=("Arial", 25))
                editionText = ctk.CTkLabel(self.__requestResultsFrame, text="Edition", font=("Arial", 25))
                publisherText = ctk.CTkLabel(self.__requestResultsFrame, text="Publisher", font=("Arial", 25))
                listActionText = ctk.CTkLabel(self.__requestResultsFrame, text="Action", font=("Arial", 25))

                titleText.grid(row=0, column=0, padx=10, pady=10)
                authorText.grid(row=0, column=1, padx=10, pady=10)
                genreText.grid(row=0, column=2, padx=10, pady=10)
                editionText.grid(row=0, column=3, padx=10, pady=10)
                publisherText.grid(row=0, column=4, padx=10, pady=10)
                listActionText.grid(row=0, column=5, padx=10, pady=10)

                i = 1
                for result in self.__searchResults:
                    ctk.CTkLabel(self.__requestResultsFrame, text=result.getBook().getName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                    ctk.CTkLabel(self.__requestResultsFrame, text=result.getBook().getAuthor(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                    ctk.CTkLabel(self.__requestResultsFrame, text=result.getBook().getGenre(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                    ctk.CTkLabel(self.__requestResultsFrame, text=result.getBook().getEdition(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                    ctk.CTkLabel(self.__requestResultsFrame, text=result.getBook().getPublisher(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                    self.__listSelectionButtons.append(ctk.CTkButton(self.__requestResultsFrame, text="List Requesters", font=("Arial", 15), command=lambda i=i:self.selectRequest(i-1)))
                    self.__listSelectionButtons[i-1].grid(row=i, column=5, padx=10, pady=10)
                    i+=1

                self.__requestResultsFrame.pack(padx=10, pady=10)
            case _:
                self.__searchResults = []

    def selectOffer(self, selection):
        bookResultsSelection = self.__searchResults[selection].getBook().getBookIDFromInstance(self.__searchResults[selection].getBook())
        bookOfferers = User.findUsersOfferingBook(bookResultsSelection, globals.currentUser.getID())

        self.__bookOfferersFrame.columnconfigure(7, weight=1)

        usernameText = ctk.CTkLabel(self.__bookOfferersFrame, text="Username", font=("Arial", 25))
        emailText = ctk.CTkLabel(self.__bookOfferersFrame, text="Email", font=("Arial", 25))
        cityText = ctk.CTkLabel(self.__bookOfferersFrame, text="City", font=("Arial", 25))
        scoreText = ctk.CTkLabel(self.__bookOfferersFrame, text="Score", font=("Arial", 25))
        deliveryTypeText = ctk.CTkLabel(self.__bookOfferersFrame, text="Delivery Type", font=("Arial", 25))
        pricePerDayText = ctk.CTkLabel(self.__bookOfferersFrame, text="Price Per Day", font=("Arial", 25))
        listActionText = ctk.CTkLabel(self.__bookOfferersFrame, text="Action", font=("Arial", 25))

        usernameText.grid(row=0, column=0, padx=10, pady=10)
        emailText.grid(row=0, column=1, padx=10, pady=10)
        cityText.grid(row=0, column=2, padx=10, pady=10)
        scoreText.grid(row=0, column=3, padx=10, pady=10)
        deliveryTypeText.grid(row=0, column=4, padx=10, pady=10)
        pricePerDayText.grid(row=0, column=5, padx=10, pady=10)
        listActionText.grid(row=0, column=6, padx=10, pady=10)

        rentButtons = []

        i = 1
        for result in bookOfferers:
            ctk.CTkLabel(self.__bookOfferersFrame, text=result.getUsername(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.__bookOfferersFrame, text=result.getEmail(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.__bookOfferersFrame, text=result.getCity(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
            ctk.CTkLabel(self.__bookOfferersFrame, text=result.getScore(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.__bookOfferersFrame, text=result.searchBookOfferByBook(bookResultsSelection).getDeliveryType(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
            ctk.CTkLabel(self.__bookOfferersFrame, text=result.searchBookOfferByBook(bookResultsSelection).getPricePerDay(), font=("Arial", 15)).grid(row=i, column=5, padx=10, pady=10)
            rentButtons.append(ctk.CTkButton(self.__bookOfferersFrame, text="Fill", font=("Arial", 15), command=
                                          lambda renter = globals.currentUser, owner=result,listing=result.searchBookOfferByBook(bookResultsSelection):
                                          self.createTransaction(renter, owner, listing)))
            rentButtons[i-1].grid(row=i, column=6, padx=10, pady=10)
            i+=1

        self.__bookOfferersFrame.pack(padx=10, pady=10)

    def selectUser(self, selection):
        userResultsSelection = self.__searchResults[selection].getID()
        globals.currentUser.addFavorite(userResultsSelection)

    def selectRequest(self, selection):
        requestResultsSelection = self.__searchResults[selection].getBook().getBookIDFromInstance(self.__searchResults[selection].getBook())
        bookOfferers = User.findUsersRequestingBook(requestResultsSelection)

        self.__bookRequestersFrame.columnconfigure(7, weight=1)

        usernameText = ctk.CTkLabel(self.__bookRequestersFrame, text="Username", font=("Arial", 25))
        emailText = ctk.CTkLabel(self.__bookRequestersFrame, text="Email", font=("Arial", 25))
        cityText = ctk.CTkLabel(self.__bookRequestersFrame, text="City", font=("Arial", 25))
        scoreText = ctk.CTkLabel(self.__bookRequestersFrame, text="Score", font=("Arial", 25))
        deliveryTypeText = ctk.CTkLabel(self.__bookRequestersFrame, text="Delivery Type", font=("Arial", 25))
        pricePerDayText = ctk.CTkLabel(self.__bookRequestersFrame, text="Price Per Day", font=("Arial", 25))
        listActionText = ctk.CTkLabel(self.__bookRequestersFrame, text="Action", font=("Arial", 25))

        usernameText.grid(row=0, column=0, padx=10, pady=10)
        emailText.grid(row=0, column=1, padx=10, pady=10)
        cityText.grid(row=0, column=2, padx=10, pady=10)
        scoreText.grid(row=0, column=3, padx=10, pady=10)
        deliveryTypeText.grid(row=0, column=4, padx=10, pady=10)
        pricePerDayText.grid(row=0, column=5, padx=10, pady=10)
        listActionText.grid(row=0, column=6, padx=10, pady=10)

        rentButtons = []

        i = 1
        for result in bookOfferers:
            ctk.CTkLabel(self.__bookRequestersFrame, text=result.getUsername(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.__bookRequestersFrame, text=result.getEmail(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.__bookRequestersFrame, text=result.getCity(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
            ctk.CTkLabel(self.__bookRequestersFrame, text=result.getScore(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.__bookRequestersFrame, text=result.searchBookRequestByBook(requestResultsSelection).getDeliveryType(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
            ctk.CTkLabel(self.__bookRequestersFrame, text=result.searchBookRequestByBook(requestResultsSelection).getPricePerDay(), font=("Arial", 15)).grid(row=i, column=5, padx=10, pady=10)
            rentButtons.append(ctk.CTkButton(self.__bookRequestersFrame, text="Fill", font=("Arial", 15), command=
                                          lambda renter=result, owner = globals.currentUser, listing=result.searchBookRequestByBook(requestResultsSelection):
                                          self.createTransaction(renter, owner, listing)))
            rentButtons[i-1].grid(row=i, column=6, padx=10, pady=10)
            i+=1

        self.__bookRequestersFrame.pack(padx=10, pady=10)

    def createTransaction(self, renter, owner, listing):
        if globals.currentUser.getBalance() > 30.0:
            transaction = Transaction(renter, owner, listing, datetime.datetime.now())
            transaction.acceptTransaction()
        else:
            msg = CTkMessagebox(title="Not Enough Money", message="The renter doesn't have enough money to cover the 30€ safety deposit", icon="cancel", option_1="Close")
            if msg.get() == "Close":
                msg.destroy()
