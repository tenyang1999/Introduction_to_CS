library = {}

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """
    # your code here
    title, genre, price = input("Enter the title, genre, and price of the book (separated bt |): ").split("|")
    library[title] = genre, float(price)
    print('Added %s to the library'%(title) )
    return True
    

def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    
    # your code here
    book_title = input("Enter the title of the book to remove: ")
    try:
       del library[book_title]
       return True
    except KeyError:
        print("Error: %s not found in the library" %(book_title))  


def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    # your code here
    book_title = input("Enter the title of the book: ")
    try:
        genre, price = library[book_title] 
        print("Title: ", book_title)
        print("Genre: ", genre)
        print("Price: ", price)
    except:
        print("Error: %s not found in the library" %(book_title))    

def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("%s (%s, $%.2f)" % (title, genre, price))
    print()
    return True

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    
    # your code here
    book_genre = input("Enter the genre to search for: ")
    cnt = 0
    for title, (genre, price) in sorted(library.items()):
        if genre == book_genre:
            print("%s (%s, $%.2f)" % (title, genre, price))
            cnt +=1
    if cnt == 0:
        print("No books found in the %s genre." % book_genre)

while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")

