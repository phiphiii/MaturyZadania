instruction = []
with open(r"instrukcje.txt") as plik:
    for line in plik:
        inst = line.strip()
        instruction.append(inst)

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
i = 0
ilerazy = []
for x in alphabet:
    ilerazy.append(0)
    i = i + 1
counter = 0
for x in instruction:
    if x.startswith("DOPISZ"):
        temp = x.split()
        for j in alphabet:
            if temp[1] == j:
                ilerazy[alphabet.index(j)] = ilerazy[alphabet.index(j)] + 1
                counter = 0
            else:
                counter = counter + 1

temp = 0
for x in ilerazy:
    if x > temp:
        temp = x
        temp2 = alphabet[ilerazy.index(x)]

print("Litera",temp2,"została dopisana najwięcej razy,\nzostała ona dopisana",temp,"razy")
