# Converting User input into different data types
from email import message

#A) Covert to integer using int()

age = int(input("Enter your age"))
print(age)
print(type(age))

#B) Convert to float using float()

price = float(input("Enter your price"))
print(price)
print(type(price))

#C covert to string

age = 20;

mess =  "My age is "  +str(age)
print(mess)

#D covert to boolean

x = bool(input("Enter a boolean"))
print(x)