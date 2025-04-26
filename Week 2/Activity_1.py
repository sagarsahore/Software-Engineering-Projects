#Activity 1: Write a code to use round , abs and square functions to calculate the 
# area of a rectangle land try to use both Jupyter Notebook and Py

def square(x):
    return x ** 2  

# Get user input for dimensions
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Ensure positive dimensions using abs
length = abs(length)
breadth = abs(breadth)

# Calculate area
area = length * breadth

# Round area to 2 and 4 decimal places
area_2dp = round(area, 2)
area_4dp = round(area, 4)

# Calculate and round squared values
length_sq = round(square(length), 2)
breadth_sq = round(square(breadth), 2)

# Output
print("\n✅ Rectangle Calculation Summary:")
print(f"Length: {length}, Breadth: {breadth}")
print(f"Area (2 decimals): {area_2dp}")
print(f"Area (4 decimals): {area_4dp}")
print(f"Length squared: {length_sq}")
print(f"Breadth squared: {breadth_sq}")

#professor's code
num1, num2 = input("Enter two numbers separated by a space: ").split()
num1 = float(num1)
num2 = float(num2)
def area(num1, num2):
    Area_land = num1 * num2
    print("Area of land:", Area_land)
    return Area_land