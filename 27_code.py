''' Join Sets '''

s1 = {1, 2, 3}
s2 = {3, 4, 5}

""" 1. Union of Sets """ # Returns a new set

s3 = s1.union(s2)
print(s3)  # Output: {1, 2, 3, 4, 5}

""" 2. Update a Set with Another Set """ # Modifies the original set

s1.update(s2)
print(s1)  # Output: {1, 2, 3, 4, 5}

""" 3. Intersection of Sets """ # Returns a new set 
s4 = s1.intersection(s2)
print(s4)  # Output: {3}

""" 4. Intersection Update of Sets """ # Modifies the original set

s1.intersection_update(s2)
print(s1)  # Output: {3}

""" 5. Symmetric Difference of Sets """ # Returns a new set

s1 = {1, 2, 3}
s2 = {3, 4, 5}

s5 = s1.symmetric_difference(s2)
print(s5)  # Output: {1, 2, 4, 5}

""" 6. Symmetric Difference Update of Sets """ # Modifies the original set

s1.symmetric_difference_update(s2)
print(s1)  # Output: {1, 2, 4, 5}

""" 7. Difference of Sets """ # Returns a new set

s6 = s1.difference(s2)
print(s6)  # Output: {1, 2}

""" 8. Difference Update of Sets """ # Modifies the original set

s1.difference_update(s2)
print(s1)  # Output: {1, 2}