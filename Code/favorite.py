import datetime
from enum import Enum

class Score(Enum):
    To_Be_Confirmed = 1
    Waiting_To_Be_Delivered = 2
    Marked_Delivered_By_One = 3
    Marked_Delivered = 4
    Marked_Returned_By_One = 5
    Marked_Returned = 6
    Finished = 7
    Denied = 8

class Favorite:
    #all = []
    id_incrementer = 0;
    def __init__(self, favorite_user_id:int, last_notification_date:datetime.datetime):

        assert favorite_user_id >= 0, f"Notification User ID {favorite_user_id} is not greater or equal to zero!"

        self.__id = Favorite.id_incrementer
        Favorite.id_incrementer+=1
        self.__favorite_user_id = favorite_user_id
        self.__last_notification_date = last_notification_date

        #Notification.all.append(self)

    def getFavoriteUserID(self):
        return self.__favorite_user_id

    def __repr__(self):
        return f"ID: {self.__id}, Favorite User ID: {self.__favorite_user_id}, Last Notification Date: {self.__last_notification_date}"

#favorite1 = Favorite(1, datetime.datetime(2015,2,2))
#print(favorite1)
