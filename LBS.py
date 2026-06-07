print("*******************")
print("WELCOME TO LIBRARY")
print("*******************")

# ---------- ADMIN OPTIONS ----------
def admin_option():
    print("""
Admin Menu:
1. Add Book
2. View Books
3. Issue Book
4. Return Book
5. Logout
""")
    
# --------Student Login ---------------

def student_options(data):
    print("""
Student Menu:
1.View Books
2.Issue Book
3.Return Book
4.Logout
""")

# ------------ ADD BOOKS -----------
data = {}

def add_books(data):
    while True:
        author_name = input("Enter the author name: ").lower()
        book_name = input("Enter the book name: ").lower()

        data[book_name] = author_name

        with open("Data_books.txt", "a") as file:
            file.write(f"Author name = {author_name} , book name = {book_name}\n")

        op = input("Do you want to add more books? (y/n): ").lower()

        if op != 'y':
            break

# -------------- VIEW BOOKS ---------------
def view_books(data):
    try:
        print("\n----- BOOKS AVAILABLE -----")

        with open("Data_books.txt", "r") as file:
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("No books are available!")

# -------------- ISSUE BOOKS ----------------
def issue_books(data):

    book = input("Enter the book name to issue: ").lower()
    found = False

    with open("Data_books.txt", "r") as file:
        lines = file.readlines()

    with open("Data_books.txt", "w") as file:
        for line in lines:
            if book in line.lower():
                found = True
            else:
                file.write(line)

    if found:
        print("BOOK SUCCESSFULLY ISSUED")
    else:
        print("BOOK NOT AVAILABLE!")

# ------------- RETURN BOOKS ------------------
def return_book(data):

    author= input("Enter the author name: ").lower()
    book= input("Enter the book name: ").lower()

    found = False

    try:
        with open("Data_books.txt", "r") as file:
            for line in file:
                if book in line.lower():
                    found = True
                    break
    except FileNotFoundError:
        pass

    if found:
        print("BOOK ALREADY PRESENT!")
    else:
        with open("Data_books.txt", "a") as file:
            file.write(f"Author name = {author} , book name = {book}\n")

        print("BOOK RETURNED SUCCESSFULLY")

# ---------- ADMIN LOGIN ----------
def admin_login(data):
    password = input("Enter the password for Admin Login: ")

    if password == "Durgesh@9604":
        print("Login Successfully")

        while True:
            admin_option()

            try:
                ch = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if ch == 1:
                print("Add Book")
                add_books(data)

            elif ch == 2:
                print("View Books")
                view_books(data)

            elif ch == 3:
                print("Issue Book")
                issue_books(data)

            elif ch == 4:
                print("Return Book")
                return_book(data)

            elif ch == 5:
                print("Logging Out...")
                break

            else:
                print("Invalid Choice!")

    else:
        print("Wrong Password!")

# ---------- STUDENT LOGIN ----------

def Student_Login(data):

    while True:
        student_options(data)

        try:
            choice = int(input("Enter the choice : "))
        except ValueError:
            print("Please Enter a valid choice!")
            continue

        if choice == 1:
            view_books(data)

        elif choice == 2:
            issue_books(data)

        elif choice == 3:
            return_book(data)

        elif choice == 4:
            print("LOGGING OUT......")
            break

        else:
            print("INVALID CHOICE!")

# ---------- MAIN PROGRAM ----------
while True:
    print("""
1. Admin Login
2. Student Login
3. Exit
""")

    try:
        choice = int(input("Enter the choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        print("Welcome to Admin Login")
        admin_login(data)
  
        

    elif choice == 2:
        print("Welcome to Student Login")
        Student_Login(data)
        
    
    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")