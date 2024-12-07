def cal_avg_sal(salary):
    if not salary:
        return 0
    else:
        return sum(salary) / len(salary)

salary = [1000,2000,3000,5000]    
print(cal_avg_sal(salary))