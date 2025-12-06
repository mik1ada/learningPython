class Book:
  def __init__(self, author = 'unknown', title = 'unknown', isbn = 'unknown', year = 'unknown'):
    self.author = author
    self.title = title
    self.isbn = isbn
    self.year = year

  def printData(self):
    print(self.author, self.title, self.isbn, self.year)

book1 = Book('Michal Nowak', 'Finanse', '6512sa', 2020)
book1.printData()

book2 = Book('Adam', year = 2010)
book2.printData()