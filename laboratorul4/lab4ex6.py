class LibraryItem:
    def __init__(self, title, author, callNumber, checkedOut=False):
        self.title = title
        self.author = author
        self.callNumber = callNumber
        self.checkedOut = checkedOut

    def checkOut(self):
        if not self.checkedOut:
            self.checkedOut = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def returnItem(self):
        if self.checkedOut:
            self.checkedOut = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is not checked out.")

    def displayInfo(self):
        print(f"Title: {self.title}.")
        print(f"Author: {self.author}.")
        print(f"Call Number: {self.callNumber}.")
        status = "Checked out" if self.checkedOut else "Available"
        print(f"Status: {status}.")

class Book(LibraryItem):
    def __init__(self, title, author, callNumber, checkedOut=False, numPages=0):
        super().__init__(title, author, callNumber, checkedOut)
        self.numPages = numPages

    def displayInfo(self):
        super().displayInfo()
        print(f"Number of Pages: {self.numPages}.")

class DVD(LibraryItem):
    def __init__(self, title, director, callNumber, checkedOut=False, runTime=0):
        super().__init__(title, director, callNumber, checkedOut)
        self.runTime = runTime

    def displayInfo(self):
        super().displayInfo()
        print(f"Run Time: {self.runTime} minutes.")

class Magazine(LibraryItem):
    def __init__(self, title, publisher, callNumber, checkedOut=False, issueNumber=0):
        super().__init__(title, publisher, callNumber, checkedOut)
        self.issueNumber = issueNumber

    def displayInfo(self):
        super().displayInfo()
        print(f"Issue Number: {self.issueNumber}.")

book = Book("Divergent", "Mike Tyson", "123", numPages=300)
dvd = DVD("Insurgent", "Jon Jones", "456", runTime=200)
magazine = Magazine("Experiment", "Connor McGregor", "789", issueNumber=400)

book.checkOut()
dvd.checkOut()
magazine.checkOut()

book.displayInfo()
dvd.displayInfo()
magazine.displayInfo()

book.returnItem()
dvd.returnItem()
magazine.returnItem()
