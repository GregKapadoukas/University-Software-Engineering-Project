import customtkinter as ctk
import globals
from user import User

class NotificationsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Notifications", font=("Arial", 25), text_color="#3A7ABF")
        label.pack(padx=10, pady=10)

        notifications = globals.currentUser.getNotifications()

        self.notificationsGrid = ctk.CTkFrame(self)
        self.notificationsGrid.columnconfigure(10, weight=1)

        self.favoriteUserText = ctk.CTkLabel(self.notificationsGrid, text="Owner", font=("Arial", 25))
        self.titleText = ctk.CTkLabel(self.notificationsGrid, text="Title", font=("Arial", 25))
        self.authorText = ctk.CTkLabel(self.notificationsGrid, text="Author", font=("Arial", 25))
        self.genreText = ctk.CTkLabel(self.notificationsGrid, text="Genre", font=("Arial", 25))
        self.editionText = ctk.CTkLabel(self.notificationsGrid, text="Edition", font=("Arial", 25))
        self.publisherText = ctk.CTkLabel(self.notificationsGrid, text="Publisher", font=("Arial", 25))
        self.cityText = ctk.CTkLabel(self.notificationsGrid, text="City", font=("Arial", 25))
        self.deliveryTypeText = ctk.CTkLabel(self.notificationsGrid, text="Delivery Type", font=("Arial", 25))
        self.pricePerDayText = ctk.CTkLabel(self.notificationsGrid, text="Price Per Day", font=("Arial", 25))
        self.actionText = ctk.CTkLabel(self.notificationsGrid, text="Action", font=("Arial", 25))

        self.favoriteUserText.grid(row=0, column=0, padx=10, pady=10)
        self.titleText.grid(row=0, column=1, padx=10, pady=10)
        self.authorText.grid(row=0, column=2, padx=10, pady=10)
        self.genreText.grid(row=0, column=3, padx=10, pady=10)
        self.editionText.grid(row=0, column=4, padx=10, pady=10)
        self.publisherText.grid(row=0, column=5, padx=10, pady=10)
        self.cityText.grid(row=0, column=6, padx=10, pady=10)
        self.deliveryTypeText.grid(row=0, column=7, padx=10, pady=10)
        self.pricePerDayText.grid(row=0, column=8, padx=10, pady=10)
        self.actionText.grid(row=0, column=9, padx=10, pady=10)

        self.clearButtons = []

        i=1
        for notification in notifications:
            ctk.CTkLabel(self.notificationsGrid, text=User.searchUserProfileByID(notification.getFavoriteUserID())[0].getFirstName() + ' ' + User.searchUserProfileByID(notification.getFavoriteUserID())[0].getLastName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.notificationsGrid, text=notification.getListing().getBook().getName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.notificationsGrid, text=notification.getListing().getBook().getAuthor(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
            ctk.CTkLabel(self.notificationsGrid, text=notification.getListing().getBook().getGenre(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.notificationsGrid, text=notification.getListing().getBook().getEdition(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
            ctk.CTkLabel(self.notificationsGrid, text=notification.getListing().getBook().getPublisher(), font=("Arial", 15)).grid(row=i, column=5, padx=10, pady=10)
            ctk.CTkLabel(self.notificationsGrid, text=User.searchUserProfileByID(notification.getFavoriteUserID())[0].getCity(), font=("Arial", 15)).grid(row=i, column=6, padx=10, pady=10)
            ctk.CTkLabel(self.notificationsGrid, text=notification.getListing().getDeliveryType(), font=("Arial", 15)).grid(row=i, column=7, padx=10, pady=10)
            ctk.CTkLabel(self.notificationsGrid, text=notification.getListing().getPricePerDay(), font=("Arial", 15)).grid(row=i, column=8, padx=10, pady=10)
            self.clearButtons.append(ctk.CTkButton(self.notificationsGrid, text="Clear", font=("Arial", 15), command=
                                          lambda notification=notification : globals.currentUser.clearNotification(notification)))
            self.clearButtons[i-1].grid(row=i, column=9, padx=10, pady=10)
            i+=1

        self.notificationsGrid.pack(padx=10, pady=10)
