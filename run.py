import random


def main():
    """
    The function which will start all other functions attached to the game.
    """
    print('Welcome to XX BATTLE-SHIP XX')
    player_name = get_valid_name_input()

    difficulty = select_difficulty()
    size, ship_size, turns = set_difficulty(difficulty)
    enemy_name = random.choice(["Pirates", "Robots", "Skeletons", "Aliens", "Ninjas"])

    # Initialize player and enemy boards
    board1 = create_board(size)
    board2 = create_board(size)

    # Place ships
    place_ship(board1, ship_size)
    place_ship(board2, ship_size)

    # Print initial game state
    print("\nPlayer's Board:")
    print_board(board1)

    print(f"\nEnemy Board ({enemy_name}):")
    print_board_hidden(board2)

    # Set to track previous guesses
    previous_computer_guesses = set()
    previous_player_guesses = set()

    # Main game loop
    while turns > 0:
        print(f'\nYou have {turns} turns left.')

        # Player's turn, ensuring no repeated moves
        row, col = get_unique_move(size, previous_player_guesses)

        # Player's guess
        if make_guess(board2, row, col):
            print("You hit a ship!")
        else:
            print("You missed!")

        # Check if player wins
        if all_ships_sunk(board2):
            print("You won!")
            break

        # Computer's turn to guess
        comp_row, comp_col = computer_guess(board1, previous_computer_guesses, size)
        if make_guess(board1, comp_row, comp_col):
            print(f"Computer hit your ship at ({comp_row}, {comp_col})!")
        else:
            print(f"Computer missed at ({comp_row}, {comp_col}).")

        # Check if computer wins
        if all_ships_sunk(board1):
            print("Computer won!")
            break

        turns -= 1

        # Reprint the boards after each round
        print("\nPlayer's Board:")
        print_board(board1)

        print(f"\nEnemy Board ({enemy_name}):")
        print_board_hidden(board2)

    if turns == 0:
        print("You ran out of turns. Game over!")


def get_unique_move(size, previous_guesses):
    """
    Ensures the player selects a unique move (not repeated).
    """
    while True:
        row = get_valid_int_input(f"Enter row (0-{size-1}): ", 0, size-1)
        col = get_valid_int_input(f"Enter column (0-{size-1}): ", 0, size-1)

        if (row, col) not in previous_guesses:
            previous_guesses.add((row, col))  # Track the move
            return row, col
        else:
            print("You already made that move. Try again.")


# Rest of the code remains unchanged (i.e., difficulty selection, board creation, ship placement, etc.)
def select_difficulty():
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Enter 1, 2, or 3: \n")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid input. Please select 1, 2, or 3.")


def set_difficulty(difficulty):
    if difficulty == 1:
        return 4, 2, 10  # Easy: Smaller board, fewer ships, more turns
    elif difficulty == 2:
        return 5, 3, 12  # Medium: Medium board, more ships, moderate turns
    elif difficulty == 3:
        return 6, 4, 14  # Hard: Larger board, most ships, more turns


def create_board(size):
    return [['O'] * size for _ in range(size)]


def print_board(board):
    for row in board:
        print(" ".join(row))


def print_board_hidden(board):
    for row in board:
        print(" ".join(['O' if cell == '$' else cell for cell in row]))


def place_ship(board, size):
    placement = random.choice(['horizontal', 'vertical'])
    if placement == 'horizontal':
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board) - size)
        place_horizontal_ship(board, row, col, size)
    else:
        row = random.randint(0, len(board) - size)
        col = random.randint(0, len(board) - 1)
        place_vertical_ship(board, row, col, size)


def place_horizontal_ship(board, row, col, size):
    for i in range(size):
        board[row][col + i] = '$'


def place_vertical_ship(board, row, col, size):
    for i in range(size):
        board[row + i][col] = '$'


def make_guess(board, row, col):
    if board[row][col] == '$':
        board[row][col] = 'X'
        return True
    elif board[row][col] == 'O':
        board[row][col] = '@'
        return False
    return None


def computer_guess(board, previous_guesses, size):
    while True:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if (row, col) not in previous_guesses:
            previous_guesses.add((row, col))
            return row, col


def all_ships_sunk(board):
    for row in board:
        if '$' in row:
            return False
    return True


def get_valid_int_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Invalid input. Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_valid_name_input():
    while True:
        name = input("Please insert your name: \n")
        if name.strip():
            return name
        else:
            print("Name cannot be empty. Please enter a valid name.")


if __name__ == "__main__":
    main()
