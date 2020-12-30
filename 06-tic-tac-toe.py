def display_board(board):

    print("          |           |       ")
    print("   ",board[7],"   ", "|", "   ", board[8], "   " ,"|","   ", board[9],"   ")
    print("          |           |       ")

    print("------------------------------------")

    print("          |           |       ")
    print("   ",board[4],"   ", "|", "   ", board[5], "   " ,"|","   ", board[6],"   ")
    print("          |           |       ")

    print("------------------------------------")

    print("          |           |       ")
    print("   ",board[1],"   ", "|", "   ", board[2], "   " ,"|","   ", board[3],"   ")    
    print("          |           |       ")


def player_input():
    marker = " "

    while not(marker == "X" or marker == "O"):
        marker = input("\nEnter your choice (X and O): ").upper()

    player1 = marker
    if player1 == 'X':
        return ('X', 'O')
    return ('O', 'X')

def assign_marker(board, marker, position):
    board[position] = marker

def space_check(board, position):
    return board[position] == " "
    
def full_space_check(board):
    for i in range(1,10):
        if space_check(board,i):
           return False
    return True
     

def win_check(board, marker):
    return (
                (board[7] == marker and board[8] == marker and board[9] == marker) or
        (board[4] == marker and board[5] == marker and board[6] == marker) or
        (board[1] == marker and board[2] == marker and board[3] == marker) or 
        (board[1] == marker and board[5] == marker and board[9] == marker) or
        (board[3] == marker and board[5] == marker and board[7] == marker) or
        (board[1] == marker and board[4] == marker and board[7] == marker) or
        (board[3] == marker and board[6] == marker and board[9] == marker) or
        (board[2] == marker and board[5] == marker and board[8] == marker)
    )

from random import randint
def choose_first():
    flip = randint(0,1)
    if flip == 0:
        return "Player 1"
    return "Player 2"

def replay():
    play_again = input("\nDo you want to play again ('Yes or No'): ").lower()
    if play_again == "yes":
        return True
    return False

def player_position(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("\nEnter the position to place your marker: "))
        return position

print("Welcome to the Awsome Kannan's Multiplayer Tic Tac Toe game \n")

while True:
    tic_tac_toe_board = [" "]*10
    player1, player2 = player_input()
    print(f"\nPlayer one is selected to {player1}")
    print(f"Player two is seleced to {player2} \n")

    last_ask = input("\nAre you ready to beat your oppenent --> say in ('yes' or 'no'): ").lower()
    if last_ask == 'yes':
        ticTacToe = True
    elif last_ask == 'no':
        ticTacToe = False
    whos_turn = choose_first()

    while ticTacToe:
        if whos_turn == "Player 1":
            
            display_board(tic_tac_toe_board)
            position = player_position(tic_tac_toe_board)
            assign_marker(tic_tac_toe_board, player1, position)
            
            if win_check(tic_tac_toe_board, player1):
                display_board(tic_tac_toe_board)
                print("\nHooya Player One You won the match\n")
                ticTacToe = False
            else:
                if full_space_check(tic_tac_toe_board):
                    display_board(tic_tac_toe_board)
                    print("\nSo tough oppenent is it, Because it ends in draw\n")
                    break
                else:
                    whos_turn = "Player 2"
        else:
            display_board(tic_tac_toe_board)
            position= player_position(tic_tac_toe_board)
            assign_marker(tic_tac_toe_board, player2, position)


            if win_check(tic_tac_toe_board, player1):
                display_board(tic_tac_toe_board)
                print("\nHooya Player Two won the match\n")
                ticTacToe = False
            else:
                if full_space_check(tic_tac_toe_board):
                    display_board(tic_tac_toe_board)
                    print("\nSo tough oppenent is it, Because it ends in draw\n")
                    break
                else:
                    whos_turn = "Player 1"

    if not replay():
        break



