'''
Zip function
-----------------
It pairs items from two (or more) lists based on their position in the list.
Use Case	Example
-> Match related data	Names + ages, players + stats
-> Loop through multiple lists at once	Avoid range(len(...))
-> Creating dictionaries	dict(zip(keys, values))
'''

names = ['Alice', 'Bob', 'Chathy']
ages = [25, 30, 35]
paired = list(zip(names, ages))
print(paired)

#convert lists of tuples to dictioary
fruits_counts = dict(zip(names, ages))
print(fruits_counts)

#aligns with the length of the shortest iterable
ids = [1, 2, 3, 4]
names = ['Alice', 'Bob', 'Chathy','David']
grades = ['A', 'B', 'A','C','F']
students = list(zip(ids, names, grades))
print(students)
students_dict = {id : {names, grades} for id, names, grades in students}
print(students_dict)