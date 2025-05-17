"""
# This script demonstrates the use of list comprehensions and dictionary comprehensions in Python."""

#Transforming Lists into a Dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {key : value for key, value in zip(keys, values)}
print(dictionary)


# Merging Dictionaries with the Double Asterisk Operator
# the double asterick(**) is used to unpack the contents of the dictionary into a new dictionary


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 ={ 'e': 3, 'f': 4}

merged_dict = {**dict1, **dict2, **dict3}
print(merged_dict)


#Merging the Dictionaries with the condition

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'e': 5}

merged_dict= {**{k:v for k, v in dict1.items() if k in 'aeiou'}, **{k:v for k, v in dict2.items() if k in 'aeiou'}}
print(merged_dict)

'''want to only take vowel keys 'aeiou'
You ignore non-vowel keys and only keep vowel keys when combining'''

#Underscore in the Dictionary
# The underscore is used to indicate that the variable is not going to be used

x, y, _ = (1, 2, "ignore me")
x,y


# ebumerate() function
# The enumerate() function adds a counter to an iterable and returns it in the form of an enumerate object.
# enumerate() is like being in a ranking drill where you get both the player's number and their name at the same time.
" Tells you each striker’s position and name — like a coach calling out your rank with your name."

players = ['Isagi', 'Bachira', 'Nagi']
for i,player in enumerate(players):
    print(i, player)