
instruction = []
with open(r"przyklad.txt") as plik:
    for line in plik:
        inst = line.strip()
        instruction.append(inst)
n= 0
for x in instruction:
    if x.startswith("DOPISZ"):
        n += 1
    elif x.startswith("USUN"):
        n -= 1
print("1)", n)