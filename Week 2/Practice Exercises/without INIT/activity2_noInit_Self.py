def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def display(num):
    print("Factorial of", num, "is", factorial(num))
    if check_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

# Call display with a number
display(10)
# Call display with a number
display(5)