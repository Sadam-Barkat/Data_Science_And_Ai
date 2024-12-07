def anagram(s1, s2):
    count = 0
    for i in s1:
        if i in s2:
            count += 1
    if count == len(s2):
        print(f'{s1} is the anagram of {s2}')
    else:
        print(f'{s1} is not anagram of {s2}')      


anagram("Georgebush","hebugsGore")