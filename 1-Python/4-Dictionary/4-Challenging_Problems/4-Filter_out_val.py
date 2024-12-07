dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict2 = {key:val for key, val in dict1.items() if val < 3 }
print(dict2)