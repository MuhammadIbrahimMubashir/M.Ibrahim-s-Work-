import json

# Load books from file
def load_books():
    try:
        with open("library.txt", "r") as file:
            return json.load(file)
    except:
        return []

# Save books to file
def save_books(books):
    with open("library.txt", "w") as file:
        json.dump(books, file, indent=4)

# Add a book
def add_book(books):
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")
    genre = input("Genre: ")
    read = input("Read? (yes/no): ") == "yes"
    books.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
    print("Book added!\n")

# Remove a book
def remove_book(books):
    title = input("Title to remove: ")
    books[:] = [b for b in books if b["title"].lower() != title.lower()]
    print("Book removed!\n")

# Search for a book
def search_book(books):
    keyword = input("Search title or author: ").lower()
    for b in books:
        if keyword in b["title"].lower() or keyword in b["author"].lower():
            print(f"{b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {'Read' if b['read'] else 'Unread'}")
    print()

# Show all books
def show_books(books):
    if not books:
        print("No books!\n")
        return
    for b in books:
        print(f"{b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {'Read' if b['read'] else 'Unread'}")
    print()

# Show statistics
def show_stats(books):
    total = len(books)
    read = sum(1 for b in books if b["read"])
    print(f"Total books: {total}\nRead: {read} ({(read/total*100) if total else 0:.1f}%)\n")

# Main menu
def main():
    books = load_books()
    while True:
        print("1. Add book\n2. Remove book\n3. Search book\n4. Show books\n5. Show stats\n6. Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_book(books)
        elif choice == "2":
            remove_book(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            show_books(books)
        elif choice == "5":
            show_stats(books)
        elif choice == "6":
            save_books(books)
            print("Saved! Bye!")
            break
        else:
            print("Invalid! Try again.\n")

if __name__ == "__main__":
    main()
