from random import randint

def print_game_intro(min_value, max_value, attempts_left):
    """
    Prints the game introduction and rules based on selected difficulty.

    Parameters:
    min_value (int): Lower bound of the guessing range
    max_value (int): Upper bound of the guessing range
    attempts_left (int): Number of allowed guesses
    """
    text = f'''\n\n
    Hello!
    Let's play a game! I will choose a random number between {min_value} and {max_value},
    and you have to guess it. You only have {attempts_left} attempts.
    Good luck!\n
    '''
    print(text)


def is_correct_guess(target_number, player_guess):
    """
    Checks if the guessed number is equal to the target number.

    Parameters:
    target_number (int): Number chosen by the computer
    player_guess (int): Number guessed by the player

    Returns:
    bool: True if guessed correctly, False otherwise
    """
    return target_number == player_guess


def get_player_guess(min_value, max_value):
    """
    Prompts the player to enter a guess within a specific range.

    Parameters:
    min_value (int): Lower bound of the guessing range
    max_value (int): Upper bound of the guessing range

    Returns:
    int: The guessed number entered by the player
    """
    return int(input(f'\nGuess a number between {min_value} and {max_value}: '))


def compare_guess(target_number, player_guess):
    """
    Compares the guessed number to the target number.

    Parameters:
    target_number (int): Number chosen by the computer
    player_guess (int): Number guessed by the player

    Returns:
    str: 'same' if equal, 'higher' if the target number is greater,
         'lower' if the target number is smaller
    """
    if target_number == player_guess:
        return 'same'
    elif target_number > player_guess:
        return 'higher'
    else:
        return 'lower'


def choose_difficulty():
    """
    Displays difficulty options and returns selected game settings.

    Returns:
    tuple: (min_value, max_value, attempts_left)
    """
    print('\nDifficulty levels:')
    print('1. Easy')
    print('2. Medium')
    print('3. Hard')
    print('4. Extreme')
    print('5. Custom')

    diff = int(input('Choose a difficulty level (1–5): '))
    if diff == 1:
        return (1, 20, 5)
    elif diff == 2:
        return (1, 100, 10)
    elif diff == 3:
        return (1, 100, 5)
    elif diff == 4:
        return (1, 1000, 5)
    elif diff == 5:
        min_value = int(input('Enter the minimum value: '))
        max_value = int(input('Enter the maximum value: '))
        attempts = int(input('Enter the number of attempts: '))
        return (min_value, max_value, attempts)


# --- Main Program Execution ---

# Get difficulty settings from the player
min_value, max_value, attempts_left = choose_difficulty()

# Generate a random number within the range
target_number = randint(min_value, max_value)

# Initialize guess
player_guess = 0

# Print introduction and rules
print_game_intro(min_value, max_value, attempts_left)

# Game loop
while not is_correct_guess(target_number, player_guess):
    player_guess = get_player_guess(min_value, max_value)
    result = compare_guess(target_number, player_guess)

    if result == "higher":
        print(f'The number is higher than {player_guess}. {attempts_left - 1} attempts left.')
        if min_value < player_guess:
            min_value = player_guess  # Adjust lower bound
    elif result == "lower":
        print(f'The number is lower than {player_guess}. {attempts_left - 1} attempts left.')
        if max_value > player_guess:
            max_value = player_guess  # Adjust upper bound

    attempts_left -= 1

    if attempts_left == 0:
        print(f"You've run out of attempts. You lost! The correct number was {target_number}.")
        exit(1)

# If guessed correctly
print(f"Well done! Your guess is correct. The number was {target_number}.")
