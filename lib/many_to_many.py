from datetime import datetime

class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception('Name must be of type str!')
        self._name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date=datetime.now().strftime('%Y-%m-%d'), royalties=10):
         
        
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([c.royalties for c in Contract.all if c.author == self])




class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise Exception('Title must be of type str!')
        self._title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]        
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]    


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties  = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        
        if not isinstance(author, Author):
            raise Exception('author must be of instance Author.')
        self._author = author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception('book must be of instance Book.')
        self._book = book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception('Only str dates only please!')
        self._date = date

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception('royalties must be an integer.')

        self._royalties = royalties

    def __str__(self):
        return f"{self.date}--> {self._book._title} by {self._author._name}"
    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in Contract.all if c.date == date]
        
           
