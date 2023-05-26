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
from transaction import Transaction, Status
from user import User

class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.pageRentFromText = ctk.CTkLabel(self, text="Renting From Other Users", font=("Arial", 25), text_color="#3A7ABF")
        self.pageRentFromText.pack(padx=10, pady=10)

        self.rentFromGrid = ctk.CTkFrame(self)
        self.rentFromGrid.columnconfigure(6, weight=1)

        self.rentFromOwnerText = ctk.CTkLabel(self.rentFromGrid, text="Owner", font=("Arial", 25))
        self.rentFromBookText = ctk.CTkLabel(self.rentFromGrid, text="Book", font=("Arial", 25))
        self.rentFromStatusText = ctk.CTkLabel(self.rentFromGrid, text="Status", font=("Arial", 25))
        self.rentFromDateText = ctk.CTkLabel(self.rentFromGrid, text="Date", font=("Arial", 25))
        self.rentFromAmountText = ctk.CTkLabel(self.rentFromGrid, text="Total Amount", font=("Arial", 25))

        self.rentFromOwnerText.grid(row=0, column=0, padx=10, pady=10)
        self.rentFromBookText.grid(row=0, column=1, padx=10, pady=10)
        self.rentFromStatusText.grid(row=0, column=2, padx=10, pady=10)
        self.rentFromDateText.grid(row=0, column=3, padx=10, pady=10)
        self.rentFromAmountText.grid(row=0, column=4, padx=10, pady=10)

        self.rentingFromTransactions = Transaction.getByRenterID(0)

        self.rentFromButtons = []

        i = 1
        for transaction in self.rentingFromTransactions :
            if transaction.getStatus == Status.Denied or transaction.getStatus == Status.Finished:
                pass
            elif transaction.getStatus() == Status.Waiting_To_Be_Delivered or transaction.getStatus() == Status.Marked_Delivered_By_One:
                ctk.CTkLabel(self.rentFromGrid, text=User.searchUserProfileByID(transaction.getOwnerID())[0].getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                ctk.CTkLabel(self.rentFromGrid, text=transaction.getBookName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                ctk.CTkLabel(self.rentFromGrid, text=transaction.getStatus(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                ctk.CTkLabel(self.rentFromGrid, text=transaction.getStartingDate(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                ctk.CTkLabel(self.rentFromGrid, text=transaction.getAmountAndCheckEnough(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                self.rentFromButtons.append(ctk.CTkButton(self.rentFromGrid, text="Mark Delivered", font=("Arial", 15), command=
                                            lambda transaction = transaction:transaction.updateStatus()))
                self.rentFromButtons[i-1].grid(row=i, column=5, padx=10, pady=10)
            elif transaction.getStatus() == Status.Marked_Delivered or transaction.getStatus == Status.Marked_Returned_By_One:
                ctk.CTkLabel(self.rentFromGrid, text=User.searchUserProfileByID(transaction.getOwnerID())[0].getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                ctk.CTkLabel(self.rentFromGrid, text=transaction.getBookName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                ctk.CTkLabel(self.rentFromGrid, text=transaction.getStatus(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                ctk.CTkLabel(self.rentFromGrid, text=transaction.getStartingDate(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                ctk.CTkLabel(self.rentFromGrid, text=transaction.getAmountAndCheckEnough(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                self.rentFromButtons.append(ctk.CTkButton(self.rentFromGrid, text="Mark Returned", font=("Arial", 15), command=
                                            lambda transaction = transaction:transaction.updateStatus()))
                self.rentFromButtons[i-1].grid(row=i, column=5, padx=10, pady=10)
            i+=1
        
        self.rentFromGrid.pack()

        self.pageRentToText = ctk.CTkLabel(self, text="Renting To Other Users", font=("Arial", 25), text_color="#3A7ABF")
        self.pageRentToText.pack(padx=10, pady=10)

        self.rentToGrid = ctk.CTkFrame(self)
        self.rentToGrid.columnconfigure(7, weight=1)

        self.rentToRenterText = ctk.CTkLabel(self.rentToGrid, text="Renter", font=("Arial", 25))
        self.rentToBookText = ctk.CTkLabel(self.rentToGrid, text="Book", font=("Arial", 25))
        self.rentToStatusText = ctk.CTkLabel(self.rentToGrid, text="Status", font=("Arial", 25))
        self.rentToDateText = ctk.CTkLabel(self.rentToGrid, text="Date", font=("Arial", 25))
        self.rentToAmountText = ctk.CTkLabel(self.rentToGrid, text="Total Amount", font=("Arial", 25))

        self.rentToRenterText.grid(row=0, column=0, padx=10, pady=10)
        self.rentToBookText.grid(row=0, column=1, padx=10, pady=10)
        self.rentToStatusText.grid(row=0, column=2, padx=10, pady=10)
        self.rentToDateText.grid(row=0, column=3, padx=10, pady=10)
        self.rentToAmountText.grid(row=0, column=4, padx=10, pady=10)

        self.rentingToTransactions = Transaction.getByOwnerID(0)

        self.rentToButtons = []
        self.extraButtons = []

        i = 1
        j = 0
        for transaction in self.rentingToTransactions:
            if transaction.getStatus == Status.Denied or transaction.getStatus == Status.Finished:
                pass
            elif transaction.getStatus() == Status.Waiting_To_Be_Delivered or transaction.getStatus() == Status.Marked_Delivered_By_One:
                ctk.CTkLabel(self.rentToGrid, text=User.searchUserProfileByID(transaction.getRenterID())[0].getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                ctk.CTkLabel(self.rentToGrid, text=transaction.getBookName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                ctk.CTkLabel(self.rentToGrid, text=transaction.getStatus(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                ctk.CTkLabel(self.rentToGrid, text=transaction.getStartingDate(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                ctk.CTkLabel(self.rentToGrid, text=transaction.getAmountAndCheckEnough(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                self.rentToButtons.append(ctk.CTkButton(self.rentToGrid, text="Mark Delivered", font=("Arial", 15), command=
                                        lambda transaction = transaction:transaction.updateStatus()))
                self.rentToButtons[i-1].grid(row=i, column=5, padx=10, pady=10)
            elif transaction.getStatus() == Status.Marked_Delivered or transaction.getStatus == Status.Marked_Returned_By_One:
                ctk.CTkLabel(self.rentToGrid, text=User.searchUserProfileByID(transaction.getRenterID())[0].getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
                ctk.CTkLabel(self.rentToGrid, text=transaction.getBookName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
                ctk.CTkLabel(self.rentToGrid, text=transaction.getStatus(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
                ctk.CTkLabel(self.rentToGrid, text=transaction.getStartingDate(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
                ctk.CTkLabel(self.rentToGrid, text=transaction.getAmountAndCheckEnough(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
                self.rentToButtons.append(ctk.CTkButton(self.rentToGrid, text="Mark Returned", font=("Arial", 15), command=
                                         lambda transaction = transaction:transaction.updateStatus()))
                self.rentToButtons[i-1].grid(row=i, column=5, padx=10, pady=10)
            i+=1

        self.rentToGrid.pack()

    def clearFrames(self):
        for widget in self.rentFromGrid.winfo_children():
            widget.destroy()
        for widget in self.rentToGrid.winfo_children():
            widget.destroy()
