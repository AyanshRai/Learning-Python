# Use to find string length 
name = "Priyanshi"
print(len(name))

# use to exclude somne characters
name = "Priyanshi"
nameshort = name[0:3] # start from 0 and end at 3 (excluding 3)
print(nameshort)

character1 = name[1]
print(character1)

# Negative string
name = "Priyanshi"
print(name[-4:-1])
print(name[5:8]) # converted Negative intesis to corresponding Positive intesis
print(name[ :4]) # Is same as (name[0:4]) 
print(name[1: ]) # Is same as (name[1:5])
print(name[1:5])

# Skiping values 
word = "amazing"
print(word[1:6:2]) # only print character on place of 1,2 and 6(specific)

# string fuctions
name = "Priyanshi"
print(name.endswith("nshi")) # show that is the string ending with the character written in the brackets with aphostrophy 
print(name.endswith("wxys")) # shows true or false, '''nshi''' was true and '''wxys''' was false
print(name.startswith("Priy")) # show that is the string start with the character written in the brackets with aphostrophy 
print(name.startswith("abcd")) # shos true or false, '''priy''' was true and '''abcd''' was false
'''note that it will show false on issue of capital and small letter''' 

name = "priyanshi"
print(name.capitalize()) # use to capitalize the name 

# These are some of the most frequently used string methods in Python for common string manipulation tasks.

'''Returns the length of the string'''
s = "Hello"
print(len(s))  # Output: 5

'''Converts the string to lowercase'''
s = "Hello"
print(s.lower())  # Output: "hello"

'''Converts the string to uppercase'''
s = "Hello"
print(s.upper())  # Output: "HELLO"

'''Removes leading and trailing whitespace characters'''
s = "  Hello  "
print(s.strip())  # Output: "Hello"

'''Replaces a substring with another substring'''
s = "Hello World"
print(s.replace("World", "Python"))  # Output: "Hello Python"

'''Splits the string into a list based on a separator (default is whitespace)'''
s = "Hello World"
print(s.split())  # Output: ['Hello', 'World']
 
'''Joins elements of a list (or other iterable) into a single string with a separator'''
s = "-".join(["a", "b", "c"])
print(s)  # Output: "a-b-c"

'''Returns the index of the first occurrence of a substring. Returns -1 if the substring is not found'''
s = "Hello World"
print(s.find("World"))  # Output: 6
print(s.find("Python"))  # Output: -1
 
'''Counts the number of occurrences of a substring in the string'''
s = "Hello Hello Hello"
print(s.count("Hello"))  # Output: 3

'''Checks if the string starts with a specified substring'''
s = "Hello World"
print(s.startswith("Hello"))  # Output: True

'''Checks if the string ends with a specified substring'''
s = "Hello World"
print(s.endswith("World"))  # Output: True
 
'''Returns True if all characters in the string are alphabetic'''
s = "Hello"
print(s.isalpha())  # Output: True

'''Returns True if all characters in the string are digits'''
s = "12345"
print(s.isdigit())  # Output: True

'''Capitalizes the first letter of each word in the string'''
s = "hello world"
print(s.title())  # Output: "Hello World"

'''Allows you to format strings by embedding values'''
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# Output: "My name is Alice and I am 25 years old."

'''Returns True if all characters in the string are uppercase'''
s = "HELLO"
print(s.isupper())  # Output: True

'''Returns True if all characters in the string are lowercase'''
s = "hello"
print(s.islower())  # Output: True

