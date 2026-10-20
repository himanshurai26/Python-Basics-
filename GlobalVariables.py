# Variable that are created outside of a function are known as global variables
# global variables can  be used by everyone, both inside of function and outside

x = "Danger"

def myfuc():
    print("I am in " + x)

myfuc()



# if you create a variable with the same name inside a function.
# this variable will be local. and can only be used inside the function.
# The global variable with the same name will remain as it was
#global and with the orignal value

x = "Himanshu"

def myfuc():

    x = "Raja"
    print("My name is " + x)

myfuc()

print("My name is " + x)

# The Global Keyword
#-> normally , when you create a variable inside a function, that variable is loca
#and can only be used inside that function
# to create a global variable inside a function, you can use the global keyword

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
