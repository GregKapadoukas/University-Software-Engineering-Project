import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from user import User
from transaction import Transaction
import globals
class TransactionHistoryPage(ctk.CTkFrame):
    
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.__graphsFrame = ctk.CTkFrame(self)
        self.__graphsFrame.columnconfigure(1,weight=1)
        self.__transactionListFrame = ctk.CTkFrame(self)
        self.__transactionListFrame.columnconfigure(1, weight=1)
        label = ctk.CTkLabel(self, text="Transaction History")
        label.pack(padx=10, pady=10)
        
        fig , ax = plt.subplots()
        transactionsList = Transaction.getClosedTransactions(globals.currentUser)
        transactionsGenreStats = Transaction.getClosedTransactionsDataGenre(transactionsList)
        transactionRenterAgeStats = Transaction. getClosedTransactionsDataRenterAge(transactionsList)

        print(list(transactionRenterAgeStats.keys()))
        print(list(transactionRenterAgeStats.values()))

        genreStats=plt.pie(list(transactionsGenreStats.values()), labels=list(transactionsGenreStats.keys()))
        genreStats = FigureCanvasTkAgg(fig, master=self.__graphsFrame)
        genreStats.draw()
        genreStats.get_tk_widget().grid(row=0, column=0)
        fig , ax = plt.subplots()
        ageStats=plt.pie(list(transactionRenterAgeStats.values()), labels=list(transactionRenterAgeStats.keys()))
        ageStats = FigureCanvasTkAgg(fig, master=self.__graphsFrame)
        ageStats.draw()
        ageStats.get_tk_widget().grid(row=0, column=1)
        self.__graphsFrame.pack()

        statusText = ctk.CTkLabel(self.__transactionListFrame, text="status", font=("Arial", 25))
        renterText = ctk.CTkLabel(self.__transactionListFrame, text="renter name", font=("Arial", 25))
        ownerText = ctk.CTkLabel(self.__transactionListFrame, text="owner name", font=("Arial", 25))
        bookText = ctk.CTkLabel(self.__transactionListFrame, text="Book", font=("Arial", 25))
        dateText = ctk.CTkLabel(self.__transactionListFrame, text="Date", font=("Arial", 25))

        statusText.grid(row=0, column=0, padx=10, pady=10)
        renterText.grid(row=0, column=1, padx=10, pady=10)
        ownerText.grid(row=0, column=2, padx=10, pady=10)
        bookText.grid(row=0, column=3, padx=10, pady=10)
        dateText.grid(row=0, column=4, padx=10, pady=10)

        i=1

        for transaction in transactionsList:

            ctk.CTkLabel(self.__transactionListFrame, text=transaction.getStatus(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.__transactionListFrame, text=transaction.getRenter().getFirstName() + transaction.getRenter().getLastName(),font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.__transactionListFrame, text=transaction.getOwner().getFirstName() + transaction.getOwner().getLastName(), font=("Arial", 15)).grid(row=i,column=2,padx=10,pady=10)
            ctk.CTkLabel(self.__transactionListFrame, text=transaction.getBookName(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.__transactionListFrame, text=transaction.getDate(), font=("Arial", 15)).grid(row=i,column=4,padx=10,pady=10)
            i += 1

        self.__transactionListFrame.pack()


