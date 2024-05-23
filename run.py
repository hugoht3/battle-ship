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
    
    difficulty = select_difficulty()
    size, ship_size, turns = set_difficulty(difficulty)
    enemy_name = random.choice(["Pirates", "Robots", "Skeletons", "Aliens", "Ninjas"])

    board1 = create_board(size)
    board2 = create_board(size)
    
    place_ship(board1, ship_size)
    place_ship(board2, ship_size)
    
    print("\nPlayer's Board:")
    print_board(board1)
    
    print(f"\nEnemy Board ({enemy_name}):")
    print_board(board2)

    while turns > 0:
        print(f'\nYou have {turns} turns left.')
        row = int(input(f"Enter row (0-{size-1}): "))
        col = int(input(f"Enter column (0-{size-1}): "))
        
        if make_guess(board2, row, col):
            print("You hit a ship!")
        else:
            print("You missed!")
        
        print("\nPlayer's Board:")
        print_board(board1)
        
        print(f"\nEnemy Board ({enemy_name}):")
        print_board(board2)
        
        if all_ships_sunk(board2):
            print("You won!")
            break
        
        turns -= 1
    
    if turns == 0:
        print("You ran out of turns. Game over!")
    

def select_difficulty():
    '''
    Function that give us a difficulty selector
    ''' 
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Enter 1, 2 or 3 \n")
        if choice in ['1' , '2', '3']:
            return int(choice)
        else:
            print("Invalid. Please select 1. Easy, 2. Medium or 3 Hard.")



def set_difficulty(difficulty):
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
    This function acts as a guess marker when you play the game.
    '''
    if board[row][col] == '$':
        board[row][col] = 'X'
        return True
    elif board[row][col] == 'O':
        board[row][col] = '@'
        return False
    return None

def all_ships_sunk(board):
    '''
    Function that checks if all ships are sunk.
    '''
    for row in board:
        if '$' in row:
            return False
    return True


main()


## IF YOU MANAGE TO FINISH A PRESENTAGBLE PROJECT LATER THEM TRY THE COLORAMA THING THAT DICK TOLD YOU












