''' Add/remove set items '''

""" 1. Adding only one item to a set, use the add() method. """

s1 = { "apple", "banana", "cherry" }
s1.add("date")
print(s1) # Output: {'banana', 'cherry', 'apple', 'date'}

""" 2. To add multiple items to a set """

s2 = { "apple", "banana", "cherry" }

s1.update(s2) # Output: {'banana', 'cherry', 'apple', 'date'}

""" 3. To remove an item from a set, use the remove() method. """

s1.remove("banana")
print(s1) # Output: {'cherry', 'apple', 'date'}

s1.discard("cherry")
print(s1) # Output: {'apple', 'date'}

# You can also use other methods like pop() del() and clear() to remove items from a set.

