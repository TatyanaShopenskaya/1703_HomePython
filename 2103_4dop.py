#полей#Крестики-нолики

#все функции содаются до основного кода!
def print_field(field):   #создали сами функцию для вывода на печать сразу 3х полей
    print(*field[:3])           # * - нужна для распоковки элементов из массива, теперь можно с ними работать отдельно
    print(*field[3:6])
    print(*field[6:])

def win(field):  #проверка победы - сами создали эту функцию
    if (my_field[0] == my_field[1] == my_field[2]   #первые 3 строки - проверка по горизонтали
    or my_field[3] == my_field[4] == my_field[5]
    or my_field[6] == my_field[7] == my_field[8]
    or my_field[0] == my_field[3] == my_field[6]   #вторые 3 строки - проверка по вертикали
    or my_field[1] == my_field[4] == my_field[7]
    or my_field[2] == my_field[5] == my_field[8]
    or my_field[0] == my_field[4] == my_field[8]   #третьи 2 строки - проверка по диагонали
    or my_field[2] == my_field[4] == my_field[6]):
        return True   #возврат какого-то значения (правда или ложь)
    return False


my_field = ['1','2','3','4','5','6','7','8','9']     #создаем массив из 9 чисел(9 полей)   кавычки-чтобы был строковый тип
    
for step in range(1,10):  #step - потому что расписываем для ходов
    print('Первый ход: - ', step)
    print_field(my_field)
    move=input('Сделайте ход - ')    #действие #без int, чтобы был строковой тип
    while move not in my_field: #"защита от дурака"
        print('Вы ввели некорректные данные.')
        move=input('Сделайте еще ход - ')
    if step % 2 != 0:
        symbol = 'x'
        my_field[int(move)-1] = "x" #-1 из-за индексирования в списке
    else:
        symbol = 'o'
        my_field[int(move)-1] = "o"
    if win(my_field):
        print_field(my_field)
        print(f'Победил {symbol}')
        break   #если кто-то победил, останавливаем игру
else:
    print("Ничья!")
