symbols = ['_', '_', '_', '_', '_', '_', '_', '_', '_']


def game_board():
    print(f'''---------
| {symbols[0]} {symbols[1]} {symbols[2]} |
| {symbols[3]} {symbols[4]} {symbols[5]} |
| {symbols[6]} {symbols[7]} {symbols[8]} |
---------''')


def is_winner(sym, x_or_o):
    return ((sym[0] == x_or_o and sym[1] == x_or_o and sym[2] == x_or_o) or  # top row
            (sym[3] == x_or_o and sym[4] == x_or_o and sym[5] == x_or_o) or  # middle row
            (sym[6] == x_or_o and sym[7] == x_or_o and sym[8] == x_or_o) or  # bottom row
            (sym[0] == x_or_o and sym[3] == x_or_o and sym[6] == x_or_o) or  # first column
            (sym[1] == x_or_o and sym[4] == x_or_o and sym[7] == x_or_o) or  # middle column
            (sym[2] == x_or_o and sym[5] == x_or_o and sym[8] == x_or_o) or  # last column
            (sym[0] == x_or_o and sym[4] == x_or_o and sym[8] == x_or_o) or  # diagonal
            (sym[2] == x_or_o and sym[4] == x_or_o and sym[6] == x_or_o))  # diagonal


def occupied():
    print("This cell is occupied! Choose another one!")


def make_move():
    while not win_check():
        o_num = symbols.count("O")
        x_num = symbols.count("X")
        if x_num > o_num:
            player = 'O'
        else:
            player = 'X'
        coordinates = input("Enter the coordinates: ").split()
        column = int(coordinates[0])
        row = int(coordinates[1])

        if not isinstance(column, int) or not isinstance(row, int):
            print("You should enter numbers!")
        if column > 3 or row > 3:
            print("Coordinates should be from 1 to 3!")
            make_move()
        elif column == 1 and row == 1:
            if symbols[6] == "_":
                symbols[6] = player
                game_board()
            else:
                occupied()
                make_move()
        elif column == 1 and row == 2:
            if symbols[3] == "_":
                symbols[3] = player
                game_board()
            else:
                occupied()
                make_move()
        elif column == 1 and row == 3:
            if symbols[0] == "_":
                symbols[0] = player
                game_board()
            else:
                occupied()
                make_move()
        elif column == 2 and row == 1:
            if symbols[7] == "_":
                symbols[7] = player
                game_board()
            else:
                occupied()
                make_move()
        elif column == 2 and row == 2:
            if symbols[4] == "_":
                symbols[4] = player
                game_board()
            else:
                occupied()
                make_move()
        elif column == 2 and row == 3:
            if symbols[1] == "_":
                symbols[1] = player
                game_board()
            else:
                occupied()
                make_move()
        elif column == 3 and row == 1:
            if symbols[8] == "_":
                symbols[8] = player
                game_board()
            else:
                occupied()
                make_move()
        elif column == 3 and row == 2:
            if symbols[5] == "_":
                symbols[5] = player
                game_board()
            else:
                occupied()
                make_move()
        elif column == 3 and row == 3:
            if symbols[2] == "_":
                symbols[2] = player
                game_board()
            else:
                occupied()
                make_move()


def win_check():
    if is_winner(symbols, 'X') and not is_winner(symbols, 'O'):
        print("X wins")
        return "X wins"
    elif is_winner(symbols, 'O') and not is_winner(symbols, 'X'):
        print("O wins")
        return "O wins"
    elif "_" not in symbols:
        print("Draw")
        return "Draw"


game_board()
make_move()

