# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. 
#Последняя строка содержит число X.

from random import randint
N=[randint(1,3) for _ in range(randint(7,10))]
print(N, end=' ')
print()
x = int(input('Введите число, количество которого надо найти - '))
count_x = 0
for i in N:
    if i == x:
        count_x+=1
print(count_x)  
