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

        

        self.__id = Transaction.id_incrementer
        Transaction.id_incrementer+=1
        self.__renter = renter
        self.__owner = owner
        self.__status = Status.To_Be_Confirmed
        self.__listing = listing
        self.__starting_date = starting_date
        self.__ratings = [{}]
        print(self.__id)
        Transaction.all.append(self)

    def getStatus(self):
        return self.__status

    def __repr__(self):
        return f"ID: {self.__id}, Renter User : {self.__renter}, Owner User : {self.__owner}, Status: {self.__status}, Listing : {self.__listing}, Starting Date: {self.__starting_date}"
    def setStatus(self, status:Status):
        self.__status=status
    def getListing(self):
        return self.__listing
    def getRenter(self):
        return self.__renter
    def getOwner(self):
        return self.__owner


    @staticmethod
    def getClosedTransactions(bookOwner : User):
        closedTransactions = []
        for transaction in Transaction.all:
            if (transaction.getStatus()==Status.Finished) and (transaction.getOwner() == bookOwner):
                closedTransactions.append(transaction)
        
        return closedTransactions

    @staticmethod
    def getClosedTransactionsDataGenre(closedTransactionsList):
        genreCount = {}
        for transaction in closedTransactionsList:
            genre = transaction.getListing().getBook().getGenre()
            if (genre in genreCount):
                genreCount[genre]+=1
            else:
                genreCount.update({genre:1})

        
        return genreCount

    @staticmethod
    def getClosedTransactionsDataRenterAge(closedTransactionsList):
        ages = {}
        
        for transaction in closedTransactionsList:
            renterAge=transaction.getRenter().getAge()

            print (renterAge)
            if (renterAge < 21):
                if "0-20" in ages:
                    ages["0-20"] += 1
                else:
                    ages.update({"0-20":1})

            elif (renterAge < 31):

                if "21-30" in ages:

                    ages["21-30"] +=1
                else:
                    ages.update({"21-30":1})
            elif (renterAge < 41):
                if "31-40" in ages:
                    ages["31-40"] +=1
                else:
                    ages.update({"31-40":1})
            elif (renterAge < 51):
                if "41-50" in ages:
                    ages["41-50"] +=1
                else:
                    ages.update({"41-50":1})
            else:
                if "50+" in ages:
                    ages["50+"] +=1
                else:
                    ages.update({"50+":1})

            print (ages)

        return ages

    def setBookOfferStatus(self,status:Status):
        self.__status=status
    

#transaction1 = Transaction(1, 2, 3, datetime.datetime.now())
#print(transaction1)
