#Python has the following data types built-in by default:
'''
Text    :   str
Numeric :   int, float, complex
Sequence:   list, tuple, range
Mapping :   dict
Set     :   set, frozenset
Boolean :   bool
Binary  :   bytes, bytearray, memoryview
None    :   None
'''
#To get the datatype of any object using type() function:
x = 5
print(type(x))

a = "Hello World"
print(type(a)) #string

b = 20
print(type(b)) #integer

c = 20.75
print(type(c)) #float

d = 2j
print(type(d)) #complex

fruits = ["apple", "banana", "cherry"]
print(type(fruits)) #list

movies = ("dil", "sye", "heart attack")
print(type(movies)) #tuple

e = range(5)
print(type(e)) #range

data = {"name" : "John", "age" : 36}
print(type(data)) #dictionary

devices = {"mobile", "laptop", "printer", "dishwasher"}
print(type(devices)) #set

devices1 = ({"mobile", "laptop", "printer", "dishwasher"})
print(type(devices1)) #frozenset

f = True
print(type(f)) #boolean

g = b"Hello"
print(type(g)) #bytes

h = bytearray(5)
print(type(h)) #bytearray

i = memoryview(bytes(5))
print(type(i)) #memoryview

j = None
print(type(j)) #Nonetype



#To specify the data type
a = str("Hello World")
b = int(20)
c = float(20.75)
d = complex(2j)
fruits = list(("apple", "banana", "cherry"))
movies = tuple(("dil", "sye", "heart attack"))
e = range(5)
data = dict({"name" : "John", "age" : 36})
devices = set(("mobile", "laptop", "printer", "dishwasher"))
devices1 = frozenset(("mobile", "laptop", "printer", "dishwasher"))
f = bool(5)
g = bytes(6)
h = bytearray(5)
i = memoryview(bytes(5))
