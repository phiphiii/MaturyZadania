file = []
with open(r'identyfikator.txt') as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

palindrom = []
for x in file:
    temp_lit = x[:3]
    temp_num = x[3:]
    is_pies_lit = temp_lit == temp_lit[::-1]
    is_pies_num = temp_num == temp_num[::-1]
    if is_pies_lit or is_pies_num:
        palindrom.append(x)

for x in palindrom:
    print(x)
