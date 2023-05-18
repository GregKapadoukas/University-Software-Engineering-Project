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
        self.userResultsFrame = ctk.CTkFrame(self)
        self.requestResultsFrame = ctk.CTkFrame(self)

        self.bookOfferersFrame = ctk.CTkFrame(self)
        self.userProfileFrame = ctk.CTkFrame(self)
        self.bookRequestersFrame = ctk.CTkFrame(self)

        self.reviewsFrame = ctk.CTkFrame(self)

        self.buttons = []
    
    def clearFrames(self):
        for widget in self.bookResultsFrame.winfo_children():
            widget.destroy()
        for widget in self.userResultsFrame.winfo_children():
            widget.destroy()
        for widget in self.requestResultsFrame.winfo_children():
            widget.destroy()
        for widget in self.bookOfferersFrame.winfo_children():
            widget.destroy()
        for widget in self.bookRequestersFrame.winfo_children():
            widget.destroy()
        for widget in self.reviewsFrame.winfo_children():
            widget.destroy()

    def search(self):
        self.bookResultsFrame.pack_forget()
        self.userResultsFrame.pack_forget()
        self.requestResultsFrame.pack_forget()

        self.bookOfferersFrame.pack_forget()
        self.userProfileFrame.pack_forget()
        self.bookRequestersFrame.pack_forget()

        self.reviewsFrame.pack_forget()

        self.clearFrames()
        
        self.buttons = []

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
                    self.buttons.append(ctk.CTkButton(self.bookResultsFrame, text="List Offerers", font=("Arial", 15), command=lambda i=i :self.selectOffer(i-1)))
                    self.buttons[i-1].grid(row=i, column=5, padx=10, pady=10)
                    i+=1

                self.bookResultsFrame.pack(padx=10, pady=10)

            case 2:
                self.results = User.searchUserProfile(self.searchEntry.get())

                self.userResultsFrame.columnconfigure(7, weight=1)

                firstNameText = ctk.CTkLabel(self.userResultsFrame, text="First Name", font=("Arial", 25))
                lastNameText = ctk.CTkLabel(self.userResultsFrame, text="Last Name", font=("Arial", 25))
                emailText = ctk.CTkLabel(self.userResultsFrame, text="Email", font=("Arial", 25))
                ageText = ctk.CTkLabel(self.userResultsFrame, text="Age", font=("Arial", 25))
                cityText = ctk.CTkLabel(self.userResultsFrame, text="City", font=("Arial", 25))
                scoreText = ctk.CTkLabel(self.userResultsFrame, text="Score", font=("Arial", 25))
                listActionText = ctk.CTkLabel(self.userResultsFrame, text="Action", font=("Arial", 25))

                firstNameText.grid(row=0, column=0, padx=10, pady=10)
                lastNameText.grid(row=0, column=1, padx=10, pady=10)
                emailText.grid(row=0, column=2, padx=10, pady=10)
                ageText.grid(row=0, column=3, padx=10, pady=10)
                cityText.grid(row=0, column=4, padx=10, pady=10)
                scoreText.grid(row=0, column=5, padx=10, pady=10)
                listActionText.grid(row=0, column=6, padx=10, pady=10)

                ctk.CTkLabel(self.userResultsFrame, text=self.results[0].getFirstName(), font=("Arial", 15)).grid(row=1, column=0, padx=10, pady=10)
                ctk.CTkLabel(self.userResultsFrame, text=self.results[0].getLastName(), font=("Arial", 15)).grid(row=1, column=1, padx=10, pady=10)
                ctk.CTkLabel(self.userResultsFrame, text=self.results[0].getEmail(), font=("Arial", 15)).grid(row=1, column=2, padx=10, pady=10)
                ctk.CTkLabel(self.userResultsFrame, text=self.results[0].getAge(), font=("Arial", 15)).grid(row=1, column=3, padx=10, pady=10)
                ctk.CTkLabel(self.userResultsFrame, text=self.results[0].getCity(), font=("Arial", 15)).grid(row=1, column=4, padx=10, pady=10)
                ctk.CTkLabel(self.userResultsFrame, text=self.results[0].getScore(), font=("Arial", 15)).grid(row=1, column=5, padx=10, pady=10)
                self.buttons.append(ctk.CTkButton(self.userResultsFrame, text="Add Favorite", font=("Arial", 15), command=lambda:self.selectUser(0)))
                self.buttons[0].grid(row=1, column=6, padx=10, pady=10)

                self.userResultsFrame.pack(padx=10, pady=10)

                results3 = Review.getUserReviews(self.results[0].getID())
                print(results3)

                self.reviewsFrame.columnconfigure(3, weight=1)

                reviewerNameText = ctk.CTkLabel(self.reviewsFrame, text="Reviewer First Name", font=("Arial", 25))
                scoreText = ctk.CTkLabel(self.reviewsFrame, text="Score", font=("Arial", 25))
                reviewCommentText = ctk.CTkLabel(self.reviewsFrame, text="Review Comment", font=("Arial", 25))

                reviewerNameText.grid(row=0, column=0, padx=10, pady=10)
                scoreText.grid(row=0, column=1, padx=10, pady=10)
                reviewCommentText.grid(row=0, column=2, padx=10, pady=10)

                i = 1
                for result in results3:
                    ctk.CTkLabel(self.reviewsFrame, text=User.searchUserProfileByID(result.getReviewerID())[0].getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                    ctk.CTkLabel(self.reviewsFrame, text=result.getScore(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                    ctk.CTkLabel(self.reviewsFrame, text=result.getReviewText(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                    i += 1

                self.reviewsFrame.pack(padx=10, pady=10)
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
                    self.buttons.append(ctk.CTkButton(self.requestResultsFrame, text="List Requesters", font=("Arial", 15), command=lambda i=i:self.selectRequest(i-1)))
                    self.buttons[i-1].grid(row=i, column=5, padx=10, pady=10)
                    i+=1

                self.requestResultsFrame.pack(padx=10, pady=10)
            case _:
                self.results = []

    def selectOffer(self, selection):
        bookResultsSelection = self.results[selection].getBook().getID()
        results2 = User.findUsersOfferingBook(bookResultsSelection)

        self.bookOfferersFrame.columnconfigure(7, weight=1)

        firstNameText = ctk.CTkLabel(self.bookOfferersFrame, text="First Name", font=("Arial", 25))
        lastNameText = ctk.CTkLabel(self.bookOfferersFrame, text="Last Name", font=("Arial", 25))
        emailText = ctk.CTkLabel(self.bookOfferersFrame, text="Email", font=("Arial", 25))
        cityText = ctk.CTkLabel(self.bookOfferersFrame, text="City", font=("Arial", 25))
        deliveryTypeText = ctk.CTkLabel(self.bookOfferersFrame, text="Delivery Type", font=("Arial", 25))
        pricePerDayText = ctk.CTkLabel(self.bookOfferersFrame, text="Price Per Day", font=("Arial", 25))
        listActionText = ctk.CTkLabel(self.bookOfferersFrame, text="Action", font=("Arial", 25))

        firstNameText.grid(row=0, column=0, padx=10, pady=10)
        lastNameText.grid(row=0, column=1, padx=10, pady=10)
        emailText.grid(row=0, column=2, padx=10, pady=10)
        cityText.grid(row=0, column=3, padx=10, pady=10)
        deliveryTypeText.grid(row=0, column=4, padx=10, pady=10)
        pricePerDayText.grid(row=0, column=5, padx=10, pady=10)
        listActionText.grid(row=0, column=6, padx=10, pady=10)

        buttons2 = []

        i = 1
        for result in results2:
            ctk.CTkLabel(self.bookOfferersFrame, text=result.getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.bookOfferersFrame, text=result.getLastName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.bookOfferersFrame, text=result.getEmail(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
            ctk.CTkLabel(self.bookOfferersFrame, text=result.getCity(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.bookOfferersFrame, text=result.getBookOffer(bookResultsSelection).getDeliveryType(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
            ctk.CTkLabel(self.bookOfferersFrame, text=result.getBookOffer(bookResultsSelection).getPricePerDay(), font=("Arial", 15)).grid(row=i, column=5, padx=10, pady=10)
            buttons2.append(ctk.CTkButton(self.bookOfferersFrame, text="Accept Offer", font=("Arial", 15), command=
                                          lambda owner_id=result.getID(),listing_id=result.getBookOffer(bookResultsSelection).getID(),date=datetime.datetime.now():
                                          self.createTransaction(owner_id, listing_id, date)))
            buttons2[i-1].grid(row=i, column=6, padx=10, pady=10)
            i+=1

        self.bookOfferersFrame.pack(padx=10, pady=10)

    def selectUser(self, selection):
        userResultsSelection = self.results[selection].getID()
        User.searchUserProfile("Greg")[0].addFavorite(userResultsSelection)

    def selectRequest(self, selection):
        requestResultsSelection = self.results[selection].getBook().getID()
        results2 = User.findUsersRequestingBook(requestResultsSelection)

        self.bookRequestersFrame.columnconfigure(7, weight=1)

        firstNameText = ctk.CTkLabel(self.bookRequestersFrame, text="First Name", font=("Arial", 25))
        lastNameText = ctk.CTkLabel(self.bookRequestersFrame, text="Last Name", font=("Arial", 25))
        emailText = ctk.CTkLabel(self.bookRequestersFrame, text="Email", font=("Arial", 25))
        cityText = ctk.CTkLabel(self.bookRequestersFrame, text="City", font=("Arial", 25))
        deliveryTypeText = ctk.CTkLabel(self.bookRequestersFrame, text="Delivery Type", font=("Arial", 25))
        pricePerDayText = ctk.CTkLabel(self.bookRequestersFrame, text="Price Per Day", font=("Arial", 25))
        listActionText = ctk.CTkLabel(self.bookRequestersFrame, text="Action", font=("Arial", 25))

        firstNameText.grid(row=0, column=0, padx=10, pady=10)
        lastNameText.grid(row=0, column=1, padx=10, pady=10)
        emailText.grid(row=0, column=2, padx=10, pady=10)
        cityText.grid(row=0, column=3, padx=10, pady=10)
        deliveryTypeText.grid(row=0, column=4, padx=10, pady=10)
        pricePerDayText.grid(row=0, column=5, padx=10, pady=10)
        listActionText.grid(row=0, column=6, padx=10, pady=10)

        buttons2 = []

        i = 1
        for result in results2:
            ctk.CTkLabel(self.bookRequestersFrame, text=result.getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.bookRequestersFrame, text=result.getLastName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.bookRequestersFrame, text=result.getEmail(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
            ctk.CTkLabel(self.bookRequestersFrame, text=result.getCity(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.bookRequestersFrame, text=result.getBookRequest(requestResultsSelection).getDeliveryType(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
            ctk.CTkLabel(self.bookRequestersFrame, text=result.getBookRequest(requestResultsSelection).getPricePerDay(), font=("Arial", 15)).grid(row=i, column=5, padx=10, pady=10)
            buttons2.append(ctk.CTkButton(self.bookRequestersFrame, text="Accept Offer", font=("Arial", 15), command=
                                          lambda owner_id=result.getID(),listing_id=result.getBookOffer(requestResultsSelection).getID(),date=datetime.datetime.now():
                                          self.createTransaction(owner_id, listing_id, date)))
            buttons2[i-1].grid(row=i, column=6, padx=10, pady=10)
            i+=1

        self.bookRequestersFrame.pack(padx=10, pady=10)

    def createTransaction(self, owner_id, listing_id, startingDate):
        Transaction(User.searchUserProfile("Greg")[0].getID(), owner_id, listing_id, startingDate)
