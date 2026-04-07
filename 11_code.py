''' String Methods '''

str1 = "Hello World"

""" 1.Uppercase """

print(str1.upper()) # Output: HELLO WORLD

""" 2. Lowercase """

print(str1.lower()) # Output: hello world

""" 3. Remove whitespace """

str2 = " Hello World "
print(str2.strip()) # Output: Hello World

""" 4. Removing trailing characters """

str3 = "Hello World!!!"
print(str3.rstrip("!")) # Output: Hello World

""" 5. Replace a string """

print(str1.replace("World","Bro")) # Output: Hello Bro

""" 6. Split a string """

print(str1.split(" ")) # Output: ['Hello', 'World']

""" 7. Captalize the first letter of a string """

str4 = "hELLO WORLD"
print(str4.capitalize()) # Output: Hello world

""" 8. Align a string """

print(str1.center(20)) # Output: '    Hello World     '
print(str1.ljust(20)) # Output: 'Hello World        '
print(str1.rjust(20)) # Output: 'Hello World        '

""" 9. Count the number of occurrences of a substring """

print(str1.count("o")) # Output: 2

""" 10. Check if a string starts with a specific substring """

print(str1.startswith("Hello")) # Output: True
print(str1.startswith("hello")) # Output: False

""" 11. Check if a string ends with a specific substring """

print(str1.endswith("World")) # Output: True 
print(str1.endswith("world")) # Output: False

""" 12. Find the index of the first occurrence of a substring """

print(str1.find("o")) # Output: 4
print(str1.find("H")) # Output: 0
print(str1.find("h")) # Output: -1

""" 13. Index of the first occurrence of a substring (raises an error if not found) """

print(str1.index("o")) # Output: 4
#print(str1.index("h"))  # This will raise a ValueError since "h" is not found in str1

""" 14. Check if a string is alphanumeric """

str5 = "Helloworld"
str6 = "Helloworld9876543"

print(str1.isalnum()) # Output: False (because of the space)
print(str5.isalnum()) # Output: True (because it only contains letters)
print(str6.isalnum()) # Output: True (because it only contains letters and numbers)

""" 15. Check if a string is alphabetic """

print(str1.isalpha()) # Output: False (because of the space)
print(str5.isalpha()) # Output: True (because it only contains letters)
print(str6.isalpha()) # Output: False (because it contains numbers)

""" 16. Check if a string is numeric """

print(str1.isnumeric()) # Output: False (because it contains letters and spaces)
print(str5.isnumeric()) # Output: False (because it contains letters)
print(str6.isnumeric()) # Output: False (because it contains letters)

""" 17. Check if a string is in lowercase """

print(str1.islower()) # Output: False (because it contains uppercase letters) 
print(str4.islower()) # Output: False (because it contains uppercase letters)

""" 18. Check if a string is in uppercase """

print(str1.isupper()) # Output: False (because it contains lowercase letters)
print(str4.isupper()) # Output: False (because it contains lowercase letters)

""" 19. Check if a string is printable """

print(str1.isprintable()) # Output: True (because all characters in str1 are printable)
print(str2.isprintable()) # Output: True (because all characters in str2 are printable, including the whitespace)

""" 20. Check if a string is whitespace """

print(str1.isspace()) # Output: False (because str1 contains non-whitespace characters)
print(str2.isspace()) # Output: False (because str2 contains non-whitespace characters, even though it has leading and trailing whitespace)

""" 21. Check if a string is title case """

print(str1.istitle()) # Output: True (because the first letter of each word in str1 is capitalized)
print(str4.istitle()) # Output: False (because the first letter of each word in str4 is not capitalized)

""" 22. Swap the case of a string """

print(str1.swapcase()) # Output: hELLO wORLD (because all uppercase letters in str1 are converted to lowercase and all lowercase letters are converted to uppercase)

""" 23. Title case a string """

print(str1.title()) # Output: Hello World (because the first letter of each word in str1 is capitalized and the rest are lowercase)