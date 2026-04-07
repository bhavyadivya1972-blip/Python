''' Python Variables '''

# a = 10
# class_10 = "Abhay"
# _code = "Python"
''' There are two types of variables '''
# 1. Local Variables
# 2. Global Variables

b = 10

def my_function():
    global a 
    a = 20
    return print(b)
my_function() # Output: 10
print(a) # Output: 20
print(b) # Output: 10
