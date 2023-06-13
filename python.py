def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
test = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def player_input():
    marker = " "
    while marker not in ["X", "O"]:
        marker = input("Choose your marker please (X or O)").upper()
    player1 = marker
    player2 = "O" if player1 == "X" else "X"
    return player1, player2
player1_marker, player2_marker = player_input()
print("Player1 is: ", player1_marker)
print("Player2 is: ", player2_marker)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (
        (board[1]==board[2]==board[3]==mark) or
        (board[4]==board[5]==board[6]==mark) or
        (board[7]==board[8]==board[9]==mark) or
        (board[1]==board[4]==board[7]==mark) or
        (board[2]==board[5]==board[8]==mark) or
        (board[3]==board[6]==board[9]==mark) or
        (board[1]==board[5]==board[9]==mark) or
        (board[3]==board[5]==board[7]==mark)
    )

import random
import itertools
player = ["Player 1", "Player 2"]
player_iterator = itertools.cycle(player)

def choose_first():
    player = random.randint(1, 2)
    if player == 1:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    if board[position]!=' ':
        return True

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board, marker):
    position = int(input("Make yor next move"))
    while space_check(board, position) is True or position not in range(1,10):
        return "This position is taken, please choose another one"
    else:
        place_marker(board, marker, position)

def replay():
    question = input('Would you like to play again?')
    if question.lower() == 'yes':
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " goes first")
    play_game = input("Are you ready to play? y or n")
    if play_game[0].lower() == "y":
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == "Player 1":
            display_board(board)
            player_choice(board, player1_marker)
            if win_check(board, player1_marker):
                display_board(board)
                print("Congratulations! Player 1 wins!")
                game_on = False
            elif full_board_check(board):
                display
        if turn == "Player 2":
            display_board(board)
            player_choice(board, player2_marker)
            if win_check(board, player2_marker):
                display_board(board)
                print("Congratulations! Player 2 wins!")
                game_on = False
            elif full_board_check(board):
                display