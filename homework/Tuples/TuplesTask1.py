tuple_1 = (1, 'ttt', 8, 67, 'YYY', [3, 10])
tuple_2 = (9, 'uuu', [6, 8], 8, 'ttt')
list_1 = []
for x in tuple_1:
    if x in list_1:
        continue
    for y in tuple_2:
        if x == y:
            list_1.append(x)
            break
print(tuple(list_1))