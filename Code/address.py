from city import City

class Address:
    all = []
    id_incrementer = 0;
    def __init__(self, street:str, street_number:str, city:City):
        self.__id = Address.id_incrementer
        Address.id_incrementer+=1
        self.__street = street
        self.__street_number = street_number
        self.__city = city

        Address.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Street: {self.__street}, Street Number: {self.__street_number}, City: {self.__city}"

#address1 = Address("Test Street", "5A", City("Patra", "Greece"))
#print(Address.all)
