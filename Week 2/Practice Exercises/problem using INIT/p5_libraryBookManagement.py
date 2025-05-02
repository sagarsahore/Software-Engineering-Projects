"""
### **Library Book Management**

Create a class called `Book` that:

- Has attributes `title`, `author`, and `status` (whether the book is available or checked out).
- Has a method `checkout()` that sets the status to "Checked out".
- Has a method `return_book()` that sets the status to "Available".
- Has a method `display_status()` that prints the current status of the book.
"""

# Library Book Management System

class Book:
    def __init__ (self, title, author, status):
        self.title = title
        self.author = author
        self.status = status  # Default status is "Available"

    def checkout(self):
        if self.status == "Available":
            self.status = "Checked out"
            print(f"The book '{self.title}' has been checked out.")
        else:
            print(f"The book '{self.title}' is already checked out.")  

    def return_book(self):
        if self.status == "Checked out":
            self.status = "Available"
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' is already available.")

    def display_status(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.status}") 

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald" , "Checked out")  # Create an instance of the Book class
book1.checkout()  # Check out the book
book1.display_status()  # Display the initial status of the book    