import random
secrate = random.randint(1,99)

guess = int(input("Guess the number : "))

while guess != secrate:
    if guess > secrate:
        print("To long")
    else:
        print("To short")    
    guess = int(input("Guess the number : "))
print(guess,"this was the number")        


