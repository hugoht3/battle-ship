import random

##Started with a battle ship game


##First functions are just pirnting something to the terminal to see if they are working.

##To se more about the project check the video of the pyhthon 3 project.

## Remeber to use the \n to new line some code so it wont bug in HEROKU


######## REMEBER THAT FUNCTION HAVE THE : AFTER ITS MAKE
######## EG def example(example): <========== remnber the comma

## A lot of the code has \n for new lines in code just in case that in the video was explained to do so for the purpose of running correctly in the HEROKU MOCK terminal




def main():
    '''
    The function wich will start all other functions attached to the game
    '''
    print('Welcome to XX KAIAK-EXTREME XX ') # STILL NEED TO MAKE THE INPUT USEFUL LATER JUST FOR SHOW
    player_name = input("Please insert your name: \n")
    
    size = 5
    board1 = create_board(size)
    board2 = create_board(size)
    ship_size = 4
    place_ship(board1, ship_size)
    print_board(board1)
    place_ship(board2, ship_size)
    print("\nComputer Board\n")
    make_guess(board1, row, col)
    

def select_difficulty():
    '''
    Function that give us a difficulty selector
    ''' 
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Enter 1, 2 or 3")
        if choice in ['1' , '2', '3']:
            return in(choice)
        else:
            print("Invalid. Please select 1, 2 or 3.")



def select_difficulty(difficulty):
    '''
    Sets the board size, and ship size and number of turns based on the difficulty
    '''
    if difficulty == 1 :
        return 4, 3, 10
    elif difficulty == 2 :
        return 5, 3, 12
    elif difficulty == 3:
        return 6, 2, 14


def create_board(size):
    ''' 
    Creates a sort of board.
    '''
    return [['O'] * size for i in range(size)]



def print_board(board):
    '''
    This Function makes the board clear with no Commas OR braces 
    at the end.
    '''
    for row in board:
        print(" ".join(row))


def place_ship(board, size):
        '''
        Function that put the ships in place
        '''
        placement = random.choice(['$', 'X'])
        if placement == '$':
            row = random.randint(0, len(board) -1)
            col = random.randint(0, len(board) - size)
            for i in range(size):
                board[row][col + i] = 'X'
        else:
            row = random.randint(0, len(board) - size)
            col = random.randint(0, len(board) - 1)
            for i in range(size):
                board[row + i][col] = '$'
        

    
def make_guess(board, row, col):
    
    '''
    This Function will act as a guess marker when you play the game.
    '''
    if board[row][col] == '$':
        board[row][col] = 'X'
        return True
    elif board[row][col] == 'O':
        board[row][col] = '@'
        return False
    return None

def all_ships_sink(board):
   '''
    Function that stops the game when you LOSE or WIN
   '''
    for row in board:
       if '$' in row:
            return False
    return True

   if all_ships_sink(board):
       print("You Won")
       break


main()


## IF YOU MANAGE TO FINISH A PRESENTAGBLE PROJECT LATER THEM TRY THE COLORAMA THING THAT DICK TOLD YOU












