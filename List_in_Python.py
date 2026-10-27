#Basic Syntax
from MultipleValue import fruits

list1 = [1,2,3,4,5,6]
print(list1)

# Creating lists with different data types

#list of integer
numbers = [1,2,3,4,5,6]

#List of string
names = ["Himanshu", "Priynashu", "Ybk"]

print(numbers)
print(names)

#creating empty list
a = []
b = list()
print(a)
print(b)

# adding  item in empty list

a.append("Himanshu")
a.append("Kumar")
print(a)

# creating list using list function
# the list() function can convert an iterable , such as string or tupple into a list

letter1 = list("Himanshu")
print(letter1)

#coverting a tupple
values = list((1,3,4,5,6))
print(values)

#creating list using repeatation
list2 = [1]*5
print(list2)

# count the number of items
print(len(list2))

# Negative indexing in list
#-1 means the last item

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
print(fruits[1])


# Slicing in python lists
# slicing means extracting a portion of a list

print(fruits[1:3])

num1 = [1,2,3,4,5,6,8,9,0,3]
print(num1)
print(num1[2:4])
print(num1[:2]) # from starting to given index
print(num1[2:])

#Using the step parameter

print("step parameter",num1[3::])

# replacing multiple items with slicing

num1[1:3] = [200,300]
print(num1)


# slicing can also delete a range of items

del num1[1:3]
print(num1)

# apped can add only one item where extend can add multiple iten

num1.extend([3,4,5,3]);
print(num1)

# Unlike append(), extend() adds the individual items from an iterable

a  = [2,6,4]
a.append([4,5,6])
print(a)

a.extend([7,8,9])
print(a)

# insert() - add an item at a speciific

num1.insert(1,10)
print(num1)

# remove by value

num1.remove(10)
print(num1)
print(num1.pop(1))
print(num1)

# Clear - remove all items

numbers = [1,2,3,4,5,6]
numbers.clear()
print(numbers)

#String formating

name = "Himanshu"
age = 24

print(f"My name is {name} and I am {age} years old")
a = 5
b = 6

print(f"The sum of the number is {a + b} ")

age = 23
print("The sum of the number is " + str(age))

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"My name is {name} and I am {age} years old")

tx1 = "My name Is Himanshu Kumar \"Learning python\""
print(tx1)