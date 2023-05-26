import customtkinter as ctk
from listing import Listing

class Notification:
    #all = []
    id_incrementer = 0;
    def __init__(self, favorite_user_id:int, listing:Listing):

        self.__id = Notification.id_incrementer
        Notification.id_incrementer+=1
        self.__favorite_user_id = favorite_user_id
        self.__listing = listing

        #Notification.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Favorite User ID: {self.__favorite_user_id}, Listing ID: {self.__listing}"

    def getListing(self):
        return self.__listing

    def getFavoriteUserID(self):
        return self.__favorite_user_id

#notification1 = Notification(1, 3)
#print(notification1)
