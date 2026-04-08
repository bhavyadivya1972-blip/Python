''' Control Statements in Python '''

""" 1. Pass Statement """

for i in range(1,11):
    if i%2 == 0:
        pass
    else:
        print(i)
        
# Output:
# 1
# 3
# 5
# 7
# 9

""" 2. Continue Statement """

for i in range(1,11):
    if i%2 == 0:
        continue
    else:
        print(i)
        
# Output:
# 1
# 3
# 5
# 7
# 9

""" 3. Break Statement """

for i in range(1,11):
    if i%2 == 0:
        break
    else:
        print(i)
        
# Output:
# 1
