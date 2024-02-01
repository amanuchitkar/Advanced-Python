import time


class Library:
    def __init__(self, lists, name):
        self.booklist = lists
        self.name = name
        self.lent_dict = {}

    def display(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lentbook(self, book, user):
        if book not in self.lent_dict.keys():
            self.lent_dict.update({book: user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by{self.lent_dict[book]}")

    def add(self, book):
        self.booklist.append(book)
        print("Your book added successfully")

    def returns(self, book):
        self.lent_dict.pop(book)


if __name__ == '__main__':
    op = Library(['Python', 'c', 'python', 'C++ Basics', 'Algorithms by CLRS'], "Aman")
    while True:
        print(f"Welcome to the {op.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        inpu = input(": ")
        if inpu not in ['1', '2', '3', '4']:
            print("input is inappropriate")
            continue
        else:
            userchoice = int(inpu)
        if userchoice == 1:
            op.display()
        elif userchoice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            op.lentbook(book, user)
        elif userchoice == 3:
            book = input("Enter book name: ")
            op.add(book)
        elif userchoice == 4:
            book = input("Enter book name: ")
            op.returns(book)
        else:
            print("Not a valid option")
        print("Press q to quit and c to continue")
        userinput = ""
        while userinput != 'q' and userinput != 'c':
            userinput = input(":").lower()
            if userinput == 'q':
                exit()
            elif userinput == 'c':
                continue
