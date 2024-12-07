def frequecny(name):
    List = []
    for i in name:
        count = 0
        for j in name:
            if j in i:
                count += 1
        List.append((count,i))  
    List = list(set(List))
    return List
print(frequecny("aklksddhfkaj"))    
