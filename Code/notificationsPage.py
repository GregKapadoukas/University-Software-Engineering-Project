import customtkinter as ctk
import globals
from user import User

class NotificationsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.__pageText = ctk.CTkLabel(self, text="Notifications", font=("Arial", 25), text_color="#3A7ABF")
        self.__pageText.pack(padx=10, pady=10)

        self.__notifications = globals.currentUser.loadNotifications()

        self.__notificationsGrid = ctk.CTkFrame(self)
        self.__notificationsGrid.columnconfigure(10, weight=1)

        self.__favoriteUserText = ctk.CTkLabel(self.__notificationsGrid, text="Favorite", font=("Arial", 25))
        self.__titleText = ctk.CTkLabel(self.__notificationsGrid, text="Title", font=("Arial", 25))
        self.__authorText = ctk.CTkLabel(self.__notificationsGrid, text="Author", font=("Arial", 25))
        self.__genreText = ctk.CTkLabel(self.__notificationsGrid, text="Genre", font=("Arial", 25))
        self.__editionText = ctk.CTkLabel(self.__notificationsGrid, text="Edition", font=("Arial", 25))
        self.__publisherText = ctk.CTkLabel(self.__notificationsGrid, text="Publisher", font=("Arial", 25))
        self.__cityText = ctk.CTkLabel(self.__notificationsGrid, text="City", font=("Arial", 25))
        self.__deliveryTypeText = ctk.CTkLabel(self.__notificationsGrid, text="Delivery Type", font=("Arial", 25))
        self.__pricePerDayText = ctk.CTkLabel(self.__notificationsGrid, text="Price Per Day", font=("Arial", 25))
        self.__actionText = ctk.CTkLabel(self.__notificationsGrid, text="Action", font=("Arial", 25))

        self.__favoriteUserText.grid(row=0, column=0, padx=10, pady=10)
        self.__titleText.grid(row=0, column=1, padx=10, pady=10)
        self.__authorText.grid(row=0, column=2, padx=10, pady=10)
        self.__genreText.grid(row=0, column=3, padx=10, pady=10)
        self.__editionText.grid(row=0, column=4, padx=10, pady=10)
        self.__publisherText.grid(row=0, column=5, padx=10, pady=10)
        self.__cityText.grid(row=0, column=6, padx=10, pady=10)
        self.__deliveryTypeText.grid(row=0, column=7, padx=10, pady=10)
        self.__pricePerDayText.grid(row=0, column=8, padx=10, pady=10)
        self.__actionText.grid(row=0, column=9, padx=10, pady=10)

        self.__clearButtons = []

        i=1
        for notification in self.__notifications:
            ctk.CTkLabel(self.__notificationsGrid, text=User.searchUserProfileByID(notification.getFavoriteUserID())[0].getUsername(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.__notificationsGrid, text=notification.getListing().getBook().getName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.__notificationsGrid, text=notification.getListing().getBook().getAuthor(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
            ctk.CTkLabel(self.__notificationsGrid, text=notification.getListing().getBook().getGenre(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.__notificationsGrid, text=notification.getListing().getBook().getEdition(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
            ctk.CTkLabel(self.__notificationsGrid, text=notification.getListing().getBook().getPublisher(), font=("Arial", 15)).grid(row=i, column=5, padx=10, pady=10)
            ctk.CTkLabel(self.__notificationsGrid, text=User.searchUserProfileByID(notification.getFavoriteUserID())[0].getCity(), font=("Arial", 15)).grid(row=i, column=6, padx=10, pady=10)
            ctk.CTkLabel(self.__notificationsGrid, text=notification.getListing().getDeliveryType(), font=("Arial", 15)).grid(row=i, column=7, padx=10, pady=10)
            ctk.CTkLabel(self.__notificationsGrid, text=notification.getListing().getPricePerDay(), font=("Arial", 15)).grid(row=i, column=8, padx=10, pady=10)
            self.__clearButtons.append(ctk.CTkButton(self.__notificationsGrid, text="Clear", font=("Arial", 15), command=
                                          lambda notification=notification : globals.currentUser.clearNotification(notification)))
            self.__clearButtons[i-1].grid(row=i, column=9, padx=10, pady=10)
            i+=1

        self.__notificationsGrid.pack(padx=10, pady=10)
