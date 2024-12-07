dict1 = {
    'Name':'John',
    'age':30,
    'address':{'street':'123 Elm st', 'City':'Boston'}
}

#access the value of key city
print(dict1['address']['City'])

#add new value with phone in nested dict
dict1['address']['phone'] = '123-456-7890'
print(dict1['address'])

#delete the nested address
del dict1['address']['street']
print(dict1)

#iterate through the ouermost key values and print
for key, val in dict1.items():
    print(key,'=', val)