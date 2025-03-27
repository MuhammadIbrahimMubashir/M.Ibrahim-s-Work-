print("Class 03")
print("Lesson 04:Srings & Type Casting")

#Strings in Python
#for multi line string use triple quotes '''any string'''
my_string: str = '''Hello,
World!'''
print(my_string)

my_string: str = r'Hello\t,\n Worl\\d!'
print(my_string)

print("\n-----\n")

my_string = 'Hello,\n World!'
print(my_string)

#Escape Sequence Characters In Python
print("Hello,\b World!") #\b backspace
print("Hello,\tWorld!")  #\t tab
print("Hello, \"World!\"")
print("Hello,\\ World!")

#Unicode Characters 
#Python also supports Unicode escape sequence characters, which are used to represent Unicode characters. These characters are denoted by \u followed by a four-digit hexadecimal code.
print(r"\u0041 = ", "\u0041")
print(r"\u0042 = ", "\u0042")
print(r"\u0043 = ", "\u0043")

#Performing Different Operations On String Object
#S#	Operation	Example
#1	Concatenation	my_string = 'Hello, ' + 'World!'
#2	Indexing	my_string = 'Hello, World!'; print(my_string[0]) # prints 'H'
#3	Slicing	my_string = 'Hello, World!'; print(my_string[7:]) # prints 'World!'
#4	Length	my_string = 'Hello, World!'; print(len(my_string)) # prints 13
#5	Upper Case	my_string = 'Hello, World!'; print(my_string.upper()) # prints 'HELLO, WORLD!'
#6	Lower Case	my_string = 'Hello, World!'; print(my_string.lower()) # prints 'hello, world!'

my_string = 'Hello, ' + 'World!' #Concatenation using + sign
print(my_string)

#Indexing, index value starts with 0 zero, so  the first character
#have index vlaue 0, second character have index value 1 and the third one
#have index value 2 and so on.
print(my_string[1]) #It will print 'e'

my_string: str = 'Hello, World!'
print(my_string[7:]) #It starts from 7 till the end of the string
print(my_string[0:5]) #It starts from 0 till the index 4 - (0,1,2,3,4) = 5 characters

print(len(" Hello, World! "))#calculating length of a string even the space will be treated as character

print(my_string.upper()) #Upper Case
print(my_string.lower()) #Lower Case

#Some Commonly Used String Methods
#split(): splits a string into a list of substrings based on a delimiter
#join(): joins a list of strings into a single string
#replace(): replaces a substring with another substring
#find(): returns the index of a substring
#count(): returns the number of occurrences of a substring

my_string: str = 'Hello! World'

# split into a list of words
words: str = my_string.split()
print("my_string.split()    = ", words)

words = my_string.split(" ") # Space as a delimiter
print('my_string.split(" ") = ',words)

words = my_string.split("l") # Splitting using 'l' as the delimiter
print('my_string.split("l") = ', words)

words: str = my_string.split("l") # Splitting using 'l' as the delimiter
print(words)

# join the words back into a single string
my_string: str = ', '
joined_string: str = my_string.join(['Pakistan', 'USA', 'Canada', 'France', 'Japan'])
print(joined_string)  # Pakistan, USA, Canada, France, Japan

joined_string: str = my_string.join('Pakistan') # my_string works as a seprator for each character in the word 'Pakistan', because string is a sequence of caharacter

print(joined_string) # P, a, k, i, s, t, a, n

print('-'.join(['Apple', 'Banana', 'Cherry'])); # ; The line terminitor

my_string: str = "Hello, World! Hello, Pakistan"
# replace a substring
my_string = my_string.replace('Hello', 'Salam Walikum')
print(my_string)  # prints 'Salam Walikum, World! Salam Walikum, Pakistan'

my_string: str = "Hello, World! Hello, Pakistan"
# find the index of a substring
starting_index = my_string.find('Hello') # Index value of the first occurance of the word 'Hello'
print("starting_index = ", starting_index)  # prints 0

# Now lets find the second occurance of the word 'Hello'
# index value start from zero

starting_index2: str = starting_index + len("Hello") #len=5

print(my_string[starting_index2:] ) # after slicing ", World! Hello, Pakistan
print(my_string[starting_index2:].find("Hello")) # Starting index 9, because of slicing ", World! Hello, Pakistan"

print(my_string)
print(len(my_string)) #character count = 29

print('\n-----\n')

print("Substring to search    = ", "Hello")
print("Starting index         = ", len("Hello")) # 5
print("End index              = ", len(my_string))
print("Second Occurance index = ", my_string.index(("Hello"), len("Hello"), len(my_string))) # (substring, start, end) - print 14

#Uncomment to see ValueError: substring not found
#print("Second Occurance index = ", my_string.index(("Hello7"), len("Hello"), len(my_string))) # (substring, start, end)

print(my_string.find("Hello7")) # -1 for not found

my_string = "Hello, World! Hello, Pakistan"
# count the occurrences of a substring
count = my_string.count('Hello')
print("my_string.count('Hello') = ", count)  # prints 2

# count the occurrences of a substring
count = my_string.count('P')
print("my_string.count('P')     = ", count)  # prints 1

# count the occurrences of a substring
count = my_string.count('o')
print("my_string.count('o')     = ", count)  # prints 2

# count the occurrences of a substring
count = my_string.count('hello') # case sensitive
print("my_string.count('hello') = ", count)  # prints 0

#String Formatting
#%s	String	"Hello, %s" % "Alice" → "Hello, Alice"
#%d	Integer (Decimal)	"Age: %d" % 25 → "Age: 25"
#%c	Character	"Letter: %c" % 'A' → "Letter: A"
#%f	Floating-point	"Pi: %f" % 3.14159 → "Pi: 3.141590"
#%.nf	Floating-point with n decimal places	"%.2f" % 3.14159 → "3.14

# % Operator
name: str = 'John'
age: int = 20
first_letter: str = name[0]
my_weight: float = 70.532000 # 70.536000

#uncomment to see type
#print(type((name, first_letter, age, my_weight)))

# using % operator
my_string: str = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %f Kg.''' % (name, first_letter, age, my_weight)
print(my_string)

my_string = '''My name is %s, first letter of my name is \'%c\', I am %d years old and my weight id %.2f Kg.''' % (name, first_letter, age, my_weight) # Dont forget period %.2f
print(my_string)

# str.format()
# using str.format()
my_string: str = 'My name is {} and I am {} years old.'.format(age, name) #order matters
print("line 1: ",my_string)

my_string: str = 'My name is {1} and I am {0} years old.'.format(age, name) #use indexing
print("line 2: ",my_string)

# F-String
# using f-strings
my_string: str = f'My name is {name} and I am {age} years old.' #Using Named Placeholders (Best for Readability)
print("line 3: ",my_string)

my_string: str = fr'My \name is {name} and I am {age}\n \t years \old.' #At the same time it could be f and r as well
print("line 4: ",my_string)
