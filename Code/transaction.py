import datetime
from enum import Enum

class Status(Enum):
    To_Be_Confirmed = 1
    Waiting_To_Be_Delivered = 2
    Marked_Delivered_By_One = 3
    Marked_Delivered = 4
    Marked_Returned_By_One = 5
    Marked_Returned = 6
    Finished = 7
    Denied = 8

class Transaction:
    all = []
    id_incrementer = 0;
    def __init__(self, renter_id:int, owner_id:int, listing_id:int, starting_date:datetime.datetime):

        assert renter_id >= 0, f"Renter User ID {renter_id} is not greater or equal to zero!"
        assert owner_id >= 0, f"Seller User ID {owner_id} is not greater or equal to zero!"
        assert listing_id >= 0, f"Listing ID {listing_id} is not greater or equal to zero!"
        assert renter_id != owner_id, f"Renter User ID {renter_id} is the same as Owner User ID {owner_id}!"

        self.__id = Transaction.id_incrementer
        Transaction.id_incrementer+=1
        self.__renter_id = renter_id
        self.__owner_id = owner_id
        self.__status = Status.To_Be_Confirmed
        self.__listing_id = listing_id
        self.__starting_date = starting_date

        Transaction.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Renter User ID: {self.__renter_id}, Owner User ID: {self.__owner_id}, Status: {self.__status}, Listing ID: {self.__listing_id}, Starting Date: {self.__starting_date}"

#transaction1 = Transaction(1, 2, 3, datetime.datetime.now())
#print(transaction1)
