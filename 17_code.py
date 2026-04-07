''' Removing items from a list '''

""" 1. Using pop """

my_list = [1, 2, 3, 4, 1, 2, 3, 4]
popped_item = my_list.pop()  # Removes and returns the last item
print(popped_item)  # Output: 4
print(my_list)     # Output: [1, 2, 3, 4, 1, 2, 3]

""" 2. Using remove """

my_list.remove(2)  # Removes the first occurrence of the specified value
print(my_list)     # Output: [1, 3, 4, 1, 2, 3]

""" 3. Using del """

del my_list[0]     # Deletes the item at the specified index
print(my_list)     # Output: [3, 4, 1, 2, 3]

""" 4. Using clear """

my_list.clear()    # Removes all items from the list
print(my_list)     # Output: []
