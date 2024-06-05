import random

def draw_area ():
    for i in area:
        print(' ' * 18, *i)




area = [['*', '*', '*'],['*', '*', '*'],['*', '*', '*']]
print()
print('-------------------------------------------')
print('     Добро пожаловать в крестики-нолики')
print('-------------------------------------------')
print()
draw_area()
print()
for turn in range(1,10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')

    row = int(input('По гризонтали  | 1 | 2 | 3 |  :  '))-1
    column = int(input('По вертикали   | 1 | 2 | 3 |  :  '))-1
    print()
    print('--------------------"СЛЕДУЮЩИЙ ХОД"---------------------------')
    print()
    print()
    if area[row][column] == '*':
          area[row][column] = turn_char
    else:
        print('Ячейка занята, вы пропускаете ход')
        draw_area()
        continue

    draw_area()




