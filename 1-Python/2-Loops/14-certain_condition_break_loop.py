num = int(input("Enter the number : "))

for i in range(num):
    if num % 2 == 0:
        break
    else:
        print(num,"Is odd number")