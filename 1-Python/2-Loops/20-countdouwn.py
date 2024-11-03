import time

start = int(input("Enter the starting number for the countdown: "))

for i in range(start, -1, -1):
    print(i)
    time.sleep(1) 

print("Countdown complete!")
