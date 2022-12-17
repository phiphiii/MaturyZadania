instruction = []
with open(r"przyklad.txt") as plik:
    for line in plik:
        inst = line.strip()
        instruction.append(inst)
n = 0
slowo = ""
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
for x in instruction:
    if x.startswith("DOPISZ"):
        n += 1
        temp = x.split()
        slowo = slowo + temp[1]
    elif x.startswith("USUN"):
        n -= 1
        slowo = slowo[:-1]
    elif x.startswith("ZMIEN"):
        temp = x.split()
        slowo = slowo[:-1]
        slowo = slowo + temp[1]
    elif x.startswith("PRZESUN"):
        temp = x.split()
        slowo = slowo[::-1]
        temp_slowo = ""
        counter = 0
        temp_litera = 0
        for i in alphabet:
            if temp[1] == i:
                temp_litera = counter + 1
            else:
                counter = counter + 1
        for i in slowo:
            if i == temp[1]:
                if i == "Z":
                    temp_slowo = temp_slowo + "A"
                else:
                    temp_slowo = temp_slowo + alphabet[temp_litera]
            else:
                temp_slowo = temp_slowo + i

        slowo = temp_slowo
        slowo = slowo[::-1]

print("Długość:", n, "\nSłowo:", slowo)
# ALANTURING
