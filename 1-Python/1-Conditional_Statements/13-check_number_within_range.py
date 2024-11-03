num = int(input("Enter the number to chech : "))
start = int(input("Enter the lower range : "))
end = int(input("Enter the upper range : "))

if num >= start and num <= end:
    print(num , "In a specified range ")
else:
    print(num, "Not in specified range ")