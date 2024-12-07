dict1 = {'a': 10, 'b': 15, 'c': 7}
max_key = max(dict1, key=dict1.get)
print(max_key)