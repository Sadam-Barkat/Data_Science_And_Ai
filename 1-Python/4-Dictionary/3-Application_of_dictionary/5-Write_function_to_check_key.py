def check_key_val(dict1, key):
    if key in dict1:
        print(f'{key} exist in {dict1} dictionary')
    else:
        print(f'{key} not found in {dict1} dictionary')   
dict1 = {1:2, 2:2, 3:3}         
check_key_val(dict1, 8)