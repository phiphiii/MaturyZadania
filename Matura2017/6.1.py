file = []
with open(r"dane.txt") as plik:
    for line in plik:
        inst = line.split()
        file.append(inst)

minPx = 255
maxPx = 0

for x in file:
    for i in x:
        if int(i)<minPx:
            minPx = int(i)
        if int(i)>maxPx:
            maxPx = int(i)

print("Najciemniejszy pixel ma jasność o wartości:",minPx)
print("Najjaśniejszy pixel ma jasność o wartości :",maxPx)


