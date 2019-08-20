import random
import os

def display_board(board):
    os.system('cls')
    print('    '+'|'+'    '+'|'+'    ')
    print('  '+board[7]+' '+'|'+'  '+board[8]+' '+'|'+'  '+board[9]+' ')
    print('    '+'|'+'    '+'|'+'    ')
    print('-----------------')
    print('    '+'|'+'    '+'|'+'    ')
    print('  '+board[4]+' '+'|'+'  '+board[5]+' '+'|'+'  '+board[6]+' ')
    print('    '+'|'+'    '+'|'+'    ')
    print('-----------------')
    print('    '+'|'+'    '+'|'+'    ')
    print('  '+board[1]+' '+'|'+'  '+board[2]+' '+'|'+'  '+board[3]+' ')
    print('    '+'|'+'    '+'|'+'    ')

def player_input():
    player_1 = input('Pick a marker "X" or "O"').upper()
    while player_1 != 'X' and player_1 != 'O':
        player_1 = input('Pick a marker "X" or "O"').upper()
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    return (player_1,player_2)


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if ((board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark) or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark)):
        return True
    else:
        return False

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    if board[position] == ' ':
        return True
    return False

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input("Choose (1-9) index to make your mark ")
    position = int(position)
    while not space_check(board,position):
        position = int(input("Enter another index from (1-9) as it is already filled!!"))
    return position

def replay():
    while True:
        want_to_play = input("want to play again Y/N?")
        if want_to_play.upper()=='Y':
            #player_1, player_2 = player_input()
            return True
        elif want_to_play.upper()=='N':
            return False
        else:
            print("Please enter either Y or N")


print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    status = input("Are you ready: Y/N?")
    if status.upper() == 'Y':
        game_on = True
    elif status.upper() == 'N':
        game_on = False
    if game_on:
        player_1, player_2 = player_input()
        first = choose_first()
        print(f'Player_1: {player_1}')
        print(f'Player_2: {player_2}')
    while game_on:

        if first == 'Player 1':
            print(f"{first}'s turn'")
            position = player_choice(board)
            # if space_check(board, position):
            place_marker(board, player_1, position)
            display_board(board)
            first = 'Player 2'
            if (full_board_check(board)):
                print("Tied!!")
                break
            elif (win_check(board, player_1)):
                print("Player_1 Won!!!!")
                break

        # Player2's turn.
        if first == 'Player 2':
            print(f"{first}'s turn'")
            position = player_choice(board)
            # print("Position:",position)
            # if space_check(board, position):
            place_marker(board, player_2, position)
            display_board(board)
            first = 'Player 1'
            if (full_board_check(board)):
                print("Tied!!")
                break
            elif (win_check(board, player_2)):
                print("Player_2 Won!!!!")
                break

    if not replay():
        break

