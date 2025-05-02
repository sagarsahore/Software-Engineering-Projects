"""/* ### Problem 3: **Student Grades**

Create a class called `Student` that:

- Has attributes `name` and `grades` (a list of integers representing the grades)
- Has a method `calculate_average()` that returns the average of the grades
- Has a method `display_info()` that prints the student's name and their average grade

Use `self` to calculate the average based on the grades stored for each object */"""


# Student Grades Management System

class Student:
    def __init__(self, name, grades):  # Constructor to initialize the number
        self.name = name
        self.grades = grades  # A list of integers representing the grades
    
    def calcualte_average(self):
        length = len(self.grades)
        total = sum(self.grades)  # Sum of all grades

        if length == 0:
            return 0  # Avoid division by zero if no grades are present
        # Calculate average
        average = total/length  # Calculate average
        return average  # can do using if else as well but will be lengthy hence this efficient way
    
    def display_info(self):
        average = self.calcualte_average()
        print("Student Name:", self.name)
        print("Average Grade:", average)

sage = Student("Sage", [90, 90, 90, 90, 90])  # Create an instance of the Student class
sage.display_info()  # Call the display_info method to show the result