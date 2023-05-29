import customtkinter as ctk
import globals
from user import User

class MyFavoritesPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.__pageText = ctk.CTkLabel(self, text="My Favorites", font=("Arial", 25), text_color="#3A7ABF")
        self.__pageText.pack(padx=10, pady=10)

        self.__favorites = globals.currentUser.getFavorites()

        self.__favoritesGrid = ctk.CTkFrame(self)
        self.__favoritesGrid.columnconfigure(8, weight=1)

        self.__usernameText = ctk.CTkLabel(self.__favoritesGrid, text="Username", font=("Arial", 25))
        self.__emailText = ctk.CTkLabel(self.__favoritesGrid, text="Email", font=("Arial", 25))
        self.__ageText = ctk.CTkLabel(self.__favoritesGrid, text="Age", font=("Arial", 25))
        self.__cityText = ctk.CTkLabel(self.__favoritesGrid, text="City", font=("Arial", 25))
        self.__phoneNumberText = ctk.CTkLabel(self.__favoritesGrid, text="Phone Number", font=("Arial", 25))
        self.__descriptionText = ctk.CTkLabel(self.__favoritesGrid, text="Description", font=("Arial", 25))
        self.__scoreText = ctk.CTkLabel(self.__favoritesGrid, text="Score", font=("Arial", 25))
        self.__actionText = ctk.CTkLabel(self.__favoritesGrid, text="Action", font=("Arial", 25))

        self.__usernameText.grid(row=0, column=0, padx=10, pady=10)
        self.__emailText.grid(row=0, column=1, padx=10, pady=10)
        self.__ageText.grid(row=0, column=2, padx=10, pady=10)
        self.__cityText.grid(row=0, column=3, padx=10, pady=10)
        self.__phoneNumberText.grid(row=0, column=4, padx=10, pady=10)
        self.__descriptionText.grid(row=0, column=5, padx=10, pady=10)
        self.__scoreText.grid(row=0, column=6, padx=10, pady=10)
        self.__actionText.grid(row=0, column=7, padx=10, pady=10)

        self.__clearButtons = []

        i=1
        for favorite in self.__favorites:
            user = User.searchUserProfileByID(favorite.getFavoriteUserID())[0]
            ctk.CTkLabel(self.__favoritesGrid, text=user.getUsername(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.__favoritesGrid, text=user.getEmail(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.__favoritesGrid, text=user.getAge(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
            ctk.CTkLabel(self.__favoritesGrid, text=user.getCity(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.__favoritesGrid, text=user.getPhoneNumber(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
            ctk.CTkLabel(self.__favoritesGrid, text=user.getDescription(), font=("Arial", 15)).grid(row=i, column=5, padx=10, pady=10)
            ctk.CTkLabel(self.__favoritesGrid, text=user.getScore(), font=("Arial", 15)).grid(row=i, column=6, padx=10, pady=10)
            self.__clearButtons.append(ctk.CTkButton(self.__favoritesGrid, text="Remove Favorite", font=("Arial", 15), command=
                                          lambda favorite=favorite : globals.currentUser.removeFavorite(favorite)))
            self.__clearButtons[i-1].grid(row=i, column=7, padx=10, pady=10)
            i+=1

        self.__favoritesGrid.pack(padx=10, pady=10)
