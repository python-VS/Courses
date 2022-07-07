c=input('Введите строку:')
d=input('Введите символ:')
if d in c:
    print(c.find(d))
    print(c.rfind(d))
else:
    print("заданный символ не содержится в введенной строке!")