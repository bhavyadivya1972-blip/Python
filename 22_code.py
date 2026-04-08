''' Tuple Indexes '''

t1 = (10, 20, 30, 40, 50)

""" 1. Positive Indexing """
print(t1[0])  # Output: 10
print(t1[1])  # Output: 20
print(t1[2])  # Output: 30
print(t1[3])  # Output: 40
print(t1[4])  # Output: 50

""" 2. Negative Indexing """
print(t1[-1])  # Output: 50
print(t1[-2])  # Output: 40
print(t1[-3])  # Output: 30
print(t1[-4])  # Output: 20
print(t1[-5])  # Output: 10

""" 3. Checking for an element in a tuple using 'in' operator """

print(20 in t1)  # Output: True
print(60 in t1)  # Output: False

""" 4. Range of Indexes """

print(t1[1:4])  # Output: (20, 30, 40)
print(t1[:3])   # Output: (10, 20, 30)
print(t1[-1:2])  # Output: ()
print(t1[1:4:2])  # Output: (20, 40)