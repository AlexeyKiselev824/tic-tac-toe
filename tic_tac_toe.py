board = list(range(1, 10))
wins = [
    (1, 2, 3), (4, 5, 6),
    (7, 8, 9), (1, 4, 7),
    (2, 5, 8), (3, 6, 9),
    (1, 5, 9), (3, 5, 7)
]


def display_board():
    """Function to playing field output"""
    print("-------------")
    for i in range(3):
        print("|", board[0 + i*3], "|", board[1 + i*3],
              "|", board[2 + i*3], "|")
        print("-------------")


def take_input(player_token):
    """Function to input validation"""
    while True:
        value = input(f"Where to put {player_token}?: ")
        if value not in str(list(range(1, 10))):
            print("Wrong input. Repeat.")
            continue

        if value in " ":
            print("Wrong input. Repeat.")
            continue

        value = int(value)
        if str(board[value - 1]) in 'XO':
            print("This cell is already occupied. Repeat.")
            continue
        board[value - 1] = player_token
        break


def check_win():
    """Function to checks winning combination"""
    for each in wins:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    return False


count = 0
while True:
    display_board()
    count += 1
    if count % 2 == 1:
        take_input('X')
    else:
        take_input('O')

    if count > 3:
        winner = check_win()
        if winner:
            display_board()
            print(winner, "WIN!!!")
            break

    if count > 8:
        display_board()
        print("Draw!")
        break
