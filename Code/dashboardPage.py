import customtkinter as ctk
import datetime
from book import Book
from bookOffer import BookOffer
from bookRequest import BookRequest
from favorite import Favorite
from listing import Listing, DeliveryType
from notification import Notification
from review import Review
from transaction import Transaction, Status
from user import User
import globals

class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.__pageText = ctk.CTkLabel(self, text="Dashboard", font=("Arial", 25), text_color="#3A7ABF")
        self.__pageText.pack(padx=20, pady=20)

        self.__pageRentFromText = ctk.CTkLabel(self, text="Renting From Other Users", font=("Arial", 25), text_color="#3A7ABF")
        self.__pageRentFromText.pack(padx=10, pady=10)

        self.__rentFromGrid = ctk.CTkFrame(self)
        self.__rentFromGrid.columnconfigure(6, weight=1)

        self.__rentFromOwnerText = ctk.CTkLabel(self.__rentFromGrid, text="Owner", font=("Arial", 25))
        self.__rentFromBookText = ctk.CTkLabel(self.__rentFromGrid, text="Book", font=("Arial", 25))
        self.__rentFromStatusText = ctk.CTkLabel(self.__rentFromGrid, text="Status", font=("Arial", 25))
        self.__rentFromDateText = ctk.CTkLabel(self.__rentFromGrid, text="Date", font=("Arial", 25))
        self.__rentFromAmountText = ctk.CTkLabel(self.__rentFromGrid, text="Total Amount", font=("Arial", 25))

        self.__rentFromOwnerText.grid(row=0, column=0, padx=10, pady=10)
        self.__rentFromBookText.grid(row=0, column=1, padx=10, pady=10)
        self.__rentFromStatusText.grid(row=0, column=2, padx=10, pady=10)
        self.__rentFromDateText.grid(row=0, column=3, padx=10, pady=10)
        self.__rentFromAmountText.grid(row=0, column=4, padx=10, pady=10)

        self.__rentingFromTransactions = Transaction.getByRenter(globals.currentUser)

        self.__rentFromButtons = []

        i = 1
        for transaction in self.__rentingFromTransactions :
            if transaction.getStatus == Status.Denied or transaction.getStatus == Status.Finished:
                pass
            elif transaction.getStatus() == Status.Waiting_To_Be_Delivered or transaction.getStatus() == Status.Marked_Delivered_By_One:
                ctk.CTkLabel(self.__rentFromGrid, text=transaction.getOwner().getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                ctk.CTkLabel(self.__rentFromGrid, text=transaction.getBookName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                ctk.CTkLabel(self.__rentFromGrid, text=transaction.getStatus(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                ctk.CTkLabel(self.__rentFromGrid, text=transaction.getStartingDate(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                ctk.CTkLabel(self.__rentFromGrid, text=transaction.getAmountAndCheckEnough(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                self.__rentFromButtons.append(ctk.CTkButton(self.__rentFromGrid, text="Mark Delivered", font=("Arial", 15), command=
                                            lambda transaction = transaction:transaction.updateStatus()))
                self.__rentFromButtons[i-1].grid(row=i, column=5, padx=10, pady=10)
                i+=1
            elif transaction.getStatus() == Status.Marked_Delivered or transaction.getStatus == Status.Marked_Returned_By_One:
                ctk.CTkLabel(self.__rentFromGrid, text=transaction.getOwner().getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                ctk.CTkLabel(self.__rentFromGrid, text=transaction.getBookName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                ctk.CTkLabel(self.__rentFromGrid, text=transaction.getStatus(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                ctk.CTkLabel(self.__rentFromGrid, text=transaction.getStartingDate(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                ctk.CTkLabel(self.__rentFromGrid, text=transaction.getAmountAndCheckEnough(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                self.__rentFromButtons.append(ctk.CTkButton(self.__rentFromGrid, text="Mark Returned", font=("Arial", 15), command=
                                            lambda transaction = transaction:transaction.updateStatus()))
                self.__rentFromButtons[i-1].grid(row=i, column=5, padx=10, pady=10)
                i+=1
        
        self.__rentFromGrid.pack()

        self.__pageRentToText = ctk.CTkLabel(self, text="Renting To Other Users", font=("Arial", 25), text_color="#3A7ABF")
        self.__pageRentToText.pack(padx=10, pady=10)

        self.__rentToGrid = ctk.CTkFrame(self)
        self.__rentToGrid.columnconfigure(7, weight=1)

        self.__rentToRenterText = ctk.CTkLabel(self.__rentToGrid, text="Renter", font=("Arial", 25))
        self.__rentToBookText = ctk.CTkLabel(self.__rentToGrid, text="Book", font=("Arial", 25))
        self.__rentToStatusText = ctk.CTkLabel(self.__rentToGrid, text="Status", font=("Arial", 25))
        self.__rentToDateText = ctk.CTkLabel(self.__rentToGrid, text="Date", font=("Arial", 25))
        self.__rentToAmountText = ctk.CTkLabel(self.__rentToGrid, text="Total Amount", font=("Arial", 25))

        self.__rentToRenterText.grid(row=0, column=0, padx=10, pady=10)
        self.__rentToBookText.grid(row=0, column=1, padx=10, pady=10)
        self.__rentToStatusText.grid(row=0, column=2, padx=10, pady=10)
        self.__rentToDateText.grid(row=0, column=3, padx=10, pady=10)
        self.__rentToAmountText.grid(row=0, column=4, padx=10, pady=10)

        self.__rentingToTransactions = Transaction.getByOwner(globals.currentUser)

        self.__rentToButtons = []
        self.__extraButtons = []

        i = 1
        for transaction in self.__rentingToTransactions:
            if transaction.getStatus == Status.Denied or transaction.getStatus == Status.Finished:
                pass
            elif transaction.getStatus() == Status.Waiting_To_Be_Delivered or transaction.getStatus() == Status.Marked_Delivered_By_One:
                ctk.CTkLabel(self.__rentToGrid, text=transaction.getRenter().getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                ctk.CTkLabel(self.__rentToGrid, text=transaction.getBookName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                ctk.CTkLabel(self.__rentToGrid, text=transaction.getStatus(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                ctk.CTkLabel(self.__rentToGrid, text=transaction.getStartingDate(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                ctk.CTkLabel(self.__rentToGrid, text=transaction.getAmountAndCheckEnough(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                self.__rentToButtons.append(ctk.CTkButton(self.__rentToGrid, text="Mark Delivered", font=("Arial", 15), command=
                                        lambda transaction = transaction:transaction.updateStatus()))
                self.__rentToButtons[i-1].grid(row=i, column=5, padx=10, pady=10)
                i+=1
            elif transaction.getStatus() == Status.Marked_Delivered or transaction.getStatus == Status.Marked_Returned_By_One:
                ctk.CTkLabel(self.__rentToGrid, text=transaction.getRenter().getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                ctk.CTkLabel(self.__rentToGrid, text=transaction.getBookName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                ctk.CTkLabel(self.__rentToGrid, text=transaction.getStatus(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                ctk.CTkLabel(self.__rentToGrid, text=transaction.getStartingDate(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                ctk.CTkLabel(self.__rentToGrid, text=transaction.getAmountAndCheckEnough(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                self.__rentToButtons.append(ctk.CTkButton(self.__rentToGrid, text="Mark Returned", font=("Arial", 15), command=
                                         lambda transaction = transaction:transaction.updateStatus()))
                self.__rentToButtons[i-1].grid(row=i, column=5, padx=10, pady=10)
                i+=1

        self.__rentToGrid.pack()

    def clearFrames(self):
        for widget in self.__rentFromGrid.winfo_children():
            widget.destroy()
        for widget in self.__rentToGrid.winfo_children():
            widget.destroy()
