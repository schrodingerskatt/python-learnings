import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
# What is cursor ?
'''1. All the operations in SQLite are made by cursors, and not by the connection object itself.
   2. That is so  that we can  have one single connection, but potentially multiple cursors either
      reading data  at most one writing data.'''
cursor.execute('YOUR SQL QUERY HERE')
connection.commit()
# what is commit ?
'''
1. Save the result of this query to disk.
2. Keep a bunch of data in memory until we commit.
3. We can write multiple things together, which is faster.
'''
connection.close()