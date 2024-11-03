num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
character = input("Select operator +,-,*,/ : ")

if character == '*':
    print("The multiplication of two numbers is : ",num1*num2)
elif character == '+':
    print("The addition of two numbers is : ",num1+num2)
elif character == '-':
    print("The subtraction of two numbers is : ",num1-num2)
elif character == '/':
    print("The division of two numbers is : ",num1/num2)    
else:
    print("invalid instructions")