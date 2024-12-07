def string_plindorm(name):
    if name == name[::-1]:
        print(f'The given string {name} is palindorm {name[::-1]}')
    else:
        print(f'The given string {name} is not palindorm')    

string_plindorm("level")        