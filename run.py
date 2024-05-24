import random

def main():
    '''
    The function which will start all other functions attached to the game
    '''
    print('Welcome to XX BATTLE-SHIP XX')
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
    print_board_hidden(board2)

    previous_computer_guesses = set()

    while turns > 0:
        print(f'\nYou have {turns} turns left.')
        row = get_valid_int_input(f"Enter row (0-{size-1}): ", 0, size-1)
        col = get_valid_int_input(f"Enter column (0-{size-1}): ", 0, size-1)
        
        if make_guess(board2, row, col):
            print("You hit a ship!")
        else:
            print("You missed!")
        
        if all_ships_sunk(board2):
            print("You won!")
            break

        # Computer's turn to guess
        comp_row, comp_col = computer_guess(board1, previous_computer_guesses, size)
        if make_guess(board1, comp_row, comp_col):
            print(f"Computer hit your ship at ({comp_row}, {comp_col})!")
        else:
            print(f"Computer missed at ({comp_row}, {comp_col}).")
        
        if all_ships_sunk(board1):
            print("Computer won!")
            break

        turns -= 1

        # Clear the screen and reprint the boards
        print("\nPlayer's Board:")
        print_board(board1)
        
        print(f"\nEnemy Board ({enemy_name}):")
        print_board_hidden(board2)
    
    if turns == 0:
        print("You ran out of turns. Game over!")
    

def select_difficulty():
    '''
    Function that allows the player to select the difficulty level
    ''' 
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Enter 1, 2 or 3 \n")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid input. Please select 1, 2, or 3.")

def set_difficulty(difficulty):
    '''
    Sets the board size, ship size, and number of turns based on the difficulty
    '''
    if difficulty == 1:
        return 4, 2, 10  # Easy: Smaller board, fewer ships, more turns
    elif difficulty == 2:
        return 5, 3, 12  # Medium: Medium board, more ships, moderate turns
    elif difficulty == 3:
        return 6, 4, 14  # Hard: Larger board, most ships, more turns

def create_board(size):
    ''' 
    Creates a board with a given size.
    '''
    return [['O'] * size for _ in range(size)]

def print_board(board):
    '''
    Prints the board without commas or brackets.
    '''
    for row in board:
        print(" ".join(row))

def print_board_hidden(board):
    '''
    Prints the board with hidden ships for the enemy board display.
    '''
    for row in board:
        print(" ".join(['O' if cell == '$' else cell for cell in row]))

def place_ship(board, size):
    '''
    Function that places ships on the board.
    '''
    placement = random.choice(['horizontal', 'vertical'])
    if placement == 'horizontal':
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board) - size)
        for i in range(size):
            board[row][col + i] = '$'
    else:
        row = random.randint(0, len(board) - size)
        col = random.randint(0, len(board) - 1)
        for i in range(size):
            board[row + i][col] = '$'

def make_guess(board, row, col):
    '''
    This function handles the player's guess and updates the board.
    '''
    if board[row][col] == '$':
        board[row][col] = 'X'
        return True
    elif board[row][col] == 'O':
        board[row][col] = '@'
        return False
    return None

def computer_guess(board, previous_guesses, size):
    '''
    Make computer guess
    '''
    while True:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if (row, col) not in previous_guesses:
            previous_guesses.add((row, col))
            return row, col

def all_ships_sunk(board):
    '''
    Function that checks if all ships are sunk.
    '''
    for row in board:
        if '$' in row:
            return False
    return True

def get_valid_int_input(prompt, min_val, max_val):
    '''
    Function that gets a valid integer input within a specified range
    '''
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Invalid input. Please enter a number " +
                    f"between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

main()
