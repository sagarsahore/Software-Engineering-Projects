class Factorial:
    def __init__(self, num1):  # Constructor to initialize the number
        self.num1 = num1
    
    def factorial(self):  # Factorial method now works with self.num1
        result = 1  # Initialized before the loop to store the product.
        for i in range(1, self.num1 + 1):
            result *= i
        return result
        
    def display(self):  # Display method corrected
        print("Factorial of", self.num1, "is", self.factorial())

# Instantiate the class with number 5
number1 = Factorial(5)

# Call the display method to show the result
number1.display()