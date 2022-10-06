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
        number = int(input('Введите число: '))
        print(f'Ваше число: '+ str(number))
    except ValueError:
        print('Нужно ввести число: ')
        numberCheck()
    return number

def biNumber(number):
    numberB = 0
    numberP = 1
    if number > 0:
        while number > 0:
            numberB += number % 2 * numberP
            numberP *= 10
            number //= 2
    else:
        number = abs(number)
        while number > 0:
            numberB += number % 2 * numberP
            numberP *= 10
            number //= 2
        
    return numberB

def forMinusNumbers (numberB):
    result = []
    while numberB > 0:
        result.append(numberB % 10)
        numberB //= 10

    result.reverse()
    
    print(result)       # 1,2,3,4,

    num = 0
    for i, v in enumerate(reversed(result)):
        num += v * 10 ** i
    print(num)
    

def Main():
    digit = numberCheck()
    print(f'Десятичному числу  будет соответствовать двоичное число {biNumber(digit)} ')

Main()