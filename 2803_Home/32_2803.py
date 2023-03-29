# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

size_arr = randint(1,20)
print(size_arr)
arr = [randint(1,9) for _ in range(size_arr)]
print(arr)

num_min = int(input('Введите заданный минимум - '))
num_max = int(input('Введите заданный максимум - '))

for i in range(size_arr):
    if num_min <= arr[i] <= num_max:
        print(i)
