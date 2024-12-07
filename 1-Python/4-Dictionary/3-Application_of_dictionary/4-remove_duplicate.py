dict1 = {'a': 10, 'b': 15, 'c': 10, 'd': 15}
dict2 = {}
Set = set()

for key, val in dict1.items():
    if not val in Set:
        dict2[key] = val
        Set.add(val)
print(dict2)        