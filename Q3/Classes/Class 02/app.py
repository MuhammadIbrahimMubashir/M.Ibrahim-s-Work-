print("Class 02") 
print("Lesson 2: Data Types")

#Integers (int)
num: int = 2
#2 is integer
print(type(num),":",num)

#Float (float)
num1: float = 2.14
#.14 is float
print(type(num1),":",num1)

#Complex (complex)
num_complex: complex = 2 + 3j
print(type(num_complex),":",num_complex)
# 2 is real part
#3j is real part
print("Real Part:",num_complex.real)
print("Imaginary Part:",num_complex.imag)

#Boolean (bool)
is_python_fun: bool = True
print(type(is_python_fun),is_python_fun)

#String (str)
text_double: str = "Hello, Python!"# Strings with Double Quotes (")
text_single: str = 'Hello, Python!'# Strings with Single Quotes (')
text_multi: str = '''Hello, Python!'''# Multi-Line Strings with Triple Quotes (''' or """)
text_multi_1: str = """Hello, Python!""" # Multi-Line Strings with Triple Quotes (''' or """)

print(type(text_double), " text_double   = ", text_double)
print(type(text_single), " text_single   = ", text_single)
print(type(text_multi), " text_multi    = ", text_multi)
print(type(text_multi_1), " text_multi_1  = ", text_multi_1)

#List (list)
list: list = [1,2,3,"Java",3.14,True]
print(type(list),":",list)
list1: list = [1,2,3,"Java",3.14,3+2j]
print(type(list1),":",list1)

#Tuple (tuple)
Tuple: tuple = (1 , 2 , 3 , "M.I" , 2.71 , False , .3 , 3+2j)
print(type(Tuple),":",Tuple)

#Range (range)
Range: range = range(1,10,2)
print(type(Range),":",Range)
#Example
for i in range(2,12,2):
    print(i)
    
#Set (set)
Set: set = {1, 2, 33, 4, 4, 5}
print(type(Set), ": ", Set)

#Frozen Set(frozenset)
frozen_set = frozenset([11, 2, 3, 4, 4, 5])
print(type(frozen_set), ":", frozen_set)

#Mapping Type (Dictionary (dict))
dict1: dict = {"name":"M.Ibrahim","Age":14,"Language":"Python"}
print(type(dict1),":",dict1)

#Bytes (bytes) used to represent binary data
byte_data: bytes = b"Hello"
print(type(byte_data), ":", byte_data)
#An example for understanding
#Open an image file in binary mode
#with open("Apollo11.jpg", "rb") as image_file:
#    image_data = image_file.read()

#print(image_data)
#with open("Apollo11.jpg", "rb") as source_file:
#    data = source_file.read()

# Write the binary data to a new image file
#with open("copy.jpg", "wb") as target_file:
#    target_file.write(data)

#print("Image copied successfully!")

#Bytearray (bytearray)
byte_array: bytearray = bytearray([65, 66, 67, 69]) #65=A, 66=B ....decimal number system
print(type(byte_array), " byte_array = ", byte_array)
print(byte_array[0])
print(chr(byte_array[0]))
print("Empty bytearray(): ",bytearray())
#UTF-8
byte_array: bytearray = bytearray([65, 66, 67, 69])
# Converting the entire bytearray to a string using decode()
print("Decoded string: ", byte_array.decode('utf-8'))

#None Data Type In Python
x: str = None
y: str = None
z: str = x

#display the data type of x:
print(type(x))
print("value of x = " + str(x) )
print("x == y = ", x == y)
print("id(x) = ", id(x))
print("id(y) = ", id(y))
print("id(z) = ", id(z))
print("x is y = ", x is y)
print("x is z = ", x is z)
print("id(x) is id(z) = ", id(x) is id(z)) # False :( why? you will get the answer in topic 'Integer Literals in Python'
print("id(x) == id(z) = ", id(x) == id(z)) # True
'''
In Python, `==` is the equality operator, which checks if the values of two objects are equal.
On the other hand, `is` is the identity operator, which checks if two objects are the same object in memory.
'''

#Type Casting
i: int = 10
print("Value of i = " + str(i) + ",     Type of i = " + str(type(i)))

j: float = 20.6

f: float = i + j #Implicit Type Casting
print("Value of f = " + str(f) + ",   Type of f = " + str(type(f)))

f1: float = 66.89
print("Value of f1 = " + str(f1) + ", Type of i = " + str(type(f1)))

i1: int = int(f1) #When ever you type cast a float value into an integer it truncate
             #the decimal part and only keeps the whole number
print("Value of i1 = " + str(i1) + ",    Type of i = " + str(type(i1)))

s: str = "25.8"
f2: float = float(s)
print("Value of f2 = " + str(f2) + ",  Type of i = " + str(type(f2)))

#isinstance() Function In Python=to check the data type
age: int = 20
weight: float = 66.89
print("check: isinstance(age, int)      = ", isinstance(age, int))
print("check: isinstance(weight, int)   = ", isinstance(weight, int))
print("check: isinstance(weight, float) = ", isinstance(weight, float))

print("Lesson 03")
print("Operators,Keywords & Variables")

# x + y = z
# x and y are operands
# + - * / are operators
# z is results

# Unary Operators
#1.Negative
x = 5
y = -x # y is -5
print(y)

#2.Logical NOT (not)
a = True
b = not a  # b is now False
print("b =", b)

# Bitwise NOT (~)
x: int = 5  # Binary: 0101
y: int = ~x  # y is now -6 (binary: 1010, but in two's complement form)
print("y =", y)

# Binary Operators
#1.Arithmetic Operators (+, -, *, /, etc.):
#2.Perform basic math operations.
#3.Comparison Operators (==, !=, >, <, etc.):
#4.Compare two values and return True or False.
#5.Logical Operators (and, or):
#6.Combine boolean values.
#7.Assignment Operators (=, +=, -=, etc.):
#8.Assign values to variables or perform operations while assigning.

#1.Arithmetic Operators:-
#1. +	Addition	5 + 2 = 7
#2. -	Subtraction	5 - 2 = 3
#3. *	Multiplication	5 * 2 = 10
#4. /	Division (float)	5 / 2 = 2.5
#5. //	Floor Division	5 // 2 = 2 (removes decimal part)
#6. %	Modulus (remainder)	5 % 2 = 1
#7. **	Exponentiation	5 ** 2 = 25

a: int = 10
b: int = 3
print("a + b  = ", a + b)   # 13 Addition
print("a - b  = ", a - b)   # 7 Subtraction
print("a * b  = ", a * b)   # 30 Multiplication
print("a / b  = ", a / b)   # 3.3333333333333335
print("a // b = ", a // b)  # 3 Floor Division
print("a % b  = ", a % b)   # 1 Modulus (remainder)
print("a % b  = ", a ** b)

#2. Comparison (Relational) Operators:-
# ==	Equal	5 == 5 → True
# !=	Not equal	5 != 3 → True
# >	Greater than	5 > 3 → True
# <	Less than	5 < 3 → False
# >=	Greater than or equal	5 >= 5 → True
# <=	Less than or equal	5 <= 3 → False

x: int = 10
y: int = 5

print("x == y = ", x == y)  # False, Equal
print("x != y = ", x != y)  # True, Not equal
print("x > y  = ", x > y)   # True, Greater than
print("x < y  = ", x < y)   # False, Less than
print("x >= y = ", x >= y)  # True, Greater than or equal
print("x <= y = ", x <= y)  # False, Less than or equal

#3. Logical Operators:-
# and	Logical AND	(5 > 3 and 10 > 5) → True
# or	Logical OR	(5 > 3 or 10 < 5) → True
# not	Logical NOT	not(5 > 3) → False

x: bool = True
y: bool = False

print("x and y = ", x and y)  # False
print("x or y  = ", x or y)   # True
print("not x   = ", not x)    # False

#4. Assignment Operators
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# //=	x //= 3	x = x // 3

x = 5
print("Assignment: x = 5                    ",x)  # Output: 5

x += 3  # Equivalent to x = x + 3
print("Addition Assignment: x += 3          ",x)  # Output: 8

x -= 3  # Equivalent to x = x - 3
print("Subtraction Assignment: x -= 3       ",x)  # Output: 5

x *= 3  # Equivalent to x = x * 3
print("Multiplication Assignment: x *= 3    ",x)  # Output: 15

x /= 3  # Equivalent to x = x / 3
print("Division Assignment: x /= 3          ",x)  # Output: 5.0

x //= 3  # Equivalent to x = x // 3
print("Floor Division Assignment: x //= 3   ",x)  # Output: 1.0

#5. Identity Operators
#is	Returns True if objects have the same memory location	x is y
#is not	Returns True if objects do not have the same memory location	x is not y

a: list = [1, 2, 3]
b: list = [1, 2, 3]
c: list = a

print("a is c     =  ",a is c)       # True  (same object, sharing same memmory space)
print("a is b     =  ",a is b)       # False (different objects, seperate memmory space)
print("a == b     =  ", a == b)      # True  (same values, different memmory space but having same vlaues)
print("a is not b =  ", a is not b)  # True  (True because of different memmory space, although having same memmory space)

print('\n-----\n') # seperator for better output readability

print("id(a) = ", id(a))
print("id(b) = ", id(b))
print("id(c) = ", id(c))

#6. Membership Operators
#in	Returns True if value is in the sequence	x in list
#not in	Returns True if value is NOT in the sequence	x not in list

my_list: list = [1, 2, 3, 4, 5]

print("my_list           = ", my_list)            # [1, 2, 3, 4, 5]
print("3 in my_list      = ", 3 in my_list)       # True
print("10 not in my_list = ", 10 not in my_list)  # True

print("\n-----\n")

my_string: str = "Operation Badar"

print("my_string                 = ", my_string)                # Operation Badar
print("'O' in my_string          = ", 'O' in my_string)         # True
print("'Hello' not in my_string  = ", 'Hello' not in my_string) # True

# Deleting Variable
x: int = 10
del x
print(x)
