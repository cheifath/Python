# print() in pyhthon
print("Hello World!")
print(5)
print("Add", 5)
print(10 * 5)
print("Hello \"Rayan\"\nHow are you today?")
print("Hello", 6 , 7, sep="---", end="000\n")
print("", "Success", sep="---", end="---\n")
print("", "in", "progress", sep="---", end="---\n")

# comments in pyhton
# "#" is used for single line comments
""" this is multi line comment
we can use """" or ''' for multi line comments """

# variables and datatypes in python
# variables, 
num = 123
isTrue = True
name = "Rayan"
nothing = None

print(type(num), type(isTrue), type(name), type(nothing))

print("value of num is: ", num)
print("value of isTrue is: ", isTrue)
print("value of name is: ", name)
print("value of nothing is: ", nothing)

complexNum = 8 +2j
print(type(complexNum))

# type casting
num = str(num)
print(type(num))

num = int(num)
print(type(num))

num = float(num)
print(type(num))

# concatenation -- only same type of data can be concatenated else we need to type cast
name = name + "Sir"
print(name)

name = name + str(404)
print(name)

# introduction to list, tuple, set, dictionary
# list 
''' A list is a sequence of values. The values can be of any type, and it can contain another list inside
of set each value is called an element.
Ex: list2 = [["Apple", "Orange"], 1, [1, 2, 3], "Rayan"] '''

list1 = [1, 2, 3, 4, 5]
print(list1)

# tuple
''' A tuple is a sequence of values much like a list but they are immutable means the value cannot be changed.
The values stored in a tuple can be of any type and they are indexed by integers.'''
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)

# set
''' In Python, a set is an unordered collection of unique elements.
Sets are defined using curly braces {} or the set() function.'''
set1 = {1, 2, 3, 4, 5}
print(set1)

# dictionary
''' A dicationary is an unordered collection of key-value pairs.
Each key is separated from its value by a colon (:),'''
dict1 = {"name": "Rayan", "age": 25, "mark": 900}
print(dict1)
