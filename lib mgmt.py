class libmgmt:

    def __init__ (self,book,name):
        self.book=book
        self.name=name
    def display_all_book(self):
        print('Available book')
        for book in self.book:
            print(book)
    def borrow_book(self,borrowbook):
        if borrowbook in self.book:
            print('the book is available to lend')
            self.book.remove(borrowbook)
        else:
            print('There is no such book is available')
    def return_book(self,returnbook):
        self.book.append(retrunbook)

msg=""" Choice
1. Display the Book
2. Borrow the book
3. return the book"""
book=['c','c++',"python"]
s1= libmgmt(book,'Ram')
while  True:
    print(msg)
    choice = int (input('enter the choice of number:'))
    if choice ==1:
        s1.display_all_book()
    elif choice ==2:
        borrowbook = input('enter the book:')
        s1.borrow_book(borrowbook)
    elif choice==3:
        retrunbook: str= input('enter the return book:')
        s1.return_book(retrunbook)
    else:
        print('thanks for spending time in library' )
        quit()