file = []

with open(r"dane_6_1.txt") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

def cezar(slowo, k):
    temp_slowo = ""
    for x in slowo:
        for i in range(k):
            if x=="Z":
                x="A"
                i = i+1
            else:
                x = chr(ord(x)+1)
        temp_slowo = temp_slowo + x
    return temp_slowo


for x in file:
    print(cezar(x,107))

