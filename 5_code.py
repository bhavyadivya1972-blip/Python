''' Data Conversion in Python '''

int1 =  float(10)
float1 = int(10.9)
complex1 = 1+2j
str1 = dict(str = "Hello, World!")
bool1 = str(True)
list1 = set([1, 2, 3])
tuple1 = (1, 2, 3)
set1 = tuple({1, 2, 3})
dict1 = list({"key": "value"})

print(type(int1)) # Output: <class 'float'>
print(int1) # Output: 10.0

print(type(float1)) # Output: <class 'int'>
print(float1) # Output: 10

print(type(tuple1)) # Output: <class 'tuple'>
print(tuple1) # Output: (1, 2, 3)

print(type(dict1)) # Output: <class 'list'>
print(dict1) # Output: ['key', 'value']

print(type(str1)) # Output: <class 'dict'>
print(str1) # Output: {'str': 'Hello, World!'}

print(type(bool1)) # Output: <class 'str'>
print(bool1) # Output: True

print(type(list1)) # Output: <class 'set'>
print(list1) # Output: {1, 2, 3}