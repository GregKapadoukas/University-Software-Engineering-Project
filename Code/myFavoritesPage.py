import customtkinter as ctk
import globals
from user import User

class MyFavoritesPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="My Favorites", font=("Arial", 25), text_color="#3A7ABF")
        label.pack(padx=10, pady=10)

        favorites = globals.currentUser.getFavorites()

        self.favoritesGrid = ctk.CTkFrame(self)
        self.favoritesGrid.columnconfigure(9, weight=1)

        self.firstNameText = ctk.CTkLabel(self.favoritesGrid, text="First Name", font=("Arial", 25))
        self.lastNameText = ctk.CTkLabel(self.favoritesGrid, text="Last Name", font=("Arial", 25))
        self.emailText = ctk.CTkLabel(self.favoritesGrid, text="Email", font=("Arial", 25))
        self.ageText = ctk.CTkLabel(self.favoritesGrid, text="Age", font=("Arial", 25))
        self.cityText = ctk.CTkLabel(self.favoritesGrid, text="City", font=("Arial", 25))
        self.phoneNumberText = ctk.CTkLabel(self.favoritesGrid, text="Phone Number", font=("Arial", 25))
        self.descriptionText = ctk.CTkLabel(self.favoritesGrid, text="Description", font=("Arial", 25))
        self.scoreText = ctk.CTkLabel(self.favoritesGrid, text="Score", font=("Arial", 25))
        self.actionText = ctk.CTkLabel(self.favoritesGrid, text="Action", font=("Arial", 25))

        self.firstNameText.grid(row=0, column=0, padx=10, pady=10)
        self.lastNameText.grid(row=0, column=1, padx=10, pady=10)
        self.emailText.grid(row=0, column=2, padx=10, pady=10)
        self.ageText.grid(row=0, column=3, padx=10, pady=10)
        self.cityText.grid(row=0, column=4, padx=10, pady=10)
        self.phoneNumberText.grid(row=0, column=5, padx=10, pady=10)
        self.descriptionText.grid(row=0, column=6, padx=10, pady=10)
        self.scoreText.grid(row=0, column=7, padx=10, pady=10)
        self.actionText.grid(row=0, column=8, padx=10, pady=10)

        self.clearButtons = []

        i=1
        for favorite in favorites:
            user = User.searchUserProfileByID(favorite.getFavoriteUserID())[0]
            ctk.CTkLabel(self.favoritesGrid, text=user.getFirstName(), font=("Arial", 15)).grid(row=i, column=0, padx=10, pady=10)
            ctk.CTkLabel(self.favoritesGrid, text=user.getLastName(), font=("Arial", 15)).grid(row=i, column=1, padx=10, pady=10)
            ctk.CTkLabel(self.favoritesGrid, text=user.getEmail(), font=("Arial", 15)).grid(row=i, column=2, padx=10, pady=10)
            ctk.CTkLabel(self.favoritesGrid, text=user.getAge(), font=("Arial", 15)).grid(row=i, column=3, padx=10, pady=10)
            ctk.CTkLabel(self.favoritesGrid, text=user.getCity(), font=("Arial", 15)).grid(row=i, column=4, padx=10, pady=10)
            ctk.CTkLabel(self.favoritesGrid, text=user.getPhoneNumber(), font=("Arial", 15)).grid(row=i, column=5, padx=10, pady=10)
            ctk.CTkLabel(self.favoritesGrid, text=user.getDescription(), font=("Arial", 15)).grid(row=i, column=6, padx=10, pady=10)
            ctk.CTkLabel(self.favoritesGrid, text=user.getScore(), font=("Arial", 15)).grid(row=i, column=7, padx=10, pady=10)
            self.clearButtons.append(ctk.CTkButton(self.favoritesGrid, text="Remove Favorite", font=("Arial", 15), command=
                                          lambda favorite=favorite : globals.currentUser.removeFavorite(favorite)))
            self.clearButtons[i-1].grid(row=i, column=8, padx=10, pady=10)
            i+=1

        self.favoritesGrid.pack(padx=10, pady=10)
