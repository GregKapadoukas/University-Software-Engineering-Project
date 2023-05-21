import datetime
from listing import Listing
from enum import Enum
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
    def __init__(self, renter:User, owner:User, listing :Listing, starting_date:datetime.datetime):

        assert renter_id >= 0, f"Renter User ID {renter_id} is not greater or equal to zero!"
        assert owner_id >= 0, f"Seller User ID {owner_id} is not greater or equal to zero!"
        assert listing_id >= 0, f"Listing ID {listing_id} is not greater or equal to zero!"
        assert renter_id != owner_id, f"Renter User ID {renter_id} is the same as Owner User ID {owner_id}!"

        self.__id = Transaction.id_incrementer
        Transaction.id_incrementer+=1
        self.__renter = renter
        self.__owner = owner
        self.__status = Status.To_Be_Confirmed
        self.__listing = listing
        self.__starting_date = starting_date

        Transaction.all.append(self)

    def getStatus(self):
        return self.__status

    def __repr__(self):
        return f"ID: {self.__id}, Renter User ID: {self.__renter_id}, Owner User ID: {self.__owner_id}, Status: {self.__status}, Listing ID: {self.__listing_id}, Starting Date: {self.__starting_date}"

    @staticmethod
    def getClosedTransactions():
        closedTransactions = []
        for transaction in Transaction.all:
            if transaction.getStatus()==Status.Finished:
                closedTransactions.append(transaction)
        return closedTransactions

    @staticmethod
    def getClosedTransactionsDataGenre(closedTransactionsList):
        genreCount = {}
        for transaction in closedTransactionsList:
            genre = transaction.getBook().getGenre()
            if (genre in genreCount):
                genreCount[genre]+=1
            else:
                genreCount.update({genre:1})

        return genreCount

    @staticmethod
    def getClosedTransactionsDataRenterAge
        ages = {
        "0-20" : 0,
        "21-30" : 0,
        "31-40" : 0,
        "41-50" : 0,
        "50+" : 0
        }
        for transaction in closedTransactionsList:
            if (renter.getAge() < 21):
                ages[0-20] += 1
            elif (renter.getAge() < 31):
                ages[21-30] +=1
            elif (renter.getAge() < 41):
                ages[31-40] +=1
            elif (renter.getAge() < 51):
                ages[41-50] +=1
            else:
                ages[50+] +=1

            return ages



#transaction1 = Transaction(1, 2, 3, datetime.datetime.now())
#print(transaction1)
