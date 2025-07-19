with open("log.txt", 'a+') as f:
    f.seek(0)
    lines = f.readlines()

with open('log.txt', 'w') as f:
    for line in lines:
        if line.strip() == 'four':
            f.write(line)
