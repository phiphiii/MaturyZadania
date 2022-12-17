instruction = []
with open(r"instrukcje.txt") as plik:
    for line in plik:
        inst = line.strip()
        instruction.append(inst)
n = 0
for x in instruction:
    if x.startswith("DOPISZ"):
        n += 1
    elif x.startswith("USUN"):
        n -= 1


print("Długość słowa:",n)
# ALANTURING
