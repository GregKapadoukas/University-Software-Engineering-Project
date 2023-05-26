import datetime
from enum import Enum
from listing import Listing
from user import User

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
    def __init__(self, renter_id:int, owner_id:int, listing_id:int):

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
        self.__transaction_date = "Not Started"

        Transaction.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Renter User ID: {self.__renter_id}, Owner User ID: {self.__owner_id}, Status: {self.__status}, Listing ID: {self.__listing_id}, Starting Date: {self.__starting_date}"

    def getRenterID(self):
        return self.__renter_id

    def getOwnerID(self):
        return self.__owner_id

    def getStatus(self):
        return self.__status

    def getStartingDate(self):
        return self.__starting_date.date()

    def getBookName(self):
        return Listing.getListingByID(self.__listing_id)[0].getBook().getName()

    def getAmountAndCheckEnough(self):
        a = datetime.date.today() 
        b = self.__starting_date.date()
        diff = a - b
        amount = Listing.getListingByID(self.__listing_id)[0].getPricePerDay() + (diff.days * Listing.getListingByID(self.__listing_id)[0].getPricePerDay())
        if amount > User.searchUserProfileByID(self.__renter_id)[0].getBalance():
            self.__status = Status.Finished
            User.searchUserProfileByID(self.__owner_id)[0].addBalance(30.0)
        return amount

    def acceptTransaction(self):
        if self.__status == Status.To_Be_Confirmed:
            self.__status = Status.Waiting_To_Be_Delivered
            self.__starting_date = datetime.datetime.now()
            if User.searchUserProfileByID(self.__renter_id)[0].getSafetyDeposit() == True:
                pass
            else:
                self.__status = Status.Denied

    def denyTransaction(self):
        if self.__status == Status.To_Be_Confirmed:
            self.__status = Status.Denied
            User.searchUserProfileByID(self.__renter_id)[0].addBalance(30.0)

    def updateStatus(self):
        if self.__status == Status.Waiting_To_Be_Delivered:
            self.__status = Status.Marked_Delivered_By_One
            self.updateStatus() #Automatically marked delivered by second user

        elif self.__status == Status.Marked_Delivered_By_One:
            self.__status = Status.Marked_Delivered

        elif self.__status == Status.Marked_Delivered:
            self.__status = Status.Marked_Returned_By_One
            self.updateStatus() #Automatically marked returned by second user
        elif self.__status == Status.Marked_Returned_By_One:
            self.__status = Status.Finished
            User.searchUserProfileByID(self.__renter_id)[0].addBalance(30.0) 
            User.searchUserProfileByID(self.__owner_id)[0].addBalance(self.getAmountAndCheckEnough())

    @staticmethod
    def getByRenterID(renter_id:int):
        result = []
        for transaction in Transaction.all:
            if transaction.getRenterID() == renter_id:
                result.append(transaction)
        return result

    @staticmethod
    def getByOwnerID(owner_id:int):
        result = []
        for transaction in Transaction.all:
            if transaction.getOwnerID() == owner_id:
                result.append(transaction)
        return result

#transaction1 = Transaction(1, 2, 3, datetime.datetime.now())
#print(transaction1)
