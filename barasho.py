# import random
# print(random.randint(0, 100))

# """
# ##Day 2 24 Jan
# # Python Syntax

# print("Hello, Fr oz")

# print("djfdf")

# # Python Indentation

# # problem 1
# if 5 > 2:
#     print("Five is greater than two!")

# # problem 2
# if 5 > 2:
#  print("Five is greater than two!")
# if 5 > 2:
#         print("Five is greater than two!")

# # Day 3 26/01/23
# # Comments

# print("comment")
# print("comment2") #this is an example of commments

# """

# ##Day 4 27/01/2023
# """
# # Variables

# x = 5 # 5 is int (integer)
# print(x)

# xx = "albashiiri" # albashiiri is str (string)
# print(xx)

# z = float(5)
# print(z)

# """

#   ## Casting

# #example 1
# a = str(100)
# b = int(100)
# c = float(100)
# print(a, b, c)

# #example 2

# h = 10
# i = "frozenset"
# j = 1.3
# print(type(h))
# print(type(i))
# print(type(j))

#  # single or double qoutes

# l = "froz1"
# k = 'froz2'
# print(l, k)

#  #Case-Sensitive
# q = 1
# Q = 4
# print(q, Q)

# T = 9
# T = "sally"
# print(T, T)

#  #variable names

#  #legal variable names
# myvar = "Bulbeni"
# my_var = "Bulbeni"
# _my_var = "Bulbeni"
# myVar = "Bulbeni"
# MYVAR1 = "e"
# myvar2 = "d"
# print(myvar2)

#  #illegal variable names
# """
# 2myvar = "Bulbeni"
# my-var = "Bulbeni"
# my var = "Bulbeni"
# """
#  #Multi Words Variable Names
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# #One Value to Multiple Variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# #Unpack a Collection
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
"""

## 06/02/2023
### Output Variables


#The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

#In the print() function, you output multiple variables, separated by a comma:
x = "c++"
y = "is"
z = "awesome"
print(x, y, z)

#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
x = "Python"
y = "is"
z = "awesome"
print(x + y + z) #You can also use the + operator to output multiple variables:

#example
x = "Machine learning "
y = "will "
z = "be awesome"
print(x + y + z) #You can also use the + operator to output multiple variables:

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error: here is example
x = 5
y = "Bulbeni"
#print(x + y) # this is an error

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "Bulbeni"
print(x, y)



#07/02/2023

#Global Variables

  ##Variables that are created outside of a function (as in all of the examples above) are known as global variables.

  #Global variables can be used by everyone, both inside of functions and outside.

x = "aminakoyum"

def myfunc():
  print("froz " + x)

myfunc()
#example 2

y = "tusaale"

def froz0():
  print("sikerim seni " + y)

froz0()

#problem2

#Create a variable inside a function, with the same name as the global variable

W = "albashiiri"

def myfunc():
  w = "saalah"
  print("Python is " + w) #If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

myfunc()

print("Python is " + W)

#The global Keyword

#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

def syntax9():
  global M
  M = 7 + 3

syntax9()
print(M)





#Also, use the global keyword if you want to change a global variable inside a function.

x = "casiir"

def myfunc():
  global x
  x = "caano"

myfunc()

x = "casiir"
x = "four"
print(x)
 




# print("hilib " + x) #To change the value of a global variable inside a function, refer to the variable by using the global keyword:



#09/02/2023
# Data types

#Built-in Data Types
#In programming, data type is an important concept. Variables can store data of different types, and different types can do different things.

#python has the following data types built-in by default, in these categories:

x = 5 
print(x)
print(type(x))


# Text Type:    str
A = "froz" 
print(A)
print(type(A))


# Numeric Types:    int, float, complex
#integer
B = 5 
print(B)
print(type(B))

# float
C = 5.3
print(C)
print(type(C))

#complex
D = 5j
print(D)
print(type(D))


# Sequence Types:    list, tuple, range
#list
E = ["albashiiri", "froz", "qowle"]
print(E)
print(type(E))

#tuple
F = ("albashiiri", "froz", "qowle") 
print(F)
print(type(F))

#range
H = range(5)
print(H)
print(type(H))

# Mapping Type:    dict

I = {"name" : "John", "age" : 36} 
print(I)
print(type(I))


# Set Types:    set, frozenset
#set
J = {"albashiiri", "froz", "qowle"} 
print(J)
print(type(J))

#frozenset
K = frozenset({"albashiiri", "froz", "qowle"}) 
print(K)
print(type(K))

# Boolean Type:    bool
#bool
L = True
print(L)
print(type(L))

# Binary Types:    bytes, bytearray, memoryview
#bytes
L = b"Hello qowle"
print(L)
print(type(L))

#bytearray
M = bytearray(7)
print(M)
print(type(M))

#memoryview
N = memoryview(bytes(5))
print(M)
print(type(N))

# None Type:    NoneType
O = None
print(O)
print(type(O))


# continue 10/02/2023

#Setting the Specific Data Type
## Text Type:    str
#str
a = str("feo<")
print(a)

#integer
b = int(9)
print(b)

c = float(10.5)
print(c)

d = complex(87j)
print(d)

e = list(("tufaax", "moos", "cherry"))
print(e)

f = tuple(("tufaax", "moos", "cherry"))
print(f)

g = range(5)
print(g)

h = dict(name="Qowle", age=100)
print(h)

i = set(("basal", "baradho", "yaanyo"))
print(i)

j = frozenset(("GAare", "bana", "crry"))
print(j)

k = bool(32)
print(k)

l = bytes(60)
print(l)

m = bytearray(2)
print(m)

n = memoryview(bytes(15))
print(n)
"""

# 13/02/2023
#Python numbers

#integer
o = 35656222554887711
print(o)

#Float
p  = 9.7639
print(p)

# Float can also be scientific numbers with an "e" to indicate the power of 10.
# e qiimaheeda waa 10 yacni, 5e1 = 5 * 10 waanna 50. mar walba e waxa ka dambeeya tirada ey tahay baa zero u xisaabin. tusaale 1e4 waa (1*10000 = 10000)
#float power
p2 = 5e8 #500000000
print(p2)

#complex
q = 234.5j
print(q)

#Type Conversion
#convert from int to float:

r = float(10)
print(r)

# convert float to complex

s = complex(29.44)
print(s)

# Random Number

# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

#Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(5, 18944))
