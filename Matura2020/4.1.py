file = []
with open(r"pary.txt") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)


def czyPierwsza(x):
    isPrime = True
    if x==1:
        isPrime = False
    for i in range(2, x):
        if (x % i) == 0:
            isPrime = False
            break
    return isPrime


for x in file:
    num = x.split(" ")
    num = int(num[0])
    if (num % 2) == 0:
        a = 0
        b = num
        for i in range(num):
            if (czyPierwsza(a) and czyPierwsza(b)):
                print(num, a, b)
                break
            else:
                a=a+1
                b=b-1
