class lmgmt:

    academics =['c','c++','python']
    fiction = ['Sherlock Holmes','Mystery of Meluha','The Alchemist','cinderla']
    non_fiction = ['The Tata way',"the hp way",'The warren buffet approach', 'follow your passion']
    list_of_book=[academics,fiction,non_fiction]

    def welcome(lmt):
        print('welcome to the library!!!')

    def __init__ (self,name,grade):
        self.name=name
        self.grade=grade

    def display_books(self):
        print('Avaialable books')
        for book in lmgmt.list_of_book:
            if lmgmt.list_of_book [0]:
                print('Academics Collection:',end='')
                print(book)
            elif lmgmt.list_of_book[1]:
                print('Fiction Collection:',end='')
                print(book)
            elif  lmgmt.list_of_book [2]:
                print('Non_fiction Collection:',end='')
                print(book)

    def borrowing (self,borrow_book):
        print(self.name + 'thanks for Borrowing the book')
        if borrow_book in lmgmt.list_of_book[0]:
            lmgmt.list_of_book.remove(borrow_book)
        elif borrow_book in lmgmt.list_of_book[1]:
            lmgmt.list_of_book.remove(borrow_book)
        elif borrow_book in lmgmt.list_of_book[2]:
            lmgmt.list_of_book.remove(borrow_book)

   ''' def returning (self,retrun_book):
        print(self.name + 'thanks for returning the book')
        lmgmt.list_of_book.append(retrun_book)
'''
Msg= '''Enter the choice of number for self-service
1. Display Available books
2. Borrow 
3. Return
'''
name=input("Enter your Name:")
grade= input('Enter your grade:')
student1=lmgmt(name,grade)


while True:
    print(Msg)
    choice= int(input('Enter your choice of number:'))
    if choice ==1:
        student1.display_books()
    elif choice==2:
        print('the list of books are available')
        student1.display_books()
        borrow_book=input('Enter the book you want to borrow:')
        student1.borrowing(borrow_book)
    elif choice==3:
        student1.returning(returnbook)
    else:
        print('Thanks for Using the Library')
        quit()

