file = []
with open(r"liczby.txt") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

divtwo = 0
diveight = 0
temp = []
for x in file:
    for y in x:
        temp.append(int(y))
    if int(temp[len(x)-1]) ==0:
        divtwo = divtwo + 1
    if int(temp[len(x)-1]) == 0 and int(temp[len(x)-2])==0 and int(temp[len(x)-3])==0:
        diveight = diveight + 1
    temp = []


print("Liczb podzielnych przez 2 jest: ",divtwo)
print("Liczb podzielnych przez 8 jest: ",diveight)