# 3. Задайте список из n чисел последовательности (1+1/n)**n
# и выведите на экран их сумму.

number = int(input('Введите число '))
if number < 0:
    print ('меньше нуля ')
elif number == 0:
    print ('равно нулю ')
else:
    summa = 0
    for i in range(1, number + 1):
        summa += (1 + 1/i)**i
    print ('Сумма чисел последовательности ',summa)