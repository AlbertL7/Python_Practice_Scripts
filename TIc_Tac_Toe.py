from pyfiglet import figlet_format
from termcolor import colored

ascii_art = figlet_format("Tic Tac Toe", font = 'doh', width = 100000)

print(ascii_art)

board = {'7':' ','8': ' ','9':' '
        ,'4':' ','5':' ','6':' ',
        '1':' ','2':' ','3':' '}

move = ' '
player1 = colored("X", "red")
player2 = colored("O", "blue")
    
print(f'player 1 is "{player1}" and player 2 is "{player2}"')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def board_positions():
    print('\n\t\t\tBoard Positions')
    print('\t\t\t~~~~~~~~~~~~~~~')
    print('\t\t\t7 |8 |9  ')
    print('\t\t\t--------')
    print('\t\t\t4 |5 |6  ')
    print('\t\t\t--------')
    print('\t\t\t1 |2 |3  ')

def board_setup(ttt_board):
    print(board['7'],' |',  board['8'],' |',  board['9'])
    print('------------')
    print(board['4'],' |', board['5'], ' |',  board['6'])
    print('------------')
    print(board['1'],' |',  board['2'],' |',  board['3'])
      
def gameon():
    choice = 'Wrong'
    while choice not in ['Y','N']:
        
        choice = input('Would you like to start / restart the game (Y or N): ').upper()
        
        if choice not in ['Y','N']:
            print('Sorry I dont understand, please choose Y or N ')
            
    if choice == 'Y':
        return True
    else:
        return False  
    
def clear_board():
    for key in board:
        board[key] = ' '
        
def clear_screen():
    print('\n' * 100)
    
def ttt_game(): 
    count = 0

    turn_Player1 = True
    
    while count in range(0,9):
         
        print(board_positions())
        board_setup(board)    
        move = input('\nSelect a Position (1-9): ')
        
        if move not in ['1','2','3','4','5','6','7','8','9']:
            move = input('Please select a valid position (1-9): ')

        if board[move] != ' ':
            print('Really... That move is already taken, choose another one!!')
            continue
                            
        if turn_Player1:
            board[move] = player1
        else:
            board[move] = player2
            
        count += 1

        turn_Player1 = not turn_Player1
               
        if count >=5:
            if board['7'] == board['8'] == board['9'] != ' ':
                winner = player1 if board['7'] == player1 else player2
                print(board_setup(board))
                print(colored(f'Player {"1" if winner == player1 else "2"} wins!', 'red' if winner == player1 else 'blue'))
                return
            elif board['4'] == board['5'] == board['6'] != ' ':
                winner = player1 if board['4'] == player1 else player2
                print(board_setup(board))
                print(colored(f'Player {"1" if winner == player1 else "2"} wins!', 'red' if winner == player1 else 'blue'))
                return
            elif board['1'] == board['2'] == board['3'] != ' ':
                winner = player1 if board['1'] == player1 else player2
                print(board_setup(board))
                print(colored(f'Player {"1" if winner == player1 else "2"} wins!', 'red' if winner == player1 else 'blue'))
                return
            elif board['1'] == board['5'] == board['9'] != ' ':
                winner = player1 if board['1'] == player1 else player2
                print(board_setup(board))
                print(colored(f'Player {"1" if winner == player1 else "2"} wins!', 'red' if winner == player1 else 'blue'))
                return
            elif board['7'] == board['5'] == board['3'] != ' ':
                winner = player1 if board['7'] == player1 else player2
                print(board_setup(board))
                print(colored(f'Player {"1" if winner == player1 else "2"} wins!', 'red' if winner == player1 else 'blue'))
                return
            elif board['7'] == board['4'] == board['1'] != ' ':
                winner = player1 if board['7'] == player1 else player2
                print(board_setup(board))
                print(colored(f'Player {"1" if winner == player1 else "2"} wins!', 'red' if winner == player1 else 'blue'))
                return
            elif board['8'] == board['5'] == board['2'] != ' ':
                winner = player1 if board['8'] == player1 else player2
                print(board_setup(board))
                print(colored(f'Player {"1" if winner == player1 else "2"} wins!', 'red' if winner == player1 else 'blue'))
                return
            elif board['9'] == board['6'] == board['3'] != ' ':
                winner = player1 if board['9'] == player1 else player2
                print(board_setup(board))
                print(colored(f'Player {"1" if winner == player1 else "2"} wins!', 'red' if winner == player1 else 'blue'))
                return

    if count == 9:
        print("It's a tie!")
        return
                                  
play_game = True

while play_game:
    print(ttt_game())
    play_game = gameon() 
    clear_board()                       
    clear_screen()
    
    
