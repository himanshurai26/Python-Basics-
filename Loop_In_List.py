# using for loop
from re import search

cars = ["honda", "audi", "bmw"]
for car in cars:
    print(car)

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    print(number *2)

    for number in numbers:
        if number % 2 == 0:
            print("Numbers", number, "is even")
        else:
            print("Numbers", number, "is odd")

#looping through a list using indexes

fruit = ["apple", "banana", "cherry"]
for i in range (len(fruit)):
    print(i, fruit[i])

# looping through indesx in reverse

numbers = [1, 2, 3, 4, 5, 6]
for i in range (len(numbers) -1,-1,-1):
    numbers[i] *= 2
    print(numbers[i])


number1 = [1, 2, 3, 4, 5, 6]
target = 50;

for number in number1:
     if number == target:
         print( "is found in list ")
         break
else:
         print( "is not found in list ")

numbers = [10, 20, 30, 40]

target = 50

for number in numbers:
    if number == target:
        print("Number found")
        break
else:
        print("Number not found")