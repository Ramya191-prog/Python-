# declaring the int,float,complex variables
x = 123     #x is of type int
y=10.234    #x is of type float
z=3j        #x is of type complex

print(x)
print(y)
print(z)

# declaring String variables
x1="ABC"    #x is of type String

print(x)


#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

#Get the Type with  type() function
x = 5
y = "Python"
print(type(x))
print(type(y))

#Single or Double Quotes
x = "John"
print(x)

x = 'John'      # is the same as above
print(x)

#Case-Sensitive
a = 4
A = "Sally"     #A will not overwrite a


#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python - Output Variables
x = "Python is awesome"
print(x)

#print() function
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# + operator to output multiple variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

#Local Variables,Global 

x = "awesome"    #outside function

def myfunc():
  x = "fantastic"
  print("Python is " + x)   #inside function
myfunc()

print("Python is " + x)

#The global Keyword
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

#changing a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)