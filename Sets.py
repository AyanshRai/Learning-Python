s = {1, 5, 32, 34, 5, 5, 5}
e = set() # Don't use s = {} as it will create an empty dictionary 

print(s) # Content doesn't repeat in set

# Methods 
s = {1, 5, 32, 34, 5, 5, 5, "Priyanshi"}
print(s, type(s))

'''Add'''
s.add(566) # Add conetnt in the set
print(s, type(s))

# Creating a set
my_set = {1, 2, 3}

# 1. add() - Adds an element to the set
my_set.add(4)
print("After add:", my_set)  # Output: {1, 2, 3, 4}

# 2. clear() - Removes all elements from the set
my_set.clear()
print("After clear:", my_set)  # Output: set()

# Recreating the set
my_set = {1, 2, 3}

# 3. copy() - Returns a shallow copy of the set
copy_set = my_set.copy()
print("Copy of set:", copy_set)  # Output: {1, 2, 3}

# 4. discard() - Removes an element safely (does nothing if element is not found)
my_set.discard(2)
print("After discard:", my_set)  # Output: {1, 3}

# 5. remove() - Removes an element, raises KeyError if element not found
# my_set.remove(5)  # Uncommenting this line will raise a KeyError
my_set.remove(1)
print("After remove:", my_set)  # Output: {3}

# 6. pop() - Removes and returns an arbitrary element
popped_item = my_set.pop()
print("Popped item:", popped_item)  # Output: 3 (or any element, since order is random)
print("Set after pop:", my_set)  # Output: set()

# Recreating the set again
my_set = {1, 2, 3}

# 7. union() - Returns a new set with elements from both sets
set2 = {3, 4, 5}
union_set = my_set.union(set2)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}

# 8. update() - Adds elements from another iterable to the set
my_set.update([4, 5, 6])
print("After update:", my_set)  # Output: {1, 2, 3, 4, 5, 6}

# 9. intersection() - Returns the common elements between sets
intersection_set = my_set.intersection(set2)
print("Intersection:", intersection_set)  # Output: {3, 4, 5}

# 10. intersection_update() - Updates the set with the intersection of itself and another set
my_set.intersection_update(set2)
print("After intersection_update:", my_set)  # Output: {3, 4, 5}

# 11. difference() - Returns the elements present in the first set but not the second
difference_set = my_set.difference(set2)
print("Difference:", difference_set)  # Output: set() (since all elements of my_set are in set2)

# 12. difference_update() - Removes elements of the set that are present in the other set
my_set.difference_update(set2)
print("After difference_update:", my_set)  # Output: set()

# Recreating the set again
my_set = {1, 2, 3}

# 13. symmetric_difference() - Returns elements in either set, but not in both
symmetric_difference_set = my_set.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 4, 5}

# 14. symmetric_difference_update() - Updates the set with symmetric difference of itself and another set
my_set.symmetric_difference_update(set2)
print("After symmetric_difference_update:", my_set)  # Output: {1, 2, 4, 5}

# 15. issubset() - Checks if all elements of the set are in another set
print("Is my_set a subset of set2?", my_set.issubset(set2))  # Output: False

# 16. issuperset() - Checks if the set contains all elements of another set
print("Is set2 a superset of my_set?", set2.issuperset(my_set))  # Output: True

# 17. isdisjoint() - Checks if two sets have no elements in common
print("Are my_set and set2 disjoint?", my_set.isdisjoint(set2))  # Output: False

# 18. frozenset() - Returns an immutable version of a set
frozen_set = frozenset(my_set)
print("Frozen set:", frozen_set)  # Output: frozenset({1, 2, 4, 5})
 
# 19. len() # Find length 
print(len(my_set))  
