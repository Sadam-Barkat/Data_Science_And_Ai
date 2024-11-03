a = float(input("Enter side a : "))
b = float(input("Enter side b : "))
c = float(input("Enter side c : "))

if a <= 0 or b <= 0 or c <= 0:
    print("sides must be positive number")
elif (a + b) > c and (b + c) > a and (c + a) > b:
    print("Valid triangel")
else:
    print("Not valid")    