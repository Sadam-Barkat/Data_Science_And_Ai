sentance = "hello world hello python world"
sentance_list = sentance.split()
dict1 = {}

for word in sentance_list:
    if not word in dict1:
        dict1[word] = 1
    else:
        dict1[word] += 1
print(dict1)        