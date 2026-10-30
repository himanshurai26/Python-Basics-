#tuple uses parentheses ()

numbers = (10,20,30,4,20)
print(numbers)
name = ("Himanshu ", "xyz", "Raja", "ABC")
print(name)
print(name[0])

#tuple without parentheses

t1 = 30,2,4,2,5,3
print(t1)
print(type(t1))

num1 = (10,20,30,40,30,36)

temp = list(num1)
temp[1] = 65
print(temp)
numbers = tuple(temp)
print(numbers)

#Finding the length, minimum , maximum and sum

numbers = (10,20,30,40,30,36)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

#to get tuple

result = tuple(sorted(numbers))
print(result)

#loop through tuple

for number in numbers:
    print(numbers)

for i in range(len(numbers)):
    print(numbers[i])

