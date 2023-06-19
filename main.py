tic_tac_toe = [
    ['□', '□', '□'],
    ['□', '□', '□'],
    ['□', '□', '□']
]

def show_board(board):
    for row in board:
        string = ""
        for item in row:
            string += item + " "

        print(string)

def is_won(board):
    for row in board:
        if row[0] != '□' and row[0] == row[1] and row[1] == row[2]:
            return True

    for col in range(len(row[0])):
        if board[0][col] != '□' and board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            return True

    if board[0][0] != '□' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True

    if board[0][2] != '□' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True

    return False


def is_draw(board):
    for row in board:
        for item in row:
            if item == '□':
                return False

    return True


while not is_draw(tic_tac_toe):
    show_board(tic_tac_toe)


    while True:
        x = int(input("Игрок 1 введите координату X (1-3) на вашем ходе: ")) - 1
        y = int(input("Игрок 1 введите координату Y (1-3) на вашем ходе: ")) - 1
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Неверная координата. Попробуйте еще раз.')
            continue

        if tic_tac_toe[y][x] != '□':
            print('Этот ход уже сделан. Попробуйте еще раз.')
            continue

        tic_tac_toe[y][x] = 'X'
        if is_won(tic_tac_toe):
            print('Игрок 1 победил!')
            exit(0)
        else:
            break

    show_board(tic_tac_toe)

    if is_draw(tic_tac_toe):
        print('Ничья!')
        exit(0)

    while True:
        x = int(input("Игрок 2 введите координату X (1-3) на вашем ходе: ")) - 1
        y = int(input("Игрок 2 введите координату Y (1-3) на вашем ходе: ")) - 1
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Неверная координата. Попробуйте еще раз.')
            continue

        if tic_tac_toe[y][x] != '□':
            print('Этот ход уже сделан. Попробуйте еще раз.')
            continue

        tic_tac_toe[y][x] = 'O'
        if is_won(tic_tac_toe):
            print('Игрок 2 победил!')
            exit(0)
        else:
            break

print('Ничья!')
