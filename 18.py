# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:* 5
#     1 2 3 4 5
#     6
#     -> 5


from random import randint
N=int(input('Введите количество элементов в массиве - '))
list_1 = [randint(1,15) for i in range(N)]
print(list_1)

if N > 0:
    x = int(input('Задайте число x - '))  
    min = abs(x - list_1[0])        # abs - функция, возвращающая абсолютное значение числа
    index = 0
    for i in range(1,N):
        number = abs(x - list_1[i])
        if number < min:
            min = number
            index = i
    print(list_1[index])
else:  
    print('Вы ввели неверное количество элементов')
    
    

     





#b=[abs(a[i]-x) for i in range(len(a))]
#print(a[b.index(min(b))])
    
 