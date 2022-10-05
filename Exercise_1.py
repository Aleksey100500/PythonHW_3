# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8
from random import randint
def digitCheck():
    try:
        length = int(input('Введите число: '))
        print(f'Ваше число: ' + str(length))
    except ValueError:
        print('Нужно ввести число: ')
        digitCheck()
    return length

def newList(length):
    length = int(length)
    lis = []
    while length > 0:
        lis.append(randint(0, 10))
        length -= 1
    return lis

def sumNumbers(length, lis):
    print("lis ", lis)
    i = 0
    sum = 0
    while i < length:
        sum += lis[i]
        i += 2
        print('Sum =',sum)
    return sum

def Main():
    digit = digitCheck()
    newNumbers = newList(digit)
    print(newNumbers)
    print(f'Сумма чисел на нечётных позициях: {sumNumbers(digit, newNumbers)}')

Main()
