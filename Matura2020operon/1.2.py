def ispali(num):
    temptab1 = []
    temptab2 = []
    if len(num)%2==1:
        num.pop(int((len(num) - 1) / 2))
    for x in range(len(num)):
        if x<len(num)/2:
            temptab1.append(num[x])
        else:
            temptab2.append(num[x])
    temptab2.reverse()
    if temptab1==temptab2:
        return True
    else:
        return False

def toarray(num):
    tab = []
    for x in str(num):
        tab.append(x)
    return tab


def changeToBinary(num):
    binary = []
    for i in range(num):
        if num>0:
            if num%2 == 0:
                num = num/2
                binary.append(0)
            elif num%2 == 1:
                num = (num-1)/2
                binary.append(1)
    binary.reverse()
    return binary

wynik = 0
for x in range(1000000):
    if ispali(toarray(x)) and ispali(changeToBinary(x)):
        wynik = wynik + x

print(wynik)
