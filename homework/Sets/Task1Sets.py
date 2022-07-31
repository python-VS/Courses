from collections import Hashable

list_1 = [1, 'a', 5, 3.2]
x = {i for i in list_1 if isinstance(i, Hashable)}
print(x)