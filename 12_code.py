''' Formatting strings '''

""" 1. Concatenation """

str1 = "Hello"
str2 = "World"

print(str1 + " " + str2)  # Output: Hello World
print(str1 + str2)        # Output: HelloWorld

""" 2. Formatting strings """

name = "Alice"
age = 30

print("My name is {} and I am {} years old.")
print(format(name, age))  # Output: My name is Alice and I am 30 years old.

""" 3. f-strings """

print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 30 years old.





