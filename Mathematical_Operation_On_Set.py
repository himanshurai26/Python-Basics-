A = {1,2,3,4,5}
B = (3,4,6,7,8)

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

num1 = {1,2,3,4,5,6,7,8,9}
num2 = {3,4,5,6,7,9}

print(num2.issubset(num1))
print(num2 <= num1)
print(num1.issuperset(num2))


square = {x**2 for x in range(10)}
square1 = {x**2 for x in range(1,11) if x % 2 == 0}
print(square1)

names = {"Himanshu", "Raja", "Priyanshu"}
update_name = {name.upper() for name in names}
print(update_name)

