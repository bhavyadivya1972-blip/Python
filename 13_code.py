''' Escape Characters '''

""" 1. To insert double quotes or single quotes in a string """

str1 = "I am a \"Python\" programmer." 
print(str1)  # Output: I am a "Python" programmer.

str2 = "I am a \'Python\' programmer."
print(str2)  # Output: I am a 'Python' programmer.

""" 2. To insert a new line in a string """

str3 = "Hello,\nWorld!"
print(str3)  # Output: Hello,
             #         World!

""" 3. To insert a tab in a string """

str4 = "Hello,\tWorld!"
print(str4)  # Output: Hello,    World!

""" 4. Removing spaces between words using backspace """

str5 = "Hello,             \bWorld!"
print(str5)  # Output: Hello,World!

""" 5. To insert a backslash in a string """

str6 = "This is a backslash: \\"
print(str6)  # Output: This is a backslash: \