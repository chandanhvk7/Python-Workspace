from ex19 import Book
import json

def main():
    b2=Book(title='Percy Jackson',author='Rick Riordan',price=799.0)

    print(json.dumps(b2,cls=Book.BookEncoder))

    books=[Book(title='Shadow and Bone',author='Leigh Bardugo',price=399.0),
           Book(title='Crooked Kingdom',author='Leigh Bardugo',price=499.0),
           b2]
    print(json.dumps(books,cls=Book.BookEncoder))

    book1={
        'c':b2,
        'java':books[0],
        'python':books[1]
    }

    print(json.dumps(books,cls=Book.BookEncoder))

if __name__=="__main__":
    main()