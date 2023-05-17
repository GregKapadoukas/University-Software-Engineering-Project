class Notification:
    #all = []
    id_incrementer = 0;
    def __init__(self, favorite_user_id:int, listing_id:int):

        assert favorite_user_id >= 0, f"Favorite User ID {favorite_user_id} is not greater or equal to zero!"
        assert listing_id >= 0, f"Listing ID {listing_id} is not greater or equal to zero!"

        self.__id = Notification.id_incrementer
        Notification.id_incrementer+=1
        self.__fav_user_id = favorite_user_id
        self.__listing_id = listing_id

        #Notification.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Favorite User ID: {self.__fav_user_id}, Listing ID: {self.__listing_id}"

#notification1 = Notification(1, 3)
#print(notification1)
