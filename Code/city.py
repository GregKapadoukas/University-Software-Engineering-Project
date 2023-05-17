class City:
    all = []
    id_incrementer = 0;
    def __init__(self, name:str, country:str):
        self.__id = City.id_incrementer
        City.id_incrementer+=1
        self.__name = name
        self.__country = country

        City.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Name: {self.__name}, Country: {self.__country}"

    def getName(self):
        return self.__name

#city1 = City("Patra", "Greece")
#print(City.all)
