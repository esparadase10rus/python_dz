day = int(input('Введите номер дня: '))
if day > 7 or day < 1:
     print('Повторите ввод')
elif day == 6 or day == 7:
     print("Да, это выходной")
else:
     print("Нет, это не выходной")