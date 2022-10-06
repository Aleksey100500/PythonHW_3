# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def numberCheck():
    try:
        number = int(input('Введите неотрицательное число: '))
        print(f'Ваше число: '+ str(number))
    except ValueError:
        print('Нужно ввести число: ')
        numberCheck()
    return number

def biNumber(number):
    numberB = 0
    numberP = 1
    while number > 0:
        numberB += number % 2 * numberP
        numberP *= 10
        number //= 2

    return numberB

def Main():
    digit = numberCheck()
    print(f'Вашему числу будет соответствовать двоичное число {biNumber(digit)} ')

Main()