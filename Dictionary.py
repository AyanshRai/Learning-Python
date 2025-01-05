marks = {
    "Priyanshi": 100,
    "Divij": 80,
    "Divisha": 50,
}

print(marks,type(marks)) # The type is dictionary
print(marks["Divij"]) # Gives specific marks of someone

# Methods 
marks = {
    "Priyanshi": 100,
    "Divij": 80,
    "Divisha": 50,
}

'''Items'''
print(marks.items()) # Conetnt in the dictionary, form of tuples

'''Keys'''
print(marks.keys()) # Name of the person in the dictionary 

'''Values'''
print(marks.values()) # Numeric content or value of the person in the dictionary 

'''Update'''
marks.update({"Priyanshi": 90, "zyx": 45}) # Update or add a content in the dictionary 
print(marks)

'''Get'''
print(marks.get("zyx")) # Give the value of zyx....(written in brcket)

# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 1. clear() - Removes all items from the dictionary
my_dict.clear()
print("After clear:", my_dict)  # Output: {}

# Re-creating the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 2. copy() - Returns a shallow copy of the dictionary
copy_dict = my_dict.copy()
print("Copy of dictionary:", copy_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 3. get() - Returns value for the specified key (default if not found)
print("Get 'a':", my_dict.get('a'))  # Output: 1
print("Get 'd' with default:", my_dict.get('d', 'Not found'))  # Output: Not found

# 4. items() - Returns a view object displaying key-value pairs
print("Items:", my_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 5. keys() - Returns a view object displaying all keys
print("Keys:", my_dict.keys())  # Output: dict_keys(['a', 'b', 'c'])

# 6. pop() - Removes item with specified key and returns its value
print("Popped 'b':", my_dict.pop('b'))  # Output: 2
print("Dictionary after pop:", my_dict)  # Output: {'a': 1, 'c': 3}

# 7. popitem() - Removes and returns the last key-value pair
print("Popped item:", my_dict.popitem())  # Output: ('c', 3)
print("Dictionary after popitem:", my_dict)  # Output: {'a': 1}

# 8. setdefault() - Returns value if key exists, else inserts the key with a default value
print("Setdefault for 'd':", my_dict.setdefault('d', 4))  # Output: 4
print("Dictionary after setdefault:", my_dict)  # Output: {'a': 1, 'd': 4}

# 9. update() - Updates dictionary with another dictionary
my_dict.update({'e': 5, 'f': 6})
print("Dictionary after update:", my_dict)  # Output: {'a': 1, 'd': 4, 'e': 5, 'f': 6}

# 10. values() - Returns a view object displaying all values
print("Values:", my_dict.values())  # Output: dict_values([1, 4, 5, 6])
