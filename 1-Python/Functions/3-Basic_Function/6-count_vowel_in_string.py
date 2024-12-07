def count_vowel(name):
    name.lower()
    vowels = "aeiou"
    count = 0
    for i in name:
        if i in vowels:
            count += 1
    return count        

print(count_vowel("sadam"))