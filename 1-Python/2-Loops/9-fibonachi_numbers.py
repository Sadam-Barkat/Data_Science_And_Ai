x = 0
z = 0
y = 1

for i in range(10):
    print(z,end=",")
    z = x+y
    x = y
    y = z