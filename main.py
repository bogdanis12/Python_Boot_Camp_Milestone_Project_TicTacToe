import random
def display_board(board):
    # Function to clear the output
    print('\n'*100)
    #Design a simple table to play TicTacToe
    print(board[7] + '|' + board[8] + '|' + board[9] + '|')
    print(board[4] + '|' + board[5] + '|' + board[6] + '|')
    print(board[1] + '|' + board[2] + '|' + board[3] + '|')

def player_input():
    #Collect the input from the player limited to X or O with upper case
    marker = ''
    while marker != 'X' and marker !='O':
        marker = input('Player 1 chose X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    return player1,player2

def place_marker(board,marker,position):
    #Finding the position of the player
    board[position] = marker

def win_check(board, mark):
    #Checking the posibilities to win
    if board[1]==mark and board [2] == mark and board[3] == mark: #bottom line
        return True
    elif board[4]==mark and board[5]==mark and board[6]==mark: #middle line
        return True
    elif board[7]==mark and board[8]==mark and board[9]==mark: #top line
        return True
    elif board[1]==mark and board[4]==mark and board[7]==mark: #across left line
        return True
    elif board[2]==mark and board[5]==mark and board[8]==mark: #across middle line
        return True
    elif board[3]==mark and board[6]==mark and board[9]==mark: #across right line
        return True
    elif board[1]==mark and board[5]==mark and board[9]==mark: #main diagonal
        return True
    elif board[3]==mark and board[5]==mark and board[7]==mark:#second diagonal
        return True
    return False

def choose_first():
    #determing which player will be the first using the random.randomint()
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'

def space_check(board,position):
    #checking if the position is blank or not, it will return True or False
    return board[position] == ' '

def full_board_check(board):
    #Checking if the board is full
    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full
    return True

def player_choice(board):
    #Putting the player to choose between 1-9 position that we have on the board
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position between 1-9: '))
    return position

def replay():
    choice = input("Play again? Enter Yes or No: ")
    return choice == 'yes'

print("Welcome to Tic Tac Toe")

while True:
    global turn
    #play the game
    #set everything up, board, who is firt, what markers they choose
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first')
    play_game  = input('Ready to play? Answer with y or n: ')
    if play_game == 'y':
        game_on = True
    else:
        game_on=False
    #game play
    while game_on:
        if turn == 'Player1':
            #show the board
            display_board(the_board)
            #choose position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 won!')
                game_on = False
            # or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is tied')
                    game_on = False
                else:
                    turn = 'Player2'
        else:
            # show the board
            display_board(the_board)
            # choose position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player2_marker, position)
            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 won!')
                game_on = False
            # or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is tied')
                    game_on = False
                else:
                    turn = 'Player1'

    if not replay():
        break
    
