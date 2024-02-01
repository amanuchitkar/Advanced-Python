import time


class library:
    lent_list = []

    def __init__(self, booklist, your_name):
        self.booklist = booklist
        # self.library_name = library_name
        self.name = your_name

    def display(self):
        print("The book of list is following: ")
        return f"Books available= {self.booklist}\n" \
               f"Lented books = {self.lent_list}"

    def add(self):
        book_add = str(input("Which Book you like to add: "))
        self.booklist.append(book_add)
        return f"{book_add} add successfully in library"

    def lent(self):
        lent_book = str(input("Which Book you want to take for lent: "))
        if lent_book in self.booklist:
            return_book = str(input("when you return the book: "))
            self.booklist.remove(lent_book)
            self.lent_list.append(f"{lent_book} : {name}")

            with open(f"{self.name}lentlog.txt", "a") as f1:
                f1.write(
                    f"{self.name} take {lent_book} at time {time.asctime()} he/she return book till {return_book}\n")
            return f"You take {lent_book} successfully from library"
        else:
            return f"Book {lent_book} is not available"

    def return_book(self):
        ret_book = str(input("Which book you want to return: "))
        if f"{ret_book} : {name}" in self.lent_list:
            self.booklist.append(ret_book)
            self.lent_list.remove(f"{ret_book} : {name}")
            with open(f"{self.name}lentlog.txt", "a") as f1:
                f1.write(
                    f"{self.name} return book {ret_book} at time {time.asctime()}\n")

            return f"{ret_book} return successfully"
        else:
            print("you can't lent the book")


booklist_1 = ['To Kill a Mockingbird by Harper Lee',
              'The Great Gatsby by F Scott Fitzgerald',
              'Things Fall Apart by Chinua Achebe',
              'Moby-Dick by Herman Melville',
              'The Color Purple by Alice Walker',
              'Catch-22 by Joseph Heller',
              'Atlas Shrugged by Ayn Rand',
              'The Lord of the Rings by J.R.R. Tolkien',
              'Harry Potter and the Philosopher Stone by J.K. Rowling',
              'Diary of a Wimpy Kid: Old School by Jeff Kinney',
              'The BFG by Roald Dahl',
              'Harry Potter and the Chamber of Secrets by J.K. Rowling',
              'Harry Potter and the prisoner of Azkaban by J.K. Rowling',
              'Diary of a Wimpy Kid: Double Down by Jeff Kinney',
              'Awful Auntie by David Walliams',
              'Diary of a Wimpy Kid: by Hard Luck Jeff Kinney',
              'Wonder by R.J. Palacio',
              'James and the Giant Peach by Roald Dahl',
              'Ratburger by David Walliams',
              'Matilda by Roald Dahl']
name = input("Enter your name: ")
while True:
    op = library(booklist_1, name)
    inp = input("What you wanna do:\n 1.Display books \n 2.Lent book \n 3.add book \n 4.Return book\n: ").upper()
    if inp == "EXIT":
        exit()
    elif inp == "1":
        print(op.display())
    elif inp == "2":
        print(op.lent())
    elif inp == "3":
        print(op.add())
    elif inp == "4":
        print(op.return_book())
    else:
        print("Inappropriate input")
        continue
