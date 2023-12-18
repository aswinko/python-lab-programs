class Publisher:
    def __init__(self, name):
        self.name = name
    def show(self):
        pass
class Book(Publisher):
    def __init__(self, titleName, author, name):
        self.titleName = titleName
        self.author = author
        Publisher.__init__(self, name)
    def show(self):
        pass
class Python(Book):
    def __init__(self, price,no_of_pages, titleName, author, name):
        self.price = price
        self.no_of_pages = no_of_pages
        Book.__init__(self, titleName, author, name)
    def show(self):
        print("Book title : ", self.titleName)
        print("Author : ", self.author)
        print("Publisher : ", self.name)
        print("Price : ", self.price)
        print("No of pages : ", self.no_of_pages)

p = Python(499, 1200, "Encyclopedia", "Aswin", "Indi")
p.show()