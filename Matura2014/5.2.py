file = []
with open(r"NAPIS.TXT") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

napisy_rosnace = []
for x in file:
    temp_num = 0
    temp_tf = False
    for y in x:
        if temp_num<ord(y):
            temp_num = ord(y)
            temp_tf = True
        else:
            temp_tf = False
            break
    if temp_tf:
        napisy_rosnace.append(x)

for x in napisy_rosnace:
    print(x)
