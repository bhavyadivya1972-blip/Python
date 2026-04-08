''' Nested if Statements '''

x = 167

if x > 100:
    print("x is greater than 100")
    
    if x > 150:
        print("x is also greater than 150")
        
    else:
        print("x is not greater than 150")
        
elif x == 100:
    print("x is equal to 100")
    
else:
    print("x is less than 100")
    
# Output: x is greater than 100
#         x is also greater than 150