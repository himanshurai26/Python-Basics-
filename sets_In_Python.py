# set is a cleection with these important properties
'''Unordered: Items do not have a fixed position or guaranteed order.
Unique: Duplicate values are automatically removed.
Mutable: You can add or remove items after creating a set.
Unindexed: You cannot access elements using positions such as my_set[0].
Multiple data types: A set can contain integers, strings, floats, and other hashable objects'''

numbers = {10,30,40,10,90,100,80,90,100}
numbers.remove(90)
print(numbers)
print(type(numbers))

#Method 2 using set

num = set([3,5,6,7,8])
print(num)

# converting tuple into set

set1 = [3,5,6,8,4,2]

temp = set(set1)
print(temp)

a ={}   # Empty dictionary
print(type(a))

b = set() # empty set
print(type(b))

# set can contain different data types

data = {10, 3.14, "Python", True}
print(data)

value = {1,1.0, True} # all are equal in set no duplicate allow
print(value)

num1 = {20,30,10}
num1.update((40,50,60,70))
print(num1)

# pop in set

result = num1.pop()
print(result)
print(num1)