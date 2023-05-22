library = {}

def add_book():
    title, genre, price = input("Enter book information (title|genre|price): ").split("|")
    library[title] = {"genre": genre, "price": price}
    print(f"{title} has been added to the library.")

def remove_book():
    title = input("Enter the title of the book you want to remove: ")
    if title in library:
        del library[title]
        print(f"{title} has been removed from the library.")
    else:
        print(f"Error: {title} not found in library.")

def get_book_info():
    title = input("Enter the title of the book you want to get information about: ")
    if title in library:
        genre = library[title]["genre"]
        price = library[title]["price"]
        print(f"Title: {title}\nGenre: {genre}\nPrice: {price}")
    else:
        print(f"Error: {title} not found in library.")

def list_all_books():
    if len(library) == 0:
        print("Library is empty.")
    else:
        sorted_books = sorted(library.items(), key=lambda x: x[0])
        print("All books in the library:")
        for title, info in sorted_books:
            genre = info["genre"]
            price = info["price"]
            print(f"Title: {title}\nGenre: {genre}\nPrice: {price}\n")

def list_books_by_genre():
    genre = input("Enter the genre of the books you want to list: ")
    books = [title for title, info in library.items() if info["genre"] == genre]
    if len(books) == 0:
        print(f"No books found in the {genre} genre.")
    else:
        books.sort()
        print(f"All books in the {genre} genre:")
        for title in books:
            price = library[title]["price"]
            print(f"Title: {title}\nPrice: {price}\n")
while True:
    print("Menu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Get book information")
    print("4. List all books")
    print("5. List books by genre")
    print("6. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_all_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")