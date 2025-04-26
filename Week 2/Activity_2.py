#Activity 2 : find the factorial of a number using recussion and iteration
num1= int(input("Enter a number to find its factorial: "))
# Recursive function to calculate factorial
def factorial(num1):
        result = 1 # initialized before the loop to store the product.
        for i in range (1,num1+1):
              result *= i
        return result
print("Factorial of", num1, "is", factorial(num1))


# Chat Gpt code and defination for recursion 

# ✅ Function: Calculates factorial using recursion
def factorial(n):
    # ✅ BEST PRACTICE: Always define a base case to prevent infinite recursion
    if n == 1:
        return 1
    else:
        # 🔁 Recursive Step: Reduce the problem by calling factorial on (n - 1)
        return n * factorial(n - 1)

# 📌 Step 1: Get input from user
# BEST PRACTICE: Validate input and use descriptive variable names
try:
    num = int(input("Enter a number to find its factorial: "))  # Get user input and convert to integer

    # 🚧 Check if input is valid (factorial only works for integers >= 1)
    if num < 1:
        print("❌ Factorial is not defined for numbers less than 1.")
    else:
        # ✅ Step 2: Call the function and print the result
        print(f"✔️ Factorial of {num} is {factorial(num)}")
except ValueError:
    # 💡 BEST PRACTICE: Always handle unexpected input with try-except
    print("❌ Invalid input! Please enter a positive integer.")
