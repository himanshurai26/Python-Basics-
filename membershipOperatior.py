# Membership Operators in python

num = [10,3,23,45,12,76,33]
print(3 in num) # return true if present
print(3 not in num) # return false if present

student = {"name": "Ram", "age": 20}

print("name" in student)  # True
print("Ram" in student)  # False
print("Ram" in student.values())  # True

subjects = ["hindi", "English", "Math", "science", "cs"]

subject = input("Please enter a subject: ")

if subject in subjects:
    print(f"{subject} are present in subjects")
else:
    print(f"{subject} is not present in subjects")