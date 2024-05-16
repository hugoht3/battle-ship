import random

##Started with a battle ship game


##First functions are just pirnting something to the terminal to see if they are working.

##To se more about the project check the video of the pyhthon 3 project.


score = {"player": 0, "computer": 0}

def main():
    '''
    The function wich will start all other functions attached to the game
    '''
    size = 5
    board = create_board(size)
    
    print('Welcome to XXXXXXX')
    player_name = input("Plase insert your name: \n")
    #get_non_numeric_input(player_name)

def create_board(size):
    return [['O'] * size for i in range(size)]




board = create_board(5)
print(board)