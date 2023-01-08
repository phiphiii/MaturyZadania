file = []
with open(r"liczby.txt") as plik:
    for line in plik:
        inst = int(line.strip())
        file.append(inst)

def nwd(a,b):
    while a!=b:
        if a > b:
            a = a- b
        else:
            b = b - a
    return a

dlug = 0
dzielnik = 0
pierw = 0
for i in range(0, len(file)-1):
    temp_dlug = 1
    temp_pierw = 0
    j = i
    temp_dzielnik = file[j]
    while nwd(temp_dzielnik, file[j+1]) != 1:
        temp_dlug = temp_dlug+1
        temp_dzielnik = nwd(temp_dzielnik,file[j+1])
        if temp_pierw == 0:
            temp_pierw=file[j]
        j = j + 1
    if temp_dlug>dlug:
        dlug = temp_dlug
        dzielnik = temp_dzielnik
        pierw = temp_pierw


print("Pierwsza liczba ciągu:",pierw)
print("Długość ciągu:",dlug)
print("Największy wspólny dzielnik:",dzielnik)