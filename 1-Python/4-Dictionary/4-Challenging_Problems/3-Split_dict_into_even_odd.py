def split_even_odd(dict1):
    even_dict = {}
    odd_dict = {}

    for key, val in dict1.items():
        if val % 2 == 0:
            even_dict[key] = val
        else:
            odd_dict[key] = val
    return even_dict, odd_dict        

dict1 = {1:1, 2:2, 3:3, 4:4, 5:5} 
print(split_even_odd(dict1))

