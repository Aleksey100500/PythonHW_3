# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def numberCheck():
    try:
        maxNumber = int(input('Введите максимальный индекс Фибоначчи: '))
        maxNumber = abs(maxNumber)
    except ValueError:
        print('Нужно ввести число.')
        numberCheck()
    return maxNumber

def fibonacci(maxNumber):
    a, b = 1, 1
    for i in range(maxNumber):
        yield a
        a, b = b, a + b

digit = numberCheck()
data = list(fibonacci(digit))

def newList(data):
    data.insert(0, 0)
    length = len(data) - 1
    newData = []
    i = 8
    while length > 0:
        newData.append(-data[length])
        length -= 1
    newData.extend(data)
    print(newData)

newList(data)
