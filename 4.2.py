instruction = []
with open(r"instrukcje.txt") as plik:
    for line in plik:
        inst = line.strip()
        instruction.append(inst)

temp = 0
temp2 = ""
dop = 0
usn = 0
zmn = 0
prz = 0
for x in instruction:
    if x.startswith("DOPISZ"):
        usn = 0
        zmn = 0
        prz = 0
        dop = dop + 1
        if dop > temp:
            temp = dop
            temp2 = "DOPISZ"
    elif x.startswith("USUN"):
        dop = 0
        zmn = 0
        prz = 0
        usn = usn + 1
        if usn > temp:
            temp = dop
            temp2 = "USUN"
    elif x.startswith("ZMIEN"):
        dop = 0
        usn = 0
        prz = 0
        zmn = zmn + 1
        if zmn > temp:
            temp = zmn
            temp2 = "ZMIEN"
    elif x.startswith("PRZESUN"):
        dop = 0
        usn = 0
        zmn = 0
        prz = prz + 1
        if prz > temp:
            temp = prz
            temp2 = "PRZESUN"


print("Najdłuższy ciąg funkcji to funkcja",temp2,"\nDługość ciągu",temp)