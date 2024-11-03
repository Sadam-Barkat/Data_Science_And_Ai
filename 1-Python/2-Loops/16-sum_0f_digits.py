num = input("Enter the number : ")
sum = 0
for i in range(len(num)):
    sum = int(num[i]) + sum
print("The sum of digits are ",sum)    