def dict_cube(num):
    dict1 = {}
    for i in range(1,num):
        dict1[i] = i*i*i
    return dict1

num = int(input("Enter the number : "))
print(dict_cube(num))