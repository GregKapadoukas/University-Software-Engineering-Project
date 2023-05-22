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
        label = ctk.CTkLabel(self, text="Transaction History")
        label.pack(padx=10, pady=10)
        
        fig , ax = plt.subplots()
        

        transactionsList = Transaction.getClosedTransactions(globals.currentUser)
        transactionsGenreStats = Transaction.getClosedTransactionsDataGenre(transactionsList)
        transactionRenterAgeStats = Transaction. getClosedTransactionsDataRenterAge(transactionsList)

        print(list(transactionRenterAgeStats.keys()))
        print(list(transactionRenterAgeStats.values()))



        GenreStats=plt.pie(list(transactionsGenreStats.values()),labels=list(transactionsGenreStats.keys()))
        GenreStats = FigureCanvasTkAgg(fig,master=self.__graphsFrame)
        GenreStats.draw()
        GenreStats.get_tk_widget().grid(row=0,column=0)

        fig , ax = plt.subplots()

        AgeStats=plt.pie(list(transactionRenterAgeStats.values()),labels=list(transactionRenterAgeStats.keys()))
        AgeStats = FigureCanvasTkAgg(fig,master=self.__graphsFrame)
        AgeStats.draw()
        AgeStats.get_tk_widget().grid(row=0,column=1)
        self.__graphsFrame.pack()