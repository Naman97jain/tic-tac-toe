import random
import os

# A function that can print out a board
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


# A function that can take in a player input and assign their marker as 'X' or 'O'.
def player_input():
    player_1 = input('Pick a marker "X" or "O"').upper()
    while player_1 != 'X' and player_1 != 'O':
        player_1 = input('Pick a marker "X" or "O"').upper()
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    return (player_1,player_2)


# A function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position] = marker

# A function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    if ((board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark) or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark)):
        return True
    else:
        return False

# A function that uses the random module to randomly decide which player goes first.
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# A function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    if board[position] == ' ':
        return True
    return False


# A function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# A function that asks for a player's next position (as a number 1-9) and then uses the function space_check() to check
# if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    position = 0
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input("Choose (1-9) index to make your mark ")
    position = int(position)
    while not space_check(board,position):
        position = int(input("Enter another index from (1-9) as it is already filled!!"))
    return position


# A function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    while True:
        want_to_play = input("want to play again Y/N?")
        if want_to_play.upper()=='Y':
            return True
        elif want_to_play.upper()=='N':
            return False
        else:
            print("Please enter either Y or N")


# The main running script calling each function described above in a specific order
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

