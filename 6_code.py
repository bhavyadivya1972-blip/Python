''' Type casting in Python '''

_int = 10
_float = 10.5
_complex = 1+2j
_str = "Hello, World!"
_bool = True
_list = [1, 2, 3]
_tuple = (1, 2, 3)
_set = {1, 2, 3}
_dict = {"key": "value"}

print(float(_int)) # Output: 10.0
print(int(_float)) # Output: 10
print(dict(str = _str)) # Output: {'str': 'Hello, World!'}
print(str(_bool)) # Output: True
print(set(_list)) # Output: {1, 2, 3}
print(tuple(_set)) # Output: (1, 2, 3)
print(list(_dict)) # Output: ['key', 'value']