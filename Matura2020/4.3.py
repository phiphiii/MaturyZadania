file = []
with open(r"pary.txt") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

min_licz = 1000
min_slowo = "zzzzzzz"
for x in file:
    x = x.split(" ")
    liczba = int(x[0])
    slowo = x[1]
    if liczba==len(slowo):
        if min_licz>liczba:
            min_licz = liczba
        if liczba==min_licz:
            counter = 0
            for y in slowo:
                if ord(y) < ord(min_slowo[slowo.index(y)]):
                    min_slowo = slowo
                    break

print(min_licz,min_slowo)