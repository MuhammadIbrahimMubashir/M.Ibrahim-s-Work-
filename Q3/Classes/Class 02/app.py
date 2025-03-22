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
