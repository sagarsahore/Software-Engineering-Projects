#Activity 2 : find the factorial of a number using recussion and iteration
num1= int(input("Enter a number to find its factorial: "))
# Recursive function to calculate factorial
def factorial(num1):
        result = 1 # initialized before the loop to store the product.
        for i in range (1,num1+1):
              result *= i
        return result
print("Factorial of", num1, "is", factorial(num1))