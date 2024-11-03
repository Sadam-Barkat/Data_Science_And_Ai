even = 0
odd = 0
for i in range(10):
    num = int(input("Enter the number : "))
    if num % 2 == 0:
        even = num + even
    else:
        odd = num + odd
print("The sum of even numbers : ",even)    
print("The sum of odd numbers : ",odd)        