'''
concerned with storing and retrieving books from csv file.
Format of the csv file :
name,author,read\n
'''

#books_file = 'books.txt'
from typing import List, Tuple
from utils.database_connection import DatabaseConnection
'''def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0')
    #books.append({'name':name, 'author':author, 'read':False})

def get_all_books():
    with open(books_file, 'a') as file:
        lines = [line.strip().split(',') for line in file.readlines()] # [[name, author, read],[name, author, read]]
        return[
            {'Name': line[0], 'Author': line[1], 'Read': line[2]}
            for line in lines
        ]


def mark_book_as_read(name):
    books = get_all_books()

    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)

def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name']!= name]
    _save_all_books(books)'''

Book = Tuple[int, str, str, int]

# creating a book table
def create_book_table()->None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

# inserting the data into table
def add_book(name, author)->None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?,?,0)',(name, author))
    

def get_all_books()->List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * from books')
    # no need to commit because we are not adding any new data
        books = cursor.fetchall()  # gives list of tuples [(name, author, read), (name, author, read)]
    return books

def mark_book_as_read(name)->None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read = 1 WHERE name = ?',(name,))


def delete_book(name)->None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name = ?',(name,))

create_book_table()