num = int(input("Enter the number : "))

if num % 2 == 0:
    print(num,"Divisible by 2")
elif num % 3 == 0:
    print(num,"Divisible by 3")  
elif num % 2 == 0 and num % 3 == 0:
    print(num,"Divisible by both 2 and 3")      