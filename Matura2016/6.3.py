file = []

with open(r"dane_6_3.txt") as plik:
    for line in plik:
        inst = line.split()
        file.append(inst)

def findkey(slowo, slowo2):
    keys = []
    error = False
    for x in range(len(slowo)):
        temp = slowo[x]
        k = 0
        while temp != slowo2[x]:
            if temp=="Z":
                temp="A"
                k = k + 1
            else:
                temp = chr(ord(temp)+1)
            k = k + 1
        keys.append(k)
    for x in keys:
        if x != keys[0]:
            error = True
    return error


for x in file:
    if findkey(x[0], x[1]):
        print(x)

