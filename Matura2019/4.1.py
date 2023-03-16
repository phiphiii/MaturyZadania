import math

file = []
with open(r"liczby.txt") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

counter = 0

#Ja nic nie widze ze nie moge uzywac bibliotek wiec czemu nie
for x in file:
    x = int(x)
    p = math.log(x) / math.log(3)
    if p - int(p) == 0:
        counter = counter+1

print(counter)

#Zadanie z błędem
