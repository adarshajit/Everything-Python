
board = [" " for i in range(9)]

def print_board():

    row1 = f"|{board[0]}|{board[1]}|{board[2]}|"
    row2 = f"|{board[3]}|{board[4]}|{board[5]}|"
    row3 = f"|{board[6]}|{board[7]}|{board[8]}|"

    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    
def player_move(icon):
    if icon =="X":
        number = 1
    elif icon == "O":
        number = 2

    print(f"your turn player {number}")
    choice = int(input("enter position: ").strip())
    if board[choice-1] == " ":
        board[choice-1] = icon
    else:
        print(f'position {choice} is already taken!!')

def player_win(icon):
    if board[0] == icon and board[1]== icon and board[2] == icon or \
    board[3] == icon and board[4]== icon and board[5] == icon or \
    board[6] == icon and board[7]== icon and board[8] == icon or \
    board[0] == icon and board[3]== icon and board[6] == icon or \
    board[1] == icon and board[4]== icon and board[7] == icon or \
    board[2] == icon and board[5]== icon and board[8] == icon or \
    board[0] == icon and board[4]== icon and board[8] == icon or \
    board[2] == icon and board[4]== icon and board[6] == icon:
        return True
    else:
        return False


def is_draw():
    if " " not in board:
        return True
    else:
        return False



while True:

    print_board()
    player_move("X")
    print_board()
    if player_win("X"):
        print("Player 1 wins..!")
        break
    elif is_draw():
        print("Game drawn")
        break
    player_move("O")
    if player_win("O"):
        print_board()
        print("Player 2 wins..!")
        break
    elif is_draw():
        print("Game drawn")
        break
 



    
