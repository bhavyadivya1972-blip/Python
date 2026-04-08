''' Manipulating Tuples '''

t1 = ("a", "b", "c", "d", "e")
t2 = list(t1)

t2[0] = "x"
t2.append("y")
t2.pop(1)

t1 = tuple(t2)
print(t1) # Output: ('x', 'c', 'd', 'e', 'y')