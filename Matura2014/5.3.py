file = []

with open(r"NAPIS.TXT") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

sortfile = sorted(file)
duplikaty = []
for x in sortfile:
    temp = sortfile.index(x)+1
    if temp == len(sortfile):
        break
    else:
        if x == sortfile[temp]:
            duplikaty.append(x)

i = 0
for x in duplikaty:
    if i%2==0:
        print(x)
    i = i +1