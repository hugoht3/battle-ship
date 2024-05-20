import random

##Started with a battle ship game


##First functions are just pirnting something to the terminal to see if they are working.

##To se more about the project check the video of the pyhthon 3 project.

## Remeber to use the \n to new line some code so it wont bug in HEROKU


######## REMEBER THAT FUNCTION HAVE THE : AFTER ITS MAKE
######## EG def example(example): <========== remnber the comma

## A lot of the code has \n for new lines in code just in case that in the video was explained to do so for the purpose of running correctly in the HEROKU MOCK terminal


score = {"player": 0, "computer": 0}  #took this from the project portifolio video used for a start on the project be sure to delete it

def main():
    '''
    The function wich will start all other functions attached to the game
    '''
    print('Welcome to XXXXXXX') # STILL NEED TO MAKE THE INPUT USEFUL LATER JUST FOR SHOW
    player_name = input("Please insert your name: \n")
    
    size = 5
    board1 = create_board(size)
    board2 = create_board(size)
    ship_size = 4
    place_ship(board1, ship_size)
    print_board(board1)
    place_ship(board2, ship_size)
    print("\nComputer Board\n")
    make_guess(board, row, col)
    


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

    # manage to have the placement of ships done with a LOADS OF F>>>>>>>>> HELP
# OMG


'''
LOOP THAT MAKES THE GAME KEEP RUNNING UNTILL LOSE OR WIN
'''
turns = 6   # MADE A NUMBER OF TURNS BUT INTENT TO HAVE A DIFICULTY SELECTOR THAT ILL AFFECT THAT NUMBER LATER
while turns > 0:
    print(f'\nYou have {turns} left.')
    row = input("Enter row")
    col = input("Enter Column")
    if make_guess(board, row, col):
        print("You Hit it")
    else:
        print("Missed It")
print(board)


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





#def test():
    #while True:
    # Code that you want to execute at least once
        #user_input = input("Enter a positive number: ")
        #number = int(user_input)
    
    # Check the condition to determine whether to continue looping
       #if number > 0:
            #break  # Exit the loop if the condition is met
    
    #print("Invalid input. Please try again.")

    #print(f"You entered a positive number: {number}")

#test()





#main()
#print_board(board)
#place_ship(board)
# Simulating a do-while loop in Python


