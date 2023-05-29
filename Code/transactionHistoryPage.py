import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from user import User
from transaction import Transaction
import globals
from reviewPage import ReviewPage

class TransactionHistoryPage(ctk.CTkFrame):
    
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.__graphsFrame = ctk.CTkFrame(self)
        self.__graphsFrame.columnconfigure(1,weight=1)
        self.__transactionListFrame = ctk.CTkFrame(self)
        self.__transactionListFrame.columnconfigure(1, weight=1)
        self.__pageText = ctk.CTkLabel(self, text="Transaction History", font=("Arial", 25), text_color="#3A7ABF")
        self.__pageText.pack(padx=20, pady=20)
        
        self.__genreStatsFigure , ax = plt.subplots()
        self.__genreStatsFigure.set_size_inches(5,5)
        self.__transactionsList = Transaction.getClosedTransactions(globals.currentUser)
        self.__ownerTransactionsList = Transaction.getOwnerClosedTransactions(globals.currentUser)
        self.__transactionsGenreStats = Transaction.getClosedTransactionsDataGenre(self.__ownerTransactionsList)
        self.__transactionRenterAgeStats = Transaction. getClosedTransactionsDataRenterAge(self.__ownerTransactionsList)
        self.__genreStats=plt.pie(list(self.__transactionsGenreStats.values()), labels=list(self.__transactionsGenreStats.keys()))
        self.__genreStats = FigureCanvasTkAgg(self.__genreStatsFigure, master=self.__graphsFrame)
        #genreStatsFigure.set_facecolor("gray")
        self.__genreStats.draw()
        self.__genreStats.get_tk_widget().grid(row=0, column=0, padx=20, pady=20)

        self.__ageStatsFigure , ax = plt.subplots()
        self.__ageStatsFigure.set_size_inches(5,5)
        self.__ageStats=plt.pie(list(self.__transactionRenterAgeStats.values()), labels=list(self.__transactionRenterAgeStats.keys()))
        self.__ageStats = FigureCanvasTkAgg(self.__ageStatsFigure, master=self.__graphsFrame)
        #genreStatsFigure.set_facecolor("gray")
        self.__ageStats.draw()
        self.__ageStats.get_tk_widget().grid(row=0, column=1, padx=20, pady=20)
        self.__graphsFrame.pack(padx=20, pady=20)
        
        plt.close(self.__genreStatsFigure)
        plt.close(self.__ageStatsFigure)

        self.__statusText = ctk.CTkLabel(self.__transactionListFrame, text="status", font=("Arial", 25))
        self.__renterText = ctk.CTkLabel(self.__transactionListFrame, text="renter name", font=("Arial", 25))
        self.__ownerText = ctk.CTkLabel(self.__transactionListFrame, text="owner name", font=("Arial", 25))
        self.__bookText = ctk.CTkLabel(self.__transactionListFrame, text="Book", font=("Arial", 25))
        self.__dateText = ctk.CTkLabel(self.__transactionListFrame, text="Date", font=("Arial", 25))
        self.__reviewText = ctk.CTkLabel(self.__transactionListFrame, text="Review", font=("Arial", 25))

        self.__statusText.grid(row=0, column=0, padx=10, pady=10)
        self.__renterText.grid(row=0, column=1, padx=10, pady=10)
        self.__ownerText.grid(row=0, column=2, padx=10, pady=10)
        self.__bookText.grid(row=0, column=3, padx=10, pady=10)
        self.__dateText.grid(row=0, column=4, padx=10, pady=10)
        self.__reviewText.grid(row=0, column=5, padx=10, pady=10)

        self.__reviewButtons = []

        i=1
        j=0
        for transaction in self.__transactionsList:

            ctk.CTkLabel(self.__transactionListFrame, text=transaction.getStatus(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.__transactionListFrame, text=transaction.getRenter().getFirstName() + ' ' + transaction.getRenter().getLastName(),font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.__transactionListFrame, text=transaction.getOwner().getFirstName() +  ' ' + transaction.getOwner().getLastName(), font=("Arial", 15)).grid(row=i,column=2,padx=10,pady=10)
            ctk.CTkLabel(self.__transactionListFrame, text=transaction.getBookName(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.__transactionListFrame, text=transaction.getDate().date(), font=("Arial", 15)).grid(row=i,column=4,padx=10,pady=10)
            flag = False
            for review in transaction.getReviews():
                if review.getReviewer() == globals.currentUser:
                    flag = True
            if flag == False:
                self.__reviewButtons.append(ctk.CTkButton(self.__transactionListFrame, text="Add Review", font=("Arial", 15), command=lambda transaction=transaction, reviewer=globals.currentUser:
                                                      self.showReviewPage(transaction, reviewer)))
                self.__reviewButtons[j].grid(row=i, column=5, padx=10, pady=10)
                j+=1
            i+=1

        self.__transactionListFrame.pack()

    def showReviewPage(self, transaction:Transaction, reviewer:User):
        ReviewPage(transaction, reviewer)
