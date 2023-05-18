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

class DashboardPage(ctk.CTkFrame):
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

        self.rentToOwnerText.grid(row=0, column=0, padx=10, pady=10)
        self.rentToScoreText.grid(row=0, column=1, padx=10, pady=10)
        self.rentToBookText.grid(row=0, column=2, padx=10, pady=10)
        self.rentToStatusText.grid(row=0, column=3, padx=10, pady=10)
        self.rentToDateText.grid(row=0, column=4, padx=10, pady=10)
        self.rentToAmountText.grid(row=0, column=5, padx=10, pady=10)
        self.rentToToggleText.grid(row=0, column=6, padx=10, pady=10)

        self.rentToGrid.pack()
