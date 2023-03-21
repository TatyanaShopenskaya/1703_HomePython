# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:* 5
#     1 2 3 4 5
#     6
#     -> 5


from random import randint
array=[]
N=int(input('Введите количество элементов в массиве - '))
array = [randint(1,9) for i in range(N)]
print(array)

if N > 0:
    x = int(input('Задайте число x - '))  
    min_diff = abs(x - array[0])        #мин.разница(abs - функция, возвращающая абсолютное значение числа / модули)
    num_min_diff = array[0]
    for num in array[1:]:
        current_diff = abs(x - num) #текущая разница
        if current_diff < min_diff:
            min_diff = current_diff
            num_min_diff = num
    print(f'{num_min_diff} наиболее близко к {x}')
else:  
    print('Вы ввели неверное количество элементов')
    
 