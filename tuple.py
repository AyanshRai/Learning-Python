
a = (1,2,3,4,5,6,7) # Multi element tuple 
print(type(a))
b = () # Blank tuple 
print(type(b))
c = (1,) # Single element tuple 
print(type(c))

# functions of tuple
a = (1,2,3,4,5,6,7) # Multi element tuple 
print(type(a))

# Count
my_tuple = (1, 2, 3, 2, 2, 4)
print(my_tuple.count(2))  # Output: 3

# Index
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # Output: 2

# len
my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3

# max
my_tuple = (1, 2, 3, 4)
print(max(my_tuple))  # Output: 4

# min
my_tuple = (1, 2, 3, 0)
print(min(my_tuple))  # Output: 0

# sum
my_tuple = (1, 2, 3, 4)
print(sum(my_tuple))  # Output: 10

# check (true and false)
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)  # Output: True
print(6 in my_tuple)  # Output: False

# Concatenation & Repetition 
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated = tuple1 + tuple2  # Concatenation
repeated = tuple1 * 2          # Repetition

print(concatenated)  # Output: (1, 2, 3, 4)
print(repeated)      # Output: (1, 2, 1, 2)


