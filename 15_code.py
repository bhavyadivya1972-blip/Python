''' List Indexes '''

l1 = ["apple", "banana", "cherry", "date", "elderberry"]
print(l1[0])  # Output: apple
print(l1[1])  # Output: banana
print(l1[2])  # Output: cherry
print(l1[-2])  # Output: date
print(l1[-1])  # Output: elderberry

""" Checking if an item exists in a list """

print("banana" in l1)  # Output: True
print("fig" in l1)     # Output: False

""" Range of Indexes """

print(l1[1:4])  # Output: ['banana', 'cherry', 'date']
print(l1[-3:-1]) # Output: ['cherry', 'date']

""" Jumping Indexes """

print(l1[0:5:2])  # Output: ['apple', 'cherry', 'elderberry']
print(l1[1:5:2])  # Output: ['banana', 'date']