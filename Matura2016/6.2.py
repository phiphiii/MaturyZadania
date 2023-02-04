file = []

with open(r"dane_6_2.txt") as plik:
    for line in plik:
        inst = line.split()
        file.append(inst)

def decezar(slowo, k):
    temp_slowo = ""
    for x in slowo:
        for i in range(k):
            if x=="A":
                x="Z"
                i = i+1
            else:
                x = chr(ord(x)-1)
        temp_slowo = temp_slowo + x
    return temp_slowo


for x in file:
    if len(x) == 1:
        x.append("0")
    print(decezar(x[0],int(x[1])))