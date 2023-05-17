class Book:
    all = []
    id_incrementer = 0;
    def __init__(self, name:str, author:str, genre:str, edition:int, publisher:str):

        assert edition >= 1, f"Edition {edition} is not greater or equal to zero!"

        self.__id = Book.id_incrementer
        Book.id_incrementer+=1
        self.__name = name
        self.__author = author
        self.__genre = genre
        self.__edition = edition
        self.__publisher = publisher

        Book.all.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Name: {self.__name}, Author: {self.__author}, Genre: {self.__genre}, Edition: {self.__edition}, Publisher: {self.__publisher}"

    def getName(self):
        return self.__name

    def getAuthor(self):
        return self.__author

    def getGenre(self):
        return self.__genre

    def getEdition(self):
        return self.__edition

    def getPublisher(self):
        return self.__publisher

    def isSame(self, other):
        if self.__name == other.getName() and self.__author == other.getAuthor() and self.__genre == other.getGenre() and self.__edition == other.getEdition() and self.__publisher == other.getPublisher():
            return True
        else:
            return False

#book1 = Book("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1, "George Allen and Unwin (UK) Houghton Mifflin (US)")
#print(Book.all)
