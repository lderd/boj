while True:
    name, age, weight = map(lambda x: int(x) if x.isdigit() else x, input().split())
    if age > 17 or weight >= 80:
        print(name, 'Senior')
    elif name == '#':
        break
    else:
        print(name, 'Junior')