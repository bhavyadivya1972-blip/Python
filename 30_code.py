''' Access Items '''

""" 1. Accessing single values """

d1 = {"name": "Alice", "age": 30, "city": "New York"}
print(d1["name"])  # Output: Alice
print(d1["age"])   # Output: 30

print(d1.get("city"))  # Output: New York
print(d1.get("country", "USA"))  # Output: USA (default value)

""" 2. Accessing multiple values """

print(d1.keys())   # Output: dict_keys(['name', 'age', 'city'])
print(d1.values()) # Output: dict_values(['Alice', 30, 'New York'])
print(d1.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

""" 3. Accessing keys """

print(d1.keys())  # Output: dict_keys(['name', 'age', 'city'])

""" 4. Accessing key-value pairs """

print(d1.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])