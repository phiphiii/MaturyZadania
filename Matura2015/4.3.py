file = []
with open(r"liczby.txt") as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)


decimaltab = []
for x in file:
    temp = []
    for y in x:
        temp.append(int(y))
    temp.reverse()
    counter = 0
    temp_num = 0
    for z in temp:
        temp_num = temp_num + z*2**counter
        counter = counter+1
    decimaltab.append(temp_num)

max = 0
max_wier = 0
min = 999999999999999999999999999
min_wier = 0
counter = 0

for x in decimaltab:
    #print(x,counter)
    if x>max:
        max = x
        max_wier = counter
        #print(max, max_wier)
    if x<min:
        min = x
        min_wier = counter
        #print(min, min_wier)
    counter = counter+1

print(max, max_wier+1)
print(min, min_wier)

