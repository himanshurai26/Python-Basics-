#Tuple unpacking means assigning the element of a tuple to variables in a single statement

student = ("Himanshu", 3, "Python", "Msc")

name, roll_number, subject, degree = student

print(name, roll_number, subject, degree)

# example -> * in the tuple unpacking
# the * operator collects multiple remaining elements into a list

numbers = [1, 2, 3, 4, 5]

first, *second, third = numbers
print(first, second, third)
