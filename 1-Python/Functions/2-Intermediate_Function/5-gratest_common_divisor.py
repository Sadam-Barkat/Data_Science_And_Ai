def common_divisor(n1, n2):
    set1 = set()
    set2 = set()
    for i in range(1, n1+1):
        if n1 % i == 0:
            set1.add(i)

    for j in range(1, n2+1): 
        if n2 % j == 0:
            set2.add(j) 
    intersection = set1.intersection(set2)
    return max(intersection)

print(common_divisor(12,18))    
print(common_divisor(8,28))    