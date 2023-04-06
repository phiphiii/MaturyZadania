file = []
with open(r'identyfikator.txt') as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

def isValid(id):
    odp = False
    sign_0 = ((ord(id[0])-55)*7)
    sign_1 = ((ord(id[1])-55)*3)
    sign_2 = (ord(id[2])-55)
    sign_4 = (int(id[4])*7)
    sign_5 = (int(id[5])*3)
    sign_6 = (int(id[6]))
    sign_7 = (int(id[7])*7)
    sign_8 = (int(id[8])*3)
    suma = sign_0 + sign_1 + sign_2 + sign_4 + sign_5 + sign_6 + sign_7 + sign_8

    if suma%10!=int(id[3]):
        odp = True
    return odp


for x in file:
    if isValid(x):
        print(x)


