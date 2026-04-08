''' Set Methods '''

""" 1. isdisjoint() method """

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: False

""" 2. issuperset() method """

set1 = {1, 2, 3, 4}
set2 = {2, 3}
print(set1.issuperset(set2))  # Output: True

set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}
print(set1.issuperset(set2))  # Output: False

""" 3. issubset() method """

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # Output: True

set1 = {1, 2, 3, 6}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # Output: False


