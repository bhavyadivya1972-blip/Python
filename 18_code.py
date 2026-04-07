''' Changing items in a list'''

""" 1. Changing an item at a specific index """

companies = ['Google', 'Apple', 'Microsoft', 'Amazon']
companies[0] = 'Meta'
print(companies) # Output: ['Meta', 'Apple', 'Microsoft', 'Amazon']

""" 2. changing mulitple items in a list """

companies = ['Google', 'Apple', 'Microsoft', 'Amazon']
companies[0:2] = ['Meta', 'Apple Inc.']
print(companies) # Output: ['Meta', 'Apple Inc.', 'Microsoft', 'Amazon']

companies[0:2] = ['Louis Vitton', 'Johnson & Johnson' , 'NVIDIA', 'Netflix']
print(companies) # Output: ['Louis Vitton', 'Johnson & Johnson', 'NVIDIA', 'Netflix' , 'Microsoft', 'Amazon']

companies[0:2] = ['Zara']
print(companies) # Output: ['Zara', 'NVIDIA', 'Netflix' , 'Microsoft', 'Amazon']