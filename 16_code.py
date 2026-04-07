''' Adding items in list '''

""" 1. Using append """

my_list = [1, 2, 3]
my_list.append(4) # Appends 4 to the end of the list
print(my_list)  # Output: [1, 2, 3, 4]

""" 2. Using insert """

my_list.insert(1, 1.5) # Inserts 1.5 at index 1 (between 1 and 2)
print(my_list)  # Output: [1, 1.5, 2, 3, 4]

""" 3. Using extend """

l2 = [1,2,3,4]
l3 = [5,6,7,8]
l4 = [9,10,11,12]

l2.extend(l3) # Extends l2 by appending elements from l3
print(l2) # Output: [1, 2, 3, 4, 5, 6, 7, 8]

print(l4+l3) # Output: [9, 10, 11, 12, 5, 6, 7, 8] 