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

#book1 = Book("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1, "George Allen and Unwin (UK) Houghton Mifflin (US)")
#print(Book.all)
