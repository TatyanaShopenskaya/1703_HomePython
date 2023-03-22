# Задача – «На вход программе подаются цифры,как только пользователь введёт 0 ввод прекращается. 
# Вывести наибольший элемент получившейся последовательности».
# Есть два кода с ошибками, нужно определить где ошибок меньше.

# Примечание: Программные коды на следующих слайдах

# 1 вариант
n = int(input())
max_number = 1000 #1. max_number = n (то, где ошибка)
while n != 0:
    n = int(input())
    if max_number > n: #2. n > max_number
        max_number = n
        print(max_number) 


#2 вариант
n = int(input())
max_number = -1   #это не ошибка
while n < 0:  #1. while n != 0:
    n = int(input())  #4. эту строчку перенести внуть цикла на 24 строку!
    if max_number < n:
        n = max_number #2. max_number = n
print(n)   #3.print(max_number) 

 