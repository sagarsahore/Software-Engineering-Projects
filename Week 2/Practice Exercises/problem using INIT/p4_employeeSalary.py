""""
### : **Employee Salary**

Create a class called `Employee` with the following:

- An `__init__` method that initializes the employee's name, position, and salary.
- A method `give_raise(percentage)` that increases the employee's salary by a percentage.
- A method `display_salary()` that prints the current salary of the employee.
- Create an employee object, give them a raise, and display the updated salary.

"""

# Employee Salary Management System

class Employee:

    def __init__(self, name, position, salary):  # Constructor to initialize the number
        self.position = position
        self.salary = salary
        self.name = name

    def give_raise(self, percentage):  # Raise method : we use self to access object variables we are working with
        print("Current salary:", self.salary)
        salaryRaise = self.salary * (percentage / 100)
        self.salary += salaryRaise
        print("Salary raised by:", salaryRaise)
        print("New salary:", self.salary)

    def display_salary(self):
        print("Employee Name:", self.name)
        print("Position:", self.position)
        print("Current Salary:", self.salary)


# Create an instance of the Employee class
employee1 = Employee("John Doe", "Software Engineer", 60000)  # Create an instance of the Employee class

employeeRaise = float(input("Enter the percentage raise: "))
employee1.give_raise(employeeRaise)
employee1.display_salary()  # Call the display_salary method to show the result
    