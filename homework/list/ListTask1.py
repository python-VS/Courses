list_1 = [1, '', 3, 'b', '', 6, [1, 'c']]
for i in list_1:
    if i == '':
        list_1.remove(i)
print(list_1)