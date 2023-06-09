# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

word = input('Введите слово - ').split()    #split() - разбивает строку по пробелам и формирует список
my_dict=dict() #создаем словарь

for letter in word:
    print(letter, end='') #end='' - чтобы не переходить на новую строку
    if letter not in my_dict: #если в словаре нет этой буквы, то мы ее добавляем
        my_dict[letter] = 0 #на данный момент столько дубликатов
    else:
        my_dict[letter]+=1 #увеличиваем кол-во дубликатов на 1, если они встречаются
        print('_', my_dict[letter], sep='', end="")
    print(end=' ')


