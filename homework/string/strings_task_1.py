# Пользователь вводит строку.
# 1. Сначала выведите третий символ этой строки.
# 2. Во второй строке выведите предпоследний символ этой строки.
# 3. В третьей строке выведите первые пять символов этой строки.
# 4. В четвертой строке выведите всю строку, кроме последних двух символов.
# 5. В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# 6. В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# 7. В седьмой строке выведите все символы в обратном порядке.
# 8. В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# 9. В девятой строке выведите длину данной строки.

string = input("введите строку:")
print(string[2])
print(string[-2])
print(string[:5])
print(string[0:-2])
print(string[2::2])
print(string[1::2])
print(string[-1::-1])
print(string[-1::-2])
print(len(string))