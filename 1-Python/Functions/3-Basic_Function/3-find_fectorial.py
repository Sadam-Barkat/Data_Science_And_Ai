def fectorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fectorial(number - 1)    

number = 5
print(f'The fectorial of {number} is {fectorial(number)}')