import customtkinter as ctk
import globals


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
        BookOfferButtons = []
        BookOfferButtons.append(ctk.CTkButton(self,text="Add Book Offer",command=self.getBookOfferData))
        BookOfferButtons.append(ctk.CTkButton(self,text="Delete Book Offer"))
        BookOfferButtons.append(ctk.CTkButton(self,text="Select Book Offer"))
        for button in BookOfferButtons:
            button.pack()

        self.__BookOffersListFrame = ctk.CTkFrame(self)
        userBookOffers = self.currentUser.getBookOffers()

        bookText = ctk.CTkLabel(self.__BookOffersListFrame, text="Book", font=("Arial", 25))
        PriceText = ctk.CTkLabel(self.__BookOffersListFrame, text="Price", font=("Arial", 25))
        deliveryText = ctk.CTkLabel(self.__BookOffersListFrame, text="Delivery type", font=("Arial", 25))


        bookText.grid(row=0, column=0, padx=10, pady=10)
        PriceText.grid(row=0, column=1, padx=10, pady=10)
        deliveryText.grid(row=0, column=2, padx=10, pady=10)


        i=1
        for offer in userBookOffers:
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getBook().getName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getPricePerDay(), font=("Arial", 15)).grid(row=i,column=2,padx=10,pady=10)
            ctk.CTkLabel(self.__BookOffersListFrame, text=offer.getDeliveryType, font=("Arial", 15)).grid(row=i,column=3,padx=10,pady=10)
            i+=1
        self.__BookOffersListFrame.pack()