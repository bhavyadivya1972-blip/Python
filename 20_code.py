''' List Methods '''

""" 1. Sorting a list in ascending order """

my_list = [3, 1, 4, 1, 5, 9]
my_list.sort() 
print(my_list) # Output: [1, 1, 3, 4, 5, 9]

l1 = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
l1.sort() 
print(l1) # Output: ['blue', 'green', 'indigo', 'orange', 'red', 'violet', 'yellow']

""" 2. Sorting a list in descending order """

l2 = [3, 1, 4, 1, 5, 9]
l2.sort(reverse=True) 
print(l2) # Output: [9, 5, 4, 3, 1, 1]

""" 3. Reversing a list """

l2 = [3, 1, 4, 1, 5, 9]
l2.reverse() 
print(l2) # Output: [9, 5, 4, 3, 1, 1]

""" 4. Copying a list """

l3 = [1, 2, 3]
l4 = l3.copy()
print(l4) # Output: [1, 2, 3]


