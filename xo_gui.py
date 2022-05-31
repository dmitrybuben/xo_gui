# Игра крестики-нолики с использованием графического интерфейса против компьютера, человек ходит первым

from tkinter import *
import random


root = Tk()             # окно
root.title('Крестики-нолики')   # заголовок окна
game_run = True     # значение пока продолжается игра
field = []      # список для хранения значений поля
cross_count = 0     # счетчик крестиков - если будет 5 и не будет победы - выдаст ничью


def new_game():             # запуск при нажатии кнопки новая игра
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '       # очистка поля
            # заполнение фона цветом
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):    # обработка нажатия
    print(row, ' ', col)
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')


def check_win(smb):  # smb - это Х или О - и проверяется кто выйграл
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n]
                   [2], smb)  # проверка по строкам
        check_line(field[0][n], field[1][n], field[2]
                   [n], smb)  # проверка по столбцам
    check_line(field[0][0], field[1][1], field[2]
               [2], smb)      # проверка по диагонали
    check_line(field[2][0], field[1][1], field[0]
               [2], smb)      # проверка по диагонали


def check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False


def can_win(a1, a2, a3, smb):                                      # не допустить выйгрыш
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res


def computer_move():                                            # проверка возможности выйгрышка компьютера
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'О'
            break


for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=3,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()
