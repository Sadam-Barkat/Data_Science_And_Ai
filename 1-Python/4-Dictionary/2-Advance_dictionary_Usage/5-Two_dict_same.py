def chek_same_dict(dict1, dict2):
    count = 0
    for item1, item2 in zip(dict1.items(), dict2.items()):
        if item1[0] == item2[0] and item1[1] == item2[1]:
            count += 1
    if count == len(dict1) or count == len(dict2):
        print("Dictionaries are identical")   
    else:
        print("Dictionaries are not identical")    
dict1 = {1:2, 2:2, 3:3, 4:4}      
dict2 = {1:2, 2:2, 3:3} 
chek_same_dict(dict1, dict2)   