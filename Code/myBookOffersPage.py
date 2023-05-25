import customtkinter as ctk
import globals
from bookOffer import BookOffer
from listing import DeliveryType


class MyBookOffersPage(ctk.CTkFrame):

    def getBookOfferData(self):
        bookData = []
        bookData.append(ctk.CTkEntry(self,placeholder_text="Book Name"))
        bookData[0].pack()
        return bookData

    def __init__(self, parent, controller):
        self.currentUser = globals.currentUser
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="My Book Offers")
        label.pack(padx=10, pady=10)
        self.BookOfferButtons = []
        self.AddButton=(ctk.CTkButton(self,text="Add Book Offer"))
        self.AddButton.pack(padx=10, pady=10)



        self.__BookOffersListFrame = ctk.CTkFrame(self)
        userBookOffers = self.currentUser.getBookOffers()

        self.__EditFrame= ctk.CTkFrame(self)

        bookText = ctk.CTkLabel(self.__BookOffersListFrame, text="Book", font=("Arial", 25))
        PriceText = ctk.CTkLabel(self.__BookOffersListFrame, text="Price", font=("Arial", 25))
        deliveryText = ctk.CTkLabel(self.__BookOffersListFrame, text="Delivery type", font=("Arial", 25))


        bookText.grid(row=0, column=0, padx=10, pady=10)
        PriceText.grid(row=0, column=1, padx=10, pady=10)
        deliveryText.grid(row=0, column=2, padx=10, pady=10)


        i=1
        for offer in userBookOffers:
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getBook().getName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getPricePerDay(), font=("Arial", 15)).grid(row=i,column=1,padx=10,pady=10)
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getDeliveryType(), font=("Arial", 15)).grid(row=i,column=2,padx=10,pady=10)
            self.BookOfferButtons.append(ctk.CTkButton(self.__BookOffersListFrame, text="Edit Book Offer",command=
                                                       lambda offer=i-1:self.editFunc(offer)))
            self.BookOfferButtons.append(ctk.CTkButton(self.__BookOffersListFrame, text="Delete Book Offer",command=
                                    lambda offer=i-1:self.deleteFunc(offer)))
            self.BookOfferButtons[(i-1)*2].grid(row=i, column=3, padx=10, pady=10)
            self.BookOfferButtons[(i - 1) * 2+1].grid(row=i, column=4, padx=10, pady=10)
            i+=1
        self.__BookOffersListFrame.pack()
    def deleteFunc (self,offer):
        #print(globals.currentUser.getBookOffers())
        print(BookOffer.all)
        del globals.currentUser.getBookOffers()[offer]
        print("-----------------------------------------")
        print(BookOffer.all)
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
            print("!!!!!!!!!!!1")
            globals.currentUser.getBookOffers()[offer].setDeliveryType(DeliveryType.By_Post)


