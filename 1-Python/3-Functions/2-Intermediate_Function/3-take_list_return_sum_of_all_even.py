def sum_even(List):
    sum = 0
    for i in List:
        if i % 2 == 0:
            sum = sum + i
    return sum

List = [1,2,3,4,5,6,7,8,9,10]   
print(f'The sum of even number from given list {List} is {sum_even(List)}')