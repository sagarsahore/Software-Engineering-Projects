#Activity 1: Write a code to use round , abs and square functions to calculate the 
# area of a rectangle land try to use both Jupyter Notebook and Py
 

length = 24.45
breadth = 20.47
area = length * breadth; 

 # Round area to 2 decimal places
area = round(area, 2)

print("Area of rectangle is: ", area)
# Output: Area of rectangle is: 50.0

# Area of rectangle using round functiton with 4 decimals
area = round(length * breadth, 4)
print("Area of rectangle with 4 decimals is : ", area)

# area of rectangle using
length_sq = round(length ** 2, 2)
breadth_sq = round(pow(breadth, 2), 2)

# Display the results
print(f"Length squared: {length_sq}")
print(f"breadth squared: {breadth_sq}")