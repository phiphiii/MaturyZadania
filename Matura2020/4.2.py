file = []
with open(r"pary.txt") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

for x in file:
    ciagznak = x.split(" ")
    ciagznak = ciagznak[1]
    temp_najd_ciagznak = ""
    najd_ciagznak = ""
    for y in ciagznak:
        if temp_najd_ciagznak == "":
            temp_najd_ciagznak = temp_najd_ciagznak +y
        else:
            if y == temp_najd_ciagznak[0]:
                temp_najd_ciagznak = temp_najd_ciagznak + y
            else:
                temp_najd_ciagznak = y
        if len(temp_najd_ciagznak)>len(najd_ciagznak):
            najd_ciagznak=temp_najd_ciagznak
    print(najd_ciagznak,len(najd_ciagznak))
