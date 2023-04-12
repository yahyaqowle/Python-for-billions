"""
import random

print(random.randint(0, 100))

##Day 2 24 Jan
# Python Syntax

print("Hello, Fr oz")

print("djfdf")

# Python Indentation

# problem 1
if 5 > 2:
  print("Five is greater than two!")

# problem 2
if 5 > 2:
  print("Five is greater than two!")
if 5 > 2:
  print("Five is greater than two!")

# Day 3 26/01/23
# Comments

print("comment")
print("comment2")  #this is an example of commments

##Day 4 27/01/2023

# Variables

x = 5  # 5 is int (integer)
print(x)

xx = "albashiiri"  # albashiiri is str (string)
print(xx)

z = float(5)
print(z)

## Casting

#example 1
a = str(100)
b = int(100)
c = float(100)
print(a, b, c)

#example 2

h = 10
i = "frozenset"
j = 1.3
print(type(h))
print(type(i))
print(type(j))

# single or double qoutes

l = "froz1"
k = 'froz2'
print(l, k)

#Case-Sensitive
q = 1
Q = 4
print(q, Q)

T = 9
T = "sally"
print(T, T)

#variable names

#legal variable names
myvar = "Bulbeni"
my_var = "Bulbeni"
_my_var = "Bulbeni"
myVar = "Bulbeni"
MYVAR1 = "e"
myvar2 = "d"
print(myvar2)

#illegal variable names

# 2myvar = "Bulbeni"
# my-var = "Bulbeni"
# my var = "Bulbeni"

#Multi Words Variable Names
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
print(x + y +
      z)  #You can also use the + operator to output multiple variables:

#example
x = "Machine learning "
y = "will "
z = "be awesome"
print(x + y +
      z)  #You can also use the + operator to output multiple variables:

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
  print(
    "Python is " + w
  )  #If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.


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

I = {"name": "John", "age": 36}
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

# 13/02/2023
#Python numbers

#integer
o = 35656222554887711
print(o)

#Float
p = 9.7639
print(p)

# Float can also be scientific numbers with an "e" to indicate the power of 10.
# e qiimaheeda waa 10 yacni, 5e1 = 5 * 10 waanna 50. mar walba e waxa ka dambeeya tirada ey tahay baa zero u xisaabin. tusaale 1e4 waa (1*10000 = 10000)
#float power
p2 = 5e8  #500000000
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

#14/02/2023
#python casting

#Specify a Variable Type There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

#Casting in python is therefore done using constructor functions:

#int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)

we1 = int(1)  # we1 will be 1
we2 = int(2.8)  # we2 will be 2
we3 = int("3")  # we3 will be 3

print(we1, we2, we3)

#float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

q1 = float(1)  # q1 will be 1.0
q2 = float(2.8)  # q2 will be 2.8
q3 = float("3")  # q3 will be 3.0
q4 = float("4.2")  # q4 will be 4.2

print(q1, q2, q3, q4)

#str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

qq = str("s1")  # qq will be 's1'
qq2 = str(2)  # qq2 will be '2'
qq3 = str(3.0)  # qq3 will be '3.0'

print(qq, qq2, qq3)

#22/02/2023
#python string

print("Hello")
print('Hello')

#Assign String to a Variable

a = "Hefroz"
print(a)

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes:

a = ''''Alleyl dumay albaabadoo laxidhay, uunkoo wada seexday Onkad yeedhay uugaama roob,alif banaadiikh ah Iihdayda bixibaa libaax iman lamoodaaye Raggase adhaxda iyo ooftu waa udub dhexaadkiiye Labadii waxlaga eegijiray waan ka awdnahaye Halkaan aa ka leeyahay Illaah kaliya uun baa og.'''
print(a)

#example 2
#al mutanabi
# e34 = '''ﺍَﻟﺨَﻴﻞُ ﻭَﺍَﻟﻠَﻴﻞُ ﻭَﺍَﻟﺒَﻴﺪَﺍﺀُ ﺗَﻌﺮِﻓُﻨِﻲ ﻭَﺍَﻟﺴَّﻴﻒُ ﻭَﺍَﻟﺮُّﻣﺢُ ﻭَﺍَﻟﻘِﺮﻃَﺎﺱُ ﻭَﺍَﻟﻘَﻠَﻢُ ﺃَﻧَﺎ ﺍَﻟَّﺬِﻱ ﻧَﻈَﺮَ ﺍَﻟﺄَﻋﻤَﻰ ﺇِﻟَﻰ ﺃَﺩَﺑِﻲ  ﻭَﺃَﺳﻤَﻌَﺖ ﻛَﻠِﻤَﺎﺗِﻲ ﻣَﻦ ﺑِﻪُ ﺻَﻤَﻢُ'''
# print(e34)

#Strings are Arrays

bir = "Hello, World!"
print(
  bir[6]
)  # Arrays waa qaabka dhismeedka ay iskugu xigaan qoraalka ama karakterka e.g "hello" H = 0 e =1 l =2 l =3 o=4

#Looping Through a String

for f in "albashiiri":
  print(f)

#String Length

a = "Hello, World!"
print(len(a))

froz03 = "Froz is in the bathroom"
print(len(froz03))

froz04 = "Frois in the bathroom"
print(froz04[3])

#Check String

txt45 = "The best things in life are free!"
print("The" in txt45)

#example 2
txt46 = '''Alleyl dumay albaabadoo laxidhay, uunkoo wada seexday Onkad yeedhay uugaama roob,  
alif banaadiikh ah Iihdayda bixibaa libaax iman lamoodaaye
Raggase adhaxda iyo ooftu waa udub dhexaadkiiye
Labadii waxlaga eegijiray waan ka awdnahaye
Halkaan aa ka leeyahay Illaah kaliya uun baa og'''
print('alif' in txt46)

#example 3
#Use it in an if statement:

txt500 = "Tuugnimo iyo biyo cabis waa khalad!"
if "biyo" in txt500:
  print("Haa, 'biyo xaditaan waa khalad.")
else:
  print("maya waa sax xaditaan")

#Check if NOT
#Check if "expensive" is NOT present in the following text:

txt = "Tuugnimo iyo biyo cabis waa khalad!"
print("iyo" not in txt)

#27/02/203
#Slicing String

#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.

b32 = "Hello, World!"
print(
  b32[2:5])  #Get the characters from position 2 to position 5 (not included):

#Slice From the Start
## By leaving out the start index, the range will start at the first character:

b33 = "Merhaba, Caalam!"
print(
  b33[:5])  #Get the characters from the start to position 5 (not included):

#Slice To the End
##By leaving out the end index, the range will go to the end:

b34 = "Iska wrn, World!"
print(
  b34[2:])  #Get the characters from position 2, and all the way to the end:

#Negative Indexing
#Use negative indexes to start the slice from the end of the string:

# Example
# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

b40 = "Hello, World!"
print(b40[-5:-2])

b55 = "Nabaadina, adduun!"
print(b55[-5:-2])

#Python - Modify Strings

a72 = "merhaba, World!"
print(a72.upper())

a73 = "ola, World!"
print(a73.lower())

#Remove Whitespace
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

#Example
#The strip() method removes any whitespace from the beginning or the end:

a74 = " Hello, World! "
print(a74.strip())  # returns "Hello, World!"

#Replace String

#Example
#The replace() method replaces a string with another string:

a75 = "Hello, World!"
print(a74.replace("H", "J"))

#Split String
#The split() method returns a list where the text between the specified separator becomes the list items.

#Example
#The split() method splits the string into substrings if it finds instances of the separator:

a76 = "Hello, World!"
print(a76.split(","))  # returns ['Hello', ' World!']

#Python - String Concatenation

#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.

#Example
#Merge variable a with variable b into variable c:

a77 = "Hello "
b77 = "Isha baxarka"
c77 = a77 + b77
print(c77)

#Python - Format - Strings

#String Format
#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
'''
age = 36
txt = "My name is John, I am " + age
print(txt) #this is an error = le "main.py", line 629, in <module>
    txt = "My name is John, I am " + age
TypeError: can only concatenate str (not "int") to str
'''

#But we can combine strings and numbers by using the format() method!

#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

#Example
#Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = "Moos iyo cambe"
price = 9.95
myorder = "I want {} pieces of item {} for {} lira."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity2 = 3
itemno2 = 567
price2 = 49.95
myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder2.format(quantity2, itemno2, price2))
"""




#Python - Escape Characters

#Escape Character
#To insert characters that are illegal in a string, use an escape character.

#An escape character is a backslash \ followed by the character you want to insert.

#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

#Example
#You will get an error if you use double quotes inside a string that is surrounded by double quotes:

#txt200 = "We are the so-called "Vikings" from the north." #this an error


#To fix this problem, use the escape character \":
####Note: if you run this txt201 u cant use {triple qoutes} so im Commenting txt201. it shows this error if you run >  ^ SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 15321-15322: truncated \xXX escape

# txt201 = "We are the so-called \"Vikings\" from the north."
# print(txt201)







# Escape Characters
# Other escape characters used in Python:

# Code	Result	Try it
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

# #Exercise
# a = ["Amasya", "Samsun", 'Ankara', "Antalya", "Diyarbakir", "Istanbul"]
# x, y, z, w, q, s = a
# print(x, y, z, w, s)

# a = "Amasya", "Samsun", 'Ankara', "Antalya"
# print(len(a[1:4]))


"""




# 12/03/23
# Python Booleans

# Boolean Values.#Booleans represent one of two values: True or False

# In programming you often need to know if an expression is True or False.

# You can evaluate any expression in Python, and get one of two answers, True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)

# When you run a condition in an if statement, Python returns True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Values and Variables

# The bool() function allows you to evaluate any value, and give you True or False in return,

print(bool("Hello"))

print(bool(15))

# print(bool(0)) #an error the function must have a value

# Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some Values are False

# The following will return False:

# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a _len_ function that returns 0 or False:


class myclass():

  def _len_(self):
    return 0


myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:


def myFunction():
  return True


print(myFunction())

# You can execute code based on the Boolean answer of a function:


def myFunction():
  return True


if myFunction():
  print("YES!")
else:
  print("NO!")

#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))

a = "froz"
print(isinstance(a, str))

#Python Operators

# Operators are used to perform operations on variables and values.

# In the example below, we use the + operator to add together two values:

print(10 + 5)

# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# Operator	        Name       	         Example
# +	               Addition	               x + y
# -		             Subtraction             x - y
# *			           Multiplication          x * y
# /		              Division               x / y
# %		               Modulus               x % y
# *		             Exponentiation        x * y
# //		             Floor division        x // y

# Operator Precedence

# Operator precedence describes the order in which operations are performed.

print((6 + 3) - (6 + 3))

# Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:

print(100 + 5 * 3)

# Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)

#13/03/2023
#Python Lists

mylist = ["apple", "banana", "cherry"]

# List
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

thislist = ["apple", "banana", "cherry"]
print(thislist)

#List Items
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

# Example
# Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#list Length To determine how many items a list has, use the len() function:

thislist1 = ["apple", "banana", "cherry"]
print(len(thislist1))

#List Items - Data Types
#List items can be of any data type:

#example String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list can contain different data types:

#example A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

#type()
# From Python's perspective, lists are defined as objects with the data type 'list': <class 'list'>

# Example
# What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

## Example
# Using the list() constructor to make a List:

thislist = list(
  ("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
''' Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.'''

#Python - Access List Items

# Access Items
# List items are indexed and you can access them by referring to the index number:

# Example
# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
'''Note: The first item has index 0.'''

# Negative Indexing, Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

# Example
# Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.

# Example
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Example
# This example returns the items from the beginning to, but NOT including, "kiwi":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Example
# This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:

# Example
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:

# Example Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Python - Change List Items

# Change Item Value To change the value of a specific item, refer to the index number:

# Example
# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

# Example
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Example
# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
'''Note: The length of the list will change when the number of items inserted does not match the number of items replaced.'''

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Example
# Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

# Example
# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#14/03/2023
#Python - Add List Items


#Append Items: To add an item to the end of the list, use the append() method:

#Example
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items: To insert a list item at a specified index, use the insert() method. The insert() method inserts an item at the specified index:

# Example: Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List To append elements from another list to the current list, use the extend() method.

# Example Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #The elements will be added to the end of the list.
print(thislist)


# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

#Example Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#24/03/2023
#Remove Specified Item
#The remove() method removes the specified item.

#Example Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# Remove Specified Index  The pop() method removes the specified index.

#Example Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.

# Example Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
# Example Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
# Example Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List. The clear() method empties the list. The list still remains, but it has no content.

# Example Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# 03/04/23
# Python - Loop Lists

# Print all items in the list, one by one:

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

"""

"""
# 06/04/2023

# collection = single "variable" used to store multiple values
  # List = [] ordered and changeable. Duplicates[yes]

  # tuple = () ordered and unchangeable. Duplicates(yes). Faster

# Set = {} unordered  and immutable but Add/Remove {yes}. No duplicated

#6/4/2023
#Python - Loop Lists

# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through the Index Numbers

# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# Using a While Loop

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension

# List Comprehension offers the shortest syntax for looping through lists:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# The Syntax
# Condition

# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

newlist = [x for x in fruits]

# You can use the range() function to create an iterable:

newlist = [x for x in range(10)]

# Accept only numbers lower than 5:

# Expression

# Set the values in the new list to upper case:

# You can set the outcome to whatever you like:

# Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

# Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]

# Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]

# Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]

# Sort List Alphanumerically

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending

# Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# Customize Sort Function

# Sort the list based on how close the number is to 50:


def myfunc(n):
  return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Case Insensitive Sort

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse Order

# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy a List

# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join Two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# 10/4/23

# Join Two Lists

# There are several ways to join, or concatenate, two or more lists in Python.

# Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:

# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# Python Tuples

# Tuple

# Tuples are used to store multiple items in a single variable.

# Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Items


# Tuple items are ordered, unchangeable, and allow duplicate values.

# Ordered


# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable


# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.



# Allow Duplicates

# Since tuples are indexed, they can have items with the same value:

# Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# Tuple Length

# To determine how many items a tuple has, use the len() function:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# Create Tuple With One Item

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple Items - Data Types

# String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)


# A tuple can contain different data types:

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

# type()

# From Python's perspective, tuples are defined as objects with the data type 'tuple':

# What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


# The tuple() Constructor

# It is also possible to use the tuple() constructor to make a tuple.

thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)

# Access Tuple Items

# You can access tuple items by referring to the index number, inside square brackets:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# Negative Indexing

# Negative indexing means start from the end.


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new tuple with the specified items.


# Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# By leaving out the start value, the range will start at the first item:

# This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


# By leaving out the end value, the range will go on to the end of the list:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Range of Negative Indexes

# Specify negative indexes if you want to start the search from the end of the tuple:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


# Check if Item Exists

# To determine if a specified item is present in a tuple use the in keyword:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Update Tuples

# Change Tuple Values

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Add Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

# Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Remove Items

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)



# Unpack Tuples

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# Packing a tuple:


fruits = ("apple", "banana", "cherry")

print(fruits)

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":


# Unpacking a tuple:


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# Using Asterisk*

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:


# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# Loop Through a Tuple


# You can loop through the tuple items by using a for loop.


# Iterate through the items and print the values:


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# Loop Through the Index Numbers


# You can also loop through the tuple items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


# Using a While Loop

# Print all items, using a while loop to go through all the index numbers:


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join Two Tuples

# To join two or more tuples you can use the + operator:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# Multiply Tuples


# If you want to multiply the content of a tuple a given number of times, you can use the * operator:


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# Method	Description

# count()	Returns the number of times a specified value occurs in a tuple.

# index()	Searches the tuple for a specified value and returns the position of where it was found.


# Python Sets

# Sets are used to store multiple items in a single variable.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)



# Get the Length of a Set

# To determine how many items a set has, use the len() function.

thisset = {"apple", "banana", "cherry"}

print(len(thisset))



# Set Items - Data Types

# String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)


# A set can contain different data types:

set1 = {"abc", 34, True, 40, "male"}

print(set1)


# type()


# What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor

# It is also possible to use the set() constructor to make a set.

thisset = set(("apple", "banana", "cherry")) # note 
print(thisset)

# Access Items

# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Add Set Items

# To add one item to a set use the add() method.


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# To add items from another set into the current set, use the update() method.

# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# Add Any Iterable

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


# Remove Set Items

# To remove an item in a set, use the remove(), or the discard() method.

# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


# The del keyword will delete the set completely:

# thisset = {"apple", "banana", "cherry"}

# del thisset

# print(thisset) #this will raise an error because the set no longer exists.

# Loop Items

# You can loop through the set items by using a for loop:

# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# Join Sets

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:


# The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# Keep ONLY the Duplicates

# The intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


# The intersection() method will return a new set, that only contains the items that are present in both sets.

# Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


# Keep All, But NOT the Duplicates

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

# True and 1 is considered the same value:


x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)


"""

#Python - Dictionary

#Access Dictionary Items
# Accessing Items = You can access the items of a dictionary by referring to its key name, inside square brackets:


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


#There is also a method called get() that will give you the same result:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)



#Get Keys
#The keys() method will return a list of all the keys in the dictionary.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)

#example2
#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


#Get Values = The values() method will return a list of all the values in the dictionary.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)


#Example 
#Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change



#Example Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


# Get Items


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)

#Example = make a change in the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#Check if Key Exists To determine if a specified key is present in a dictionary use the in keyword:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Python - Change Dictionary Items

#Change Values = You can change the value of a specific item by referring to its key name:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

#Python - Add Dictionary Items

#Adding Items Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Update Dictionary = The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

#The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)

# Python - Remove Dictionary Items

# Removing Items = There are several methods to remove items from a dictionary:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# # Example = The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


# Example The del keyword removes the item with the specified key name:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# # Example = The del keyword can also delete the dictionary completely:

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

# Example  == The clear() method empties the dictionary:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# Python - Loop Dictionaries
# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

#Example Print all values in the dictionary, one by one:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

# Example You can also use the values() method to return values of a dictionary:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

#Example You can use the keys() method to return the keys of a dictionary:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)


#Example = Loop through both keys and values, by using the items() method:        

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)


#Python - Copy Dictionaries

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2. There are ways to make a copy, one way is to use the built-in Dictionary method copy().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


#Another way to make a copy is to use the built-in function dict(). 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Python - Nested Dictionaries

# Nested Dictionaries A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

#Or, if you want to add three dictionaries into a new dictionary:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary: 

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])








