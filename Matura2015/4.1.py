file = []
with open(r"liczby.txt") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

temp = []
for x in file:
    numzero = 0
    numones = 0
    for y in x:
        if int(y)==0:
            numzero = numzero + 1
        else:
            numones = numones + 1
    if numzero>numones:
        temp.append(x)

print(len(temp))