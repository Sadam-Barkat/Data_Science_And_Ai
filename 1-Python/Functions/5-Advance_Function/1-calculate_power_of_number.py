import math
def power_num(number):
    return int(math.pow(number,2))

number = int(input("Enter the number : "))
print(f'The power of {number} is {power_num(number)}')
