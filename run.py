import random

##Started with a battle ship game


##First functions are just pirnting something to the terminal to see if they are working.

##To se more about the project check the video of the pyhthon 3 project.


score = {"player": 0, "computer": 0}

def main():
    '''
    The function wich will start all other functions attached to the game
    '''
    print('Welcome to XXXXXXX')
    player_name = input("Plase insert your name: \n")
    
    size = 5
    board = create_board(size)
    


    
    

def create_board(size):
    ''' 
    Creates a sort of board
    '''
    return [['O'] * size for i in range(size)]

def print_board(board):
    for row in board:
        print(" ".join(row))



board = create_board(5)
print_board(board)
#main()