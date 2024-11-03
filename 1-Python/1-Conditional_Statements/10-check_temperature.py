temp = float(input("Enter temperature : "))

if temp < 0:
    print("Freezing")
elif temp > 0 and temp <= 25:
    print("Moderate")  
else:
    print("Hot")      