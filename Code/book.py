class Book:
    unique = []
    id_incrementer = 0;
    def __init__(self, name:str, author:str, genre:str, edition:int, publisher:str):

        assert edition >= 1, f"Edition {edition} is not greater or equal to zero!"

        self.__name = name
        self.__author = author
        self.__genre = genre
        self.__edition = edition
        self.__publisher = publisher

        same = False
        for book in Book.unique:
            if self.isSame(book):
                same = True

        if same == False:
            self.__id = Book.id_incrementer
            Book.id_incrementer+=1
            Book.unique.append(self)

    def __repr__(self):
        return f"ID: {self.__id}, Name: {self.__name}, Author: {self.__author}, Genre: {self.__genre}, Edition: {self.__edition}, Publisher: {self.__publisher}"

    def getID(self):
        return self.__id

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

    @staticmethod
    def getBookFromID(book_id:int):
        for book in Book.unique:
            if book.getID() == book_id:
                return book
        return -1

    @staticmethod
    def getBookIDFromInstance(find_book):
        for book in Book.unique:
            if find_book.isSame(book):
                return book.getID()
        return -1

#book1 = Book("The Hobbit", "J. R. R. Tolkien", "Fantasy", 1, "George Allen and Unwin (UK) Houghton Mifflin (US)")
#print(Book.all)
