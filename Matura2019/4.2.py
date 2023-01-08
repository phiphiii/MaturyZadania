file = []
with open(r"liczby.txt") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

def silnia(num):
    wynik = 1
    if num>1:
        temp = num
        for x in range(2,num+1):
            wynik=wynik*temp
            temp = temp-1
    return wynik


for x in file:
    sil = 0
    for y in range(len(x)):
        sil = sil + silnia(int(x[y]))
    if sil==int(x):
        print(int(x))


