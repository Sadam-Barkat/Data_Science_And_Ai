student = {
    'name':'sadam',
    'age':24,
    'grade':3.55
}
#print grade
print(student['grade'])

#add new key city
student['city'] = 'New York'
print(student)

#update the value of age into 20
student['age'] = 20
print(student)

#remove the key city
del student['city']
print(student)

#iterate through student and print all keys
for key in student.keys():
    print(key)

#iterate through student and print all values
for val in student.values():
    print(val)

#print all key value pair
for key, val in student.items():
    print(key,":", val)

#check grade in student
if student['grade'] in student:
    print("True")   
else:
    print("Flase")     

#count the total keys in student
count_keys = len(student.keys())
print(count_keys)