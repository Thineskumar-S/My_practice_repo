class libmmgmt:

    def __init__ (self,book,name):
        self.book=book
        self.name=name
    def display_all_book(self,book):
        print('Available book')
        for bo in self.book:
            print('book')
    def borrow_book(self,borrow_book):
        if borrow_book in self.book:
            print('the book is available to withdraw')
            self.book.remove(borrow_book)
        else:
            print("the book is not available")
    def return_book(self,retunbook):
        print('Returnin the book')
        self.book.append(rertunbook)

        borrow_book= input('enter the book')
msg=""" Choice
1. Display the Book
2. Borrow the book
3. return the book"""
book=['c','c++',"python"]
s1= libmmgmt(book,'Ram')
while  True:
    print(msg)
    choice = int (input('enter the choice of number:'))
    if choice ==1:
        s1.display_all_book(book)
    if choice ==2:
        s1.borrow_book(borrow_book)
    if choice==3:
        s1.return_book(retrunbook)