# Imports
import sqlite3

# Book Art
book_art = '''                                                                                 
░░              ░░                    ░░                    ░░                    ░░    
                                                                                        
                                                                                        
                              ██████████          ██████████                            
░░      ░░            ░░    ██          ██  ░░  ██          ██    ░░      ░░            
                          ██              ██  ██              ██                        
                        ██      ██  ██      ██      ██  ██      ██                      
                      ████  ██          ██  ██  ██          ██  ████                    
        ░░      ░░  ██░░██                  ██                  ██░░██    ░░      ░░    
                    ██░░██      ██  ██      ██      ██  ██      ██░░██                  
                    ██░░██  ██          ██  ██  ██          ██  ██░░██                  
                    ██░░██                  ██                  ██░░██                  
                    ██░░██                  ██                  ██░░██                  
                    ██░░██  ████████████    ██    ████████████  ██░░██                  
                    ██░░████            ██  ██  ██            ████░░██                  
░░                  ██░░██  ████████████  ██████  ████████████  ██░░██                  
                    ██░░████░░░░░░░░░░░░██  ██  ██░░░░░░░░░░░░████░░██                  
                    ██░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░██                  
                    ██░░░░░░░░██████████░░░░░░░░░░██████████░░░░░░░░██                  
                    ██░░░░████          ██████████          ████░░░░██                  
                      ████                                      ████                                                                                                      
'''

        # ----- [Create Database] ----- #

# Create Database
db = sqlite3.connect('ebookstore')
# Make a cursor object
cursor = db.cursor ()

# --- Drop tables so they can be created again - for testing purposes only --- #
#cursor.execute('''
#DROP TABLE books
#''')

cursor.execute('''
DROP TABLE booksV
''')

# Use cursor to create table
cursor.execute('''
    Create TABLE books(id INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT, Author TEXT, Qty INTEGER)
 ''')

# Use a list of Tuples to store the list of books and execute many to add to database
books = [
    ('A Tale of Two Cities', 'Charles Dickens', 30), 
    ('Harry Potter and The Philosophers Stone', 'J.K. Rowling', 40),
    ('The Lion, The Witch and The Wardrobe', 'C.S. Lewis', 25),
    ('The Lord Of The Rings', 'J.R.R. Tolkein', 37),
    ('Alice In Wonderland', 'Lewis Carroll', 12),
    ]

# Execute many to add all from books
cursor.executemany('''
    INSERT INTO books(Title, Author, Qty) 
    VALUES(?,?,?)
''',books)

# Commit changes
db.commit()

# Create new Virtual table from current table to use FTS
cursor.execute('''
    CREATE VIRTUAL TABLE booksV
    USING FTS5(id, Title, Author, Qty)
    ''')
    # Copy over table values
cursor.execute('''
    INSERT INTO booksV(id, Title, Author, Qty)
    SELECT id, Title, Author, Qty FROM books;
    ''')
db.commit()

            # ----- [Objects] ----- #
# Book object
class Book:
    '''Book class for storing  information. the ___str___ prints each object
    in a readable format. Each quality has a get function'''
    def __init__(self, id, author, title, qty):
        self.id = id
        self.author = author
        self.title = title
        self.qty = qty
        
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_qty(self):
        return self.qty

    def __str__(self):
        output =  f"\n----- {self.title} -----\n"
        output += f"ID: {self.id}\n"
        output += f"Author: {self.author}\n"
        output += f"Quantity: {self.qty}\n"
        output += "----------------------\n"

        return output


# ----- [Functions] ----- #

# Add New Book
def add_book():
    while True:
        title = input("Enter the Title: ")
        author = input("Etnter the author: ")
        qty = int(input("Enter the amount of stock: "))

        output  = "----- New book -----\n"
        output += f"Title: {title}\n"
        output += f"Author: {author}\n"
        output += f"Stock quantity: {qty}"
        print(output)
    
        while True:
            correct = input("Is the correct? (Y/N)").lower()
            if correct == "y":
                break
            elif correct == "n":
                print("Please re-enter the information.")
                add_book()
            else:
                print("Please select a valid option")
                
        break
    # Insert into database
    cursor.execute('''
    INSERT INTO books(Title, Author, Qty)
    VALUES(?,?,?)''', (title, author, qty))

    # Get ID for user:
    cursor.execute('''
    SELECT MAX(id)
    FROM books 
    ''')
    id = cursor.fetchone()
    # Feedback to console
    print(f'Book added to database, ID: {id[0]}')
    return


# Update book information
def update_book():
     # Select book by id
    while True:
        id= int(input("What is the id of the book you'd like to update?\n"))
        cursor.execute('''
        SELECT id, Author, Title, Qty
        FROM books 
        WHERE id = ?
        ''',(id,))
        result = cursor.fetchone()
        print(result)
        correct = input("Is this the correct book? Y/N: ").lower()
        if correct == 'y':
            break

    # creat an object from data by indexing the tuple
    update_book = Book(result[0], result[1],result[2],result[3])
    print(update_book)
    print("What would you like to update?")
    print('''
    1: Title
    2: Author
    3: Quantity
    ''')

    # Choose and update selection
    while True:
        select = input("")
        if select == "1":
            new_title = input("Enter the new title: ")
            # Update Database
            cursor.execute('''
            UPDATE books
            SET Title = ?
            WHERE id = ?
            ''', (new_title, id))
            break
        elif select == "2":
            new_author = input("Enter the new author: ")
             # Update Database
            cursor.execute('''
            UPDATE books
            SET Author = ?
            WHERE id = ?
            ''', (new_author, id))
            break
        elif select == "3":
            new_qty = int(input("Enter the new quantity: "))
             # Update Database
            cursor.execute('''
            UPDATE books
            SET Qty = ?
            WHERE id = ?
            ''', (new_qty, id))
            break
        else:
            print("Please select a valid option")
    # print output
    print("\n----- Sucessfully Updated -----")
    cursor.execute('''
        SELECT id, Author, Title, Qty
        FROM books 
        WHERE id = ?
        ''',(id,))
    result = cursor.fetchone()
    update_book = Book(result[0], result[1],result[2],result[3])
    print(update_book)

# Delete book
def delete_book():
    # Select book by id
    while True:
        id= int(input("What is the id of the book you'd like to update?\n"))
        cursor.execute('''
        SELECT id, Author, Title, Qty
        FROM books 
        WHERE id = ?
        ''',(id,))
        result = cursor.fetchone()
        # create an object from data by indexing the tuple
        delete_book = Book(result[0], result[1],result[2],result[3])
        print(delete_book)
        correct = input("Is this the correct book for deletion? Y/N: ").lower()
        if correct == 'y':       
            cursor.execute('''
            DELETE FROM books
            WHERE  id = ?
            ''',(id,))
            print("\n ----- BOOK DELETED ----- \n")
            return
  


    
    
    # Remove from database and print notice to console

# Search for a specific book
def search_book():
    # Ask for a search phrase
    phrase = input("Enter search phrase: ")
    cursor.execute('''
    SELECT *
    FROM booksV
    WHERE booksV MATCH ?
    ''',(phrase,))
    # Return book and print to console in a visually clear way (book object)
    result = cursor.fetchone()
    print(result)


# ----- [Menu and console display] ----- #
print (book_art)
# menu
menu = '''
1. Enter Book
2. Update Book
3. Delete Book
4. Search Books
0. Exit
'''

while True:
    print(menu)

    selection = input("Choose an option from above: ")

    if selection == "0":
        print("Goodbye")
        break

    elif selection == "1":
        print("Enter a new book") # TODO!
        add_book()
    
    elif selection == "2":
        print("Update a book") # TODO!
        update_book()
    
    elif selection == "3":
        print("Delete a book") # TODO!
        delete_book()

    elif selection == "4":
        search_book()

        print("Search Books") # TODO!
    # Catchall for invalid selection
    else:
        print("Please choose a valid option")