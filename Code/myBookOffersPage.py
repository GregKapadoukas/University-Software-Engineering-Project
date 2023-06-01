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
        ctk.CTkFrame.__init__(self, parent)
        self.__pageText = ctk.CTkLabel(self, text="My Book Offers", font=("Arial", 25), text_color="#3A7ABF")
        self.__pageText.pack(padx=10, pady=10)
        self.__bookOfferButtons = []
        self.__addButton=(ctk.CTkButton(self,text="Add Book Offer", command= lambda : self.addFunc()))
        self.__addButton.pack(padx=10, pady=10)

        self.__bookOffersListFrame = ctk.CTkFrame(self)
        self.__userBookOffers = globals.currentUser.getBookOffers()

        self.__editFrame= ctk.CTkFrame(self)

        self.__titleText = ctk.CTkLabel(self.__bookOffersListFrame, text="Title", font=("Arial", 25))
        self.__authorText = ctk.CTkLabel(self.__bookOffersListFrame, text="Author", font=("Arial", 25))
        self.__genreText = ctk.CTkLabel(self.__bookOffersListFrame, text="Genre", font=("Arial", 25))
        self.__editionText = ctk.CTkLabel(self.__bookOffersListFrame, text="Edition", font=("Arial", 25))
        self.__publisherText = ctk.CTkLabel(self.__bookOffersListFrame, text="Publisher", font=("Arial", 25))
        self.__priceText = ctk.CTkLabel(self.__bookOffersListFrame, text="Price", font=("Arial", 25))
        self.__deliveryText = ctk.CTkLabel(self.__bookOffersListFrame, text="Delivery type", font=("Arial", 25))
        self.__editText = ctk.CTkLabel(self.__bookOffersListFrame, text="Edit", font=("Arial", 25))
        self.__deleteText = ctk.CTkLabel(self.__bookOffersListFrame, text="Delete", font=("Arial", 25))


        self.__titleText.grid(row=0, column=0, padx=10, pady=10)
        self.__authorText.grid(row=0, column=1, padx=10, pady=10)
        self.__genreText.grid(row=0, column=2, padx=10, pady=10)
        self.__editionText.grid(row=0, column=3, padx=10, pady=10)
        self.__publisherText.grid(row=0, column=4, padx=10, pady=10)
        self.__priceText.grid(row=0, column=5, padx=10, pady=10)
        self.__deliveryText.grid(row=0, column=6, padx=10, pady=10)
        self.__editText.grid(row=0, column=7, padx=10, pady=10)
        self.__deleteText.grid(row=0, column=8, padx=10, pady=10)


        i=1
        for offer in self.__userBookOffers:
            ctk.CTkLabel(self.__bookOffersListFrame, text=offer.getBook().getName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.__bookOffersListFrame, text=offer.getBook().getAuthor(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.__bookOffersListFrame, text=offer.getBook().getGenre(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
            ctk.CTkLabel(self.__bookOffersListFrame, text=offer.getBook().getEdition(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.__bookOffersListFrame, text=offer.getBook().getPublisher(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
            ctk.CTkLabel(self.__bookOffersListFrame, text=offer.getPricePerDay(), font=("Arial", 15)).grid(row=i,column=5,padx=10,pady=10)
            ctk.CTkLabel(self.__bookOffersListFrame, text=offer.getDeliveryType(), font=("Arial", 15)).grid(row=i,column=6,padx=10,pady=10)
            self.__bookOfferButtons.append(ctk.CTkButton(self.__bookOffersListFrame, text="Edit Book Offer",command=
                                                       lambda offer=i-1:self.editFunc(offer)))
            self.__bookOfferButtons.append(ctk.CTkButton(self.__bookOffersListFrame, text="Delete Book Offer",command=
                                    lambda offer=i-1:self.deleteFunc(offer)))
            self.__bookOfferButtons[(i-1)*2].grid(row=i, column=7, padx=10, pady=10)
            self.__bookOfferButtons[(i - 1) * 2+1].grid(row=i, column=8, padx=10, pady=10)
            i+=1
        self.__bookOffersListFrame.pack()
    def deleteFunc (self,offer):
        #print(globals.currentUser.getBookOffers())
        #print(BookOffer.all)
        del globals.currentUser.getBookOffers()[offer]
        #print("-----------------------------------------")
        #print(BookOffer.all)
        #print(globals.currentUser.getBookOffers())

    def editFunc(self,offer):
        self.__radiobutton_variable = ctk.IntVar()
        self.__priceChangeText=ctk.CTkLabel(self.__editFrame, text="Enter price per day if you want to change it", font=("Arial", 25), text_color="#3A7ABF")
        self.__priceChange = ctk.CTkEntry(self.__editFrame,placeholder_text="Price")
        self.__priceChangeText.pack()
        self.__priceChange.pack()
        self.__deliveryTypeText = ctk.CTkLabel(self.__editFrame, text="Select delivery type",font=("Arial", 25), text_color="#3A7ABF")
        self.__deliveryTypeLocalMeet = ctk.CTkRadioButton(self.__editFrame, text="Local Meeting", variable=self.__radiobutton_variable, value=1)
        self.__deliveryTypePost = ctk.CTkRadioButton(self.__editFrame, text="By Post",variable=self.__radiobutton_variable, value=2)
        self.__deliveryTypeText.pack()
        self.__deliveryTypeLocalMeet.pack()
        self.__deliveryTypePost.pack()
        self.__applyButton = ctk.CTkButton(self.__editFrame,text="Apply",command=
                                                lambda offer = offer,: self.apply(offer))


        self.__applyButton.pack()
        self.__editFrame.pack()
    def apply(self,offer):
        price=self.__priceChange.get()
        delivery=self.__radiobutton_variable.get()

        if price != "":
            globals.currentUser.getBookOffers()[offer].setPricePerDay(float(price))
        if delivery == 1:
            globals.currentUser.getBookOffers()[offer].setDeliveryType(DeliveryType.Local_Meeting)
        elif delivery == 2:
            globals.currentUser.getBookOffers()[offer].setDeliveryType(DeliveryType.By_Post)

    def addFunc(self):
        self.__addOfferFrame=ctk.CTkFrame(self)

        self.__bookName = ctk.CTkEntry(self.__addOfferFrame, placeholder_text="Book Name")
        self.__bookName.pack()
        self.__bookAuthor = ctk.CTkEntry(self.__addOfferFrame, placeholder_text="Book Author")
        self.__bookAuthor.pack()
        self.__bookGenre = ctk.CTkEntry(self.__addOfferFrame, placeholder_text="Genre")
        self.__bookGenre.pack()
        self.__bookEdition = ctk.CTkEntry(self.__addOfferFrame, placeholder_text="Edition")
        self.__bookEdition.pack()
        self.__bookPublisher = ctk.CTkEntry(self.__addOfferFrame, placeholder_text="Publisher")
        self.__bookPublisher.pack()

        self.__pricePerDay = ctk.CTkEntry(self.__addOfferFrame, placeholder_text="Price per Day")
        self.__pricePerDay.pack()

        self.__radiobutton = ctk.IntVar()
        self.__deliveryTypeText = ctk.CTkLabel(self.__addOfferFrame, text="Select delivery type", font=("Arial", 25),text_color="#3A7ABF")
        self.__deliveryTypeLocalMeet = ctk.CTkRadioButton(self.__addOfferFrame, text="Local Meet",variable=self.__radiobutton, value=1)
        self.__deliveryTypePost = ctk.CTkRadioButton(self.__addOfferFrame, text="Postal delivery",variable=self.__radiobutton, value=2)
        self.__deliveryTypeText.pack()
        self.__deliveryTypeLocalMeet.pack()
        self.__deliveryTypePost.pack()

        self.__applyButton = ctk.CTkButton(self.__addOfferFrame,text="Apply",command=lambda : self.addOffer())
        self.__applyButton.pack()
        self.__addOfferFrame.pack()


    def addOffer(self):
        if self.__bookName.get() == "" or self.__bookAuthor.get() == "" or self.__bookGenre.get() == "" or self.__pricePerDay.get() == "" or self.__radiobutton.get()== "":
            self.__incompleteFormFrame = ctk.CTkFrame(self)
            self.__incompleteFormText= ctk.CTkLabel(self.__incompleteFormFrame,text="There are mandatory fields in the form you have not field")
            self.__incompleteFormText.pack()
            self.__incompleteFormFrame.pack()
            return
        delivery:DeliveryType
        if self.__radiobutton.get() == 1:
            delivery=DeliveryType.Local_Meeting
        else:
            delivery=DeliveryType.By_Post
        globals.currentUser.addBookOffer(self.__bookName.get(),
                                        self.__bookAuthor.get(),
                                        self.__bookGenre.get(),
                                        int(self.__bookEdition.get()),
                                        self.__bookPublisher.get(),
                                        float(self.__pricePerDay.get()),
                                        delivery,
                                        datetime.datetime.now())
