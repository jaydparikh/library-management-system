from crud import add_book
from crud import get_book
from crud import add_member
from crud import view_member
from crud import issue_book

def addNewBook():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    count = int(input("Enter number of copies: "))
    add_book(title, author, isbn, count)

def printBooks():
    books = get_book()
    for book in books:
        available = "Available" if book.count > 0 else "Not Available" #better than writing if loop
        print(f"{book.id}: '{book.title}' by {book.author} (ISBN: {book.isbn}) - {available} ({book.count} copies)")

def addNewMember():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    add_member(name, email)

def viewMember():
    members = view_member()
    for member in members:
        print(f"Member {member.id} with Name{member.name} and Email: {member.email}")

def issueABook():
    book_id = int(input("Enter book ID:"))
    member_id = int(input("Enter member ID:"))
    issue_book(book_id, member_id)

def main():
    print("************************************")
    print("1. Add Book")
    print("2. Book List")
    print("3. Add Member")
    print("4. View Member")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. View Transactions by Member")
    print("***********************************")
    choice = input("Enter your choice: ",)
    
    if choice == "1":
        addNewBook()
    elif choice =="2":
        printBooks()
    elif choice =="3":
        addNewMember()
    elif choice == "4":
        viewMember()
    elif choice == "5":
        issueABook()
    elif choice == "6":
        pass
    elif choice == "7":
        pass
        
if __name__ == "__main__": #start execution from here
    main()