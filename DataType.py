# Python Data Types

# Setting the data type
# In python , the data is set when you assign a value to a variable
x  = 5
print(x)
print(type(x))
x = "Himanshu Kumar"
print(x)
print(type(x))

x = 4.2
print(x)
print(type(x))

x = 1j
print(x)
print(type(x))

# A list is a data type used to store multiple items in a single variable
# A list contain number , strings, or even different data type
x = ["Himanshu", "Priyanshu", "Ujjwal"]
print(x)
print(type(x))

my_list = [10, "Himanshu", 34.5, True]
print(my_list)
print(type(my_list))
print(my_list[0])
print(type(my_list[0]))
print(my_list[1])
print(type(my_list[1]))

for item in my_list:
    print(item, type(item))

# list contain another list
data = ["13", 4, "Himanshu", [5, "Kumar"], 4]
data[0] = "Change"
print(data)
print(data[3])


# A tuple in Python is a collection of items that is ordered and cannot be changed
# after creation. It is similar to a list, but the main difference is that a tuple is immutable

my_tuple = (10, "Himanshu", 34.5, True)
#my_tuple[0] = "Change"
print(my_tuple)
print(my_tuple)
print(my_tuple[0])

t = (10, 20, 30)
print(t)
t = (100, 200, 300)

print(t)