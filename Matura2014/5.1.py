file = []
with open(r"NAPIS.TXT") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

def primeNum(num):
    isPrime = True
    if num == 1:
        isPrime = False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                isPrime = False
                break
    return isPrime

napisy_piersze = []
for x in file:
    liczba = 0
    for y in x:
        liczba = liczba + ord(y)
    if primeNum(liczba):
        napisy_piersze.append(liczba)

for x in napisy_piersze:
    print(x)
