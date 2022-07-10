tuple_1 = (1, 'ttt', 8, 67, 'YYY', [3, 10])
tuple_2 = (9, 'uuu', [6, 8], 8, 'ttt')
list = []
for item in tuple_1:
    if item in list:
        continue
    for item_2 in tuple_2:
        if item == item_2:
            list.append(item)
            break
print(tuple(list))
