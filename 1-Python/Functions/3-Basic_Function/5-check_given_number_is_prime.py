def check_prime(number):
    count = 0
    for i in range(1,number+1):
        if number % i == 0:
            count += 1
    if count == 2:
        print(f'The given number {number} is prime') 
    else:
        print(f'The given number {number} is not prime')

check_prime(9)