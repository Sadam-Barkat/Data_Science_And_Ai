dict1 = {'a': 5, 'b': 10}
dict2 = {'a': 3, 'b': 7}

dict3 = {}

for item1, item2 in zip(dict1.items(), dict2.items()):
    dict3[item1[0]] = item1[1] + item2[1]
print(dict3)    