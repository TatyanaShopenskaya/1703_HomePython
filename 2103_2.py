# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13 (т.е. подсчитать кол-во уникальных слов, регистр верхний/нижний не учитываем)
 
text =  '''She sells sea shells on the sea shore 
        The shells that she sells are sea shells 
        I'm sure So if she sells sea shells on the sea shore 
        I'm sure that the shells are sea shore shells'''.lower().split()      #создали массив слов
print(text)
unique_words = set(text) #преобразуем в множество,чтобы исключить повторы слов
print(len(unique_words))  #выводим на печать длину множества уникальных слов

