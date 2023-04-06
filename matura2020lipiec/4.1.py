file = []
with open(r'identyfikator.txt') as plik:
    for line in plik:
        inst = line.strip()
        file.append(inst)

max_sum = 0
max_nums = []
for x in file:
    temp = x[3:]
    temp_counter = 0
    for y in temp:
        temp_counter = temp_counter + int(y)

    if int(temp_counter) > int(max_sum):
        max_sum = temp_counter
        max_nums.clear()
        max_nums.append(x)
    elif int(temp_counter) == int(max_sum):
        max_nums.append(x)


for x in max_nums:
    print(x)
