class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        
    def __setattr__(self, key, value):
        if not ((key in ['title', 'author'] and type(value) is str) or (key in ['pages', 'year'] and type(value) is int)):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)
            

book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
