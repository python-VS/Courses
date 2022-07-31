list_1 = [1, 2, 3, 4, 5, 6]
a, b = list_1.index(min(list_1)), list_1.index(max(list_1))
list_1[a], list_1[b] = list_1[b], list_1[a]
print(list_1)