''' Add/Remove items '''

"""1 . Adding items """

""" (i) Using a new key """

d1 = {'a': 1, 'b': 2, 'c': 3}
d1['d'] = 4
print(d1) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

""" (ii) Using update() method """

d1.update({'e': 5, 'f': 6})
print(d1) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

""" 2 . Removing items """

""" (i) Using clear statement """

d1.clear()
print(d1) # Output: {}

""" (ii) Using pop statement """

d1 = {'a': 1, 'b': 2, 'c': 3}
d1.pop('b')
print(d1) # Output: {'a': 1, 'c': 3}

""" (iii) Using popitem statement """

d1 = {'a': 1, 'b': 2, 'c': 3}
d1.popitem()
print(d1) # Output: {'a': 1, 'b': 2}