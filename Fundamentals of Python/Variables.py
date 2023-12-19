#Variables are containers for storing data values.
#syntax <variable name> = <value>
#Python uses = to assign values to variables
#There is no need to declare data type in python

#string
v = ("Vamshi")
print(v)

#Integer
a = 2
print(a)

#long integer
b = 234567812345678234567
print(b)

#floating point
pi = 3.14
print(pi)

#Boolean
t = True
print(t)

#Empty value of None Data type
x = None
print(x)


#casting
#If we want to specify the data type of a variable, this can be done with casting.
x = str(3)
y = int(3)
z = float(3)

#You can get the data type of a variable with the type() function.
print(type(x))
print(type(y))
print(type(z))

#Variable names are case-sensitive.
r = 4
R = 16
print(r)
print(R)
#Both are not same


#Variable Names:
#A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume)

#Rules for Python variables:
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.

#Legal Variable Names
myvar = "Vamshi"
my_var = "Vamshi"
_my_var = "Vamshi"
myVar = "Vamshi"
MYVAR = "Vamshi"
myvar2 = "Vamshi"

#Illegal variable names:
#These give error

#2myvar = "Vamshi"
#my-var = "Vamshi"
#my var = "Vamshi"


#Multi Words Variable Names
#Variable names with more than one word can be difficult to read.
#Techniques you can use to make them more readable:

#Camel Case
#Each word, except the first, starts with a capital letter:
myVariableName = "John"

#Pascal Case
#Each word starts with a capital letter:
MyVariableName = "John"

#Snake Case
#Each word is separated by an underscore character:
my_variable_name = "John"



#Assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Note: Make sure the number of variables matches the number of values, or else you will get an error.

#One Value to Multiple Variables
#we can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
#If you have a collection of values in a list, tuple etc.
#Python allows you to extract the values into variables
#This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
print(x + y)
#it will give error

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)

#You can change the value of a variable in your program at any time.
#Python will always keep track of its current value.
reply = ("No! I can't")
print(reply)
reply = ("Yes I can")
print(reply)

