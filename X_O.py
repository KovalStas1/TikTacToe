table = [[1, 2, 3],[4, 5, 6],[7, 8, 9 ]]
for i in table:
    print(i)
#inital teable
# table[0][0] == 1, table[0][1] == 2, table[0][2] == 3
# table[1][0] == 4, table[1][1] == 5, table[1][2] == 6
# table[2][0] == 7, table[2][1] == 8, table[2][2] == 9

def hod_igrok_1():
    vash_hod = []
    while vash_hod != 'quit':
        vash_hod = int(input("Ход для крестика, введите число: "))
        if vash_hod == table[0][0]:
            table[0][0] = 'X'
            for i in table:
                print(i)
            break
        elif vash_hod == table[0][1]:
            table[0][1] = 'X'
            for i in table:
                print(i)

        elif vash_hod == table[0][2]:
            table[0][2] = 'X'
            for i in table:
                print(i)

        elif vash_hod == table[1][0]:
            table[1][0] = 'X'
            for i in table:
                print(i)

        elif vash_hod == table[1][1]:
            table[1][1] = 'X'
            for i in table:
                print(i)

        elif vash_hod == table[1][2]:
            table[1][2] = 'X'
            for i in table:
                print(i)

        elif vash_hod == table[2][0]:
            table[2][0] = 'X'
            for i in table:
                print(i)

        elif vash_hod == table[2][1]:
            table[2][1] = 'X'
            for i in table:
                print(i)

        elif vash_hod == table[2][2]:
                table[2][2] = 'X'
                for i in table:
                    print(i)
        else:
            print('Клетка занята')
        break

def hod_igroka_2():
    vash_hod_2 = []
    while vash_hod_2 != 'quit':
        vash_hod_2 = int(input("Ход для нолика, введите число: "))
        if vash_hod_2 == table[0][0]:
            table[0][0] = 'O'
            for i in table:
                print(i)
        elif vash_hod_2 == table[0][1]:
            table[0][1] = 'O'
            for i in table:
                print(i)
        elif vash_hod_2 == table[0][2]:
            table[0][2] = 'O'
            for i in table:
                print(i)
        elif vash_hod_2 == table[1][0]:
            table[1][0] = 'O'
            for i in table:
                print(i)
        elif vash_hod_2 == table[1][1]:
            table[1][1] = 'O'
            for i in table:
                print(i)
        elif vash_hod_2 == table[1][2]:
            table[1][2] = 'O'
            for i in table:
                print(i)
        elif vash_hod_2 == table[2][0]:
            table[2][0] = 'O'
            for i in table:
                print(i)
        elif vash_hod_2 == table[2][1]:
            table[2][1] = 'O'
            for i in table:
                print(i)
        elif vash_hod_2 == table[2][2]:
            table[2][2] = 'O'
            for i in table:
                print(i)
        else:
            print('Клетка занята')
        break

def win_combination():
    if table[0][0] == 'O' and table[0][1] == 'O' and table[0][2] == 'O':
        print('Нолик победил!')
    elif table[1][0] == 'O' and table[1][1] == 'O' and table[1][2] == 'O':
        print('Нолик победил!')
    elif table[2][0] == 'O' and table[2][1] == 'O' and table[2][2] == 'O':
        print('Нолик победил!')
    elif table[0][0] == 'O' and table[1][1] == 'O' and table[2][2] == 'O':
        print('Нолик победил!')
    elif table[0][2] == 'O' and table[1][1] == 'O' and table[2][0] == 'O':
        print('Нолик победил!')
    elif table[0][0] == 'O' and table[1][0] == 'O' and table[2][0] == 'O':
        print('Нолик победил!')
    elif table[0][1] == 'O' and table[1][1] == 'O' and table[2][1] == 'O':
        print('Нолик победил!')
    elif table[0][2] == 'O' and table[1][2] == 'O' and table[2][2] == 'O':
        print('Нолик победил!')
    if table[0][0] == 'X' and table[0][1] == 'X' and table[0][2] == 'X':
        print('Крестик победил!')
    elif table[1][0] == 'X' and table[1][1] == 'X' and table[1][2] == 'X':
        print('Крестик победил!')
    elif table[2][0] == 'X' and table[2][1] == 'X' and table[2][2] == 'X':
        print('Крестик победил!')
    elif table[0][0] == 'X' and table[1][1] == 'X' and table[2][2] == 'X':
        print('Крестик победил!')
    elif table[0][2] == 'X' and table[1][1] == 'X' and table[2][0] == 'X':
        print('Крестик победил!')
    elif table[0][0] == 'X' and table[1][0] == 'X' and table[2][0] == 'X':
        print('Крестик победил!')
    elif table[0][1] == 'X' and table[1][1] == 'X' and table[2][1] == 'X':
        print('Крестик победил!')
    elif table[0][2] == 'X' and table[1][2] == 'X' and table[2][2] == 'X':
        print('Крестик победил!')

def the_game():
    while True:
        hod_igrok_1()
        win_combination()
        hod_igroka_2()
        win_combination()



