import customtkinter as ctk
import globals
from bookOffer import BookOffer
from listing import DeliveryType
import datetime

class MyBookOffersPage(ctk.CTkFrame):

    def getBookOfferData(self):
        bookData = []
        bookData.append(ctk.CTkEntry(self,placeholder_text="Book Name"))
        bookData[0].pack()
        return bookData

    def __init__(self, parent, controller):
        self.currentUser = globals.currentUser
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="My Book Offers", font=("Arial", 25), text_color="#3A7ABF")
        label.pack(padx=10, pady=10)
        self.BookOfferButtons = []
        self.AddButton=(ctk.CTkButton(self,text="Add Book Offer", command= lambda : self.addFunc()))
        self.AddButton.pack(padx=10, pady=10)

        self.__BookOffersListFrame = ctk.CTkFrame(self)
        userBookOffers = self.currentUser.getBookOffers()

        self.__EditFrame= ctk.CTkFrame(self)

        titleText = ctk.CTkLabel(self.__BookOffersListFrame, text="Title", font=("Arial", 25))
        authorText = ctk.CTkLabel(self.__BookOffersListFrame, text="Author", font=("Arial", 25))
        genreText = ctk.CTkLabel(self.__BookOffersListFrame, text="Genre", font=("Arial", 25))
        editionText = ctk.CTkLabel(self.__BookOffersListFrame, text="Edition", font=("Arial", 25))
        publisherText = ctk.CTkLabel(self.__BookOffersListFrame, text="Publisher", font=("Arial", 25))
        priceText = ctk.CTkLabel(self.__BookOffersListFrame, text="Price", font=("Arial", 25))
        deliveryText = ctk.CTkLabel(self.__BookOffersListFrame, text="Delivery type", font=("Arial", 25))
        editText = ctk.CTkLabel(self.__BookOffersListFrame, text="Edit", font=("Arial", 25))
        deleteText = ctk.CTkLabel(self.__BookOffersListFrame, text="Delete", font=("Arial", 25))


        titleText.grid(row=0, column=0, padx=10, pady=10)
        authorText.grid(row=0, column=1, padx=10, pady=10)
        genreText.grid(row=0, column=2, padx=10, pady=10)
        editionText.grid(row=0, column=3, padx=10, pady=10)
        publisherText.grid(row=0, column=4, padx=10, pady=10)
        priceText.grid(row=0, column=5, padx=10, pady=10)
        deliveryText.grid(row=0, column=6, padx=10, pady=10)
        editText.grid(row=0, column=7, padx=10, pady=10)
        deleteText.grid(row=0, column=8, padx=10, pady=10)


        i=1
        for offer in userBookOffers:
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getBook().getName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getBook().getAuthor(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getBook().getGenre(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getBook().getEdition(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getBook().getPublisher(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getPricePerDay(), font=("Arial", 15)).grid(row=i,column=5,padx=10,pady=10)
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getDeliveryType(), font=("Arial", 15)).grid(row=i,column=6,padx=10,pady=10)
            self.BookOfferButtons.append(ctk.CTkButton(self.__BookOffersListFrame, text="Edit Book Offer",command=
                                                       lambda offer=i-1:self.editFunc(offer)))
            self.BookOfferButtons.append(ctk.CTkButton(self.__BookOffersListFrame, text="Delete Book Offer",command=
                                    lambda offer=i-1:self.deleteFunc(offer)))
            self.BookOfferButtons[(i-1)*2].grid(row=i, column=7, padx=10, pady=10)
            self.BookOfferButtons[(i - 1) * 2+1].grid(row=i, column=8, padx=10, pady=10)
            i+=1
        self.__BookOffersListFrame.pack()
    def deleteFunc (self,offer):
        #print(globals.currentUser.getBookOffers())
        #print(BookOffer.all)
        del globals.currentUser.getBookOffers()[offer]
        #print("-----------------------------------------")
        #print(BookOffer.all)
        #print(globals.currentUser.getBookOffers())

    def editFunc(self,offer):
        self.radiobutton_variable = ctk.IntVar()
        self.priceChangeText=ctk.CTkLabel(self.__EditFrame, text="Enter price per day if you want to change it", font=("Arial", 25), text_color="#3A7ABF")
        self.priceChange = ctk.CTkEntry(self.__EditFrame,placeholder_text="Price")
        self.priceChangeText.pack()
        self.priceChange.pack()
        self.deliveryTypeText = ctk.CTkLabel(self.__EditFrame, text="Select delivery type",font=("Arial", 25), text_color="#3A7ABF")
        self.deliveryTypeLocalMeet = ctk.CTkRadioButton(self.__EditFrame, text="Local Meet", variable=self.radiobutton_variable, value=1)
        self.deliveryTypePost = ctk.CTkRadioButton(self.__EditFrame, text="Postal delivery",variable=self.radiobutton_variable, value=2)
        self.deliveryTypeText.pack()
        self.deliveryTypeLocalMeet.pack()
        self.deliveryTypePost.pack()
        self.applyButton = ctk.CTkButton(self.__EditFrame,text="Apply",command=
                                                lambda offer = offer,: self.apply(offer))


        self.applyButton.pack()
        self.__EditFrame.pack()
    def apply(self,offer):
        price=self.priceChange.get()
        delivery=self.radiobutton_variable.get()

        if price != "":
            globals.currentUser.getBookOffers()[offer].setPricePerDay(float(price))
        if delivery == 1:
            globals.currentUser.getBookOffers()[offer].setDeliveryType(DeliveryType.Local_Meeting)
        elif delivery == 2:
            globals.currentUser.getBookOffers()[offer].setDeliveryType(DeliveryType.By_Post)

    def addFunc(self):
        self.__AddOfferFrame=ctk.CTkFrame(self)

        self.bookName = ctk.CTkEntry(self.__AddOfferFrame, placeholder_text="Book Name")
        self.bookName.pack()
        self.bookAuthor = ctk.CTkEntry(self.__AddOfferFrame, placeholder_text="Book Author")
        self.bookAuthor.pack()
        self.bookGenre = ctk.CTkEntry(self.__AddOfferFrame, placeholder_text="Genre")
        self.bookGenre.pack()
        self.bookEdition = ctk.CTkEntry(self.__AddOfferFrame, placeholder_text="Edition")
        self.bookEdition.pack()
        self.bookPublisher = ctk.CTkEntry(self.__AddOfferFrame, placeholder_text="Publisher")
        self.bookPublisher.pack()

        self.pricePerDay = ctk.CTkEntry(self.__AddOfferFrame, placeholder_text="Price per Day")
        self.pricePerDay.pack()

        self.radiobutton = ctk.IntVar()
        self.deliveryTypeText = ctk.CTkLabel(self.__AddOfferFrame, text="Select delivery type", font=("Arial", 25),text_color="#3A7ABF")
        self.deliveryTypeLocalMeet = ctk.CTkRadioButton(self.__AddOfferFrame, text="Local Meet",variable=self.radiobutton, value=1)
        self.deliveryTypePost = ctk.CTkRadioButton(self.__AddOfferFrame, text="Postal delivery",variable=self.radiobutton, value=2)
        self.deliveryTypeText.pack()
        self.deliveryTypeLocalMeet.pack()
        self.deliveryTypePost.pack()

        self.applyButton = ctk.CTkButton(self.__AddOfferFrame,text="Apply",command=lambda : self.addOffer())
        self.applyButton.pack()
        self.__AddOfferFrame.pack()


    def addOffer(self):
        if self.bookName.get() == "" or self.bookAuthor.get() == "" or self.bookGenre.get() == "" or self.pricePerDay.get() == "" or self.radiobutton.get()== "":
            self.__incompletFormFrame = ctk.CTkFrame(self)
            incompletFormText= ctk.CTkLabel(self.__incompletFormFrame,text="There are mandatory fields in the form you have not field")
            incompletFormText.pack()
            self.__incompletFormFrame.pack()
            return
        delivery:DeliveryType
        if self.radiobutton.get() == 1:
            delivery=DeliveryType.Local_Meeting
        else:
            delivery=DeliveryType.By_Post
        globals.currentUser.addBookOffer(self.bookName.get(),
                                        self.bookAuthor.get(),
                                        self.bookGenre.get(),
                                        int(self.bookEdition.get()),
                                        self.bookPublisher.get(),
                                        float(self.pricePerDay.get()),
                                        delivery,
                                        datetime.datetime.now())
