from models import Book
from models import Member
from models import Transaction
from database import session
from datetime import date

# we define functions here and not within database classes 
def add_book(title, author, isbn, count):
    print("CRUD Book")
    book = Book(title=title, author=author, isbn=isbn, count=count)
    session.add(book)
    session.commit()

def get_book():
    return session.query(Book).all()

def add_member(name, email):
    member = Member(name=name, email=email)
    session.add(member)
    session.commit()

def view_member():
    return session.query(Member).all()

def issue_book(book_id, member_id):
    book = session.query(Book).filter_by(id = book_id).first() #or [0] first entry of list
    if book and book.count >0: #does book exist and count available
        transaction = Transaction(book_id = book_id, member_id = member_id, issue_date = date.today())
        book.count -1
        session.add(transaction)
        session.commit()
    else:
        print("Book not available")
