# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
from random import randint

def numberCheck():
    try:
        length = int(input('Введите число: '))
        print(f'Ваше число: ' + str(length))
    except ValueError:
        print('Нужно ввести число: ')
        numberCheck()
    return length

def firstList(length):
    length = abs(int(length))
    lis = []
    
    while length > 0:
        lis.append(randint(0, 10))
        length -= 1
    return lis

def multList(lis, length):
    secondList = []
    i = 0
    if length % 2 == 0:
        while i < int(length / 2):
            secondList.append(lis[i] * lis[length - (i + 1)])
            i += 1
        return secondList
    else:
        while i < int(length / 2):
            secondList.append(lis[i] * lis[length - (i + 1)])
            i += 1
        secondList.append(lis[round(length / 2)])
        return secondList

def Main():
    digit = numberCheck()
    newList = firstList(digit)
    print(newList)
    print(f'Список с произведениями чисел: \n{multList(newList, digit)}')

Main()

