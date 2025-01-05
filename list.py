friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"] # Can store any data type
print(friends[3]) # Helps to result in output of the given No. in the string position
print(friends[1:4]) # Print from 1 to 4 (excludes 4th one)

# Append
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
friends.append("Priyanshi")
print(friends)

# Sort
l1 = [4343, 44, 5, 345.06, 10, 22, 36]
l1.sort() # In Accending order
print(l1)

# Reverse
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
friends.reverse() # Reverse the order conten
print(friends)

# Insert
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
friends.insert(0, 2222222) #Insert any Content in between the list at any position 
print(friends)             #(First write the index the position you want to insert the content and then write the content you want to insert)

# Pop
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends.pop(1)) # Remove the content entered on that no. postion in the list and return value seprately (here 1 say about removal of orange as orange is on sequence 1)
print(friends) 

# Remove
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
friends.remove(2) # Removes the content from list on that numeric position
print(friends)  
