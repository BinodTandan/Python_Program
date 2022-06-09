# Implementing a Student Library System

class Library:
    def __init__(self, bookList):
        self.bookList = bookList

    def displayAvailableBooks(self):
        print("The books available in library are: ")
        # for items in self.bookList:
        #     print("--- " + items)
        print("\n --- ".join(self.bookList))

    def borrowBooks(self, bookName):
        
        if bookName in self.bookList:
            self.bookList.remove(bookName)
            print("The book you look for is available in library. So we kindly request it to return in time")
            return True
        else:
            print("Sorry!!! The book  you want is not available in our library.")
            return False

    def issueDate(self):
        self.date = (input("Date of book issued: "))
        print(f"This book is issued in date : {self.date}")

    def returnDate(self):
        self.date = (input("Date of book returned: "))
        print(f"This book is returned in date : {self.date}")

    def returnBooks(self, bookName):
        print("Thanks for returning book in time!!!")
        self.bookList.append(bookName)

class Student:
    def requestBook(self):
        self.book = input("Enter the book name you want: ").upper
        return self.book

    def returnBook(self):
        self.book = input("Enter the name o book you want to return: ")
        return self.book


if __name__ == "__main__":
    books = Library(["Python", "Java", "C++", ".Net", "C", "Web Development", "Microprocessor", "DBMS", "DMDW", "Statistic"])
    student = Student()

    while(True):
        print('''~~~~~~~~~Welcome to our library System~~~~~~~~~
        Please choose an option
        1.  List of books available
        2.  Request the book
        3.  Add/Return the book
        4.  Date of book issued
        5.  Date of book returned
        6.  Exit from system''')
        a = int(input("choose number:  "))
        if a ==1:
            books.displayAvailableBooks()
        elif a ==2:
            books.borrowBooks(student.requestBook())
        elif a ==3:
            books.returnBooks(student.returnBook())
        elif a ==4:
            books.issueDate()
        elif a ==5:
            books.returnDate()
        else:
            exit()


