file = []
with open(r"dane.txt") as plik:
    for line in plik:
        inst = line.split()
        file.append(inst)


toRemove = 0
for x in file:
    for i in range(0,319):
        if int(x[i]) != int(x[(319-i)]):
            toRemove = toRemove + 1
            break

print("By osiągnąć pionową oś symetri należy usuąć",toRemove,"wiersze/y")




