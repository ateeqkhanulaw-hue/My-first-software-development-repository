# ============================================
# IMPORTING PYTHON'S BUILT-IN PACKAGES
# ============================================

import random  # Used to generate random numbers
import time    # Used to add delays for better user experience
import os      # Used to clear the terminal screen

# ============================================
# GAME CONFIGURATION CONSTANTS
# ============================================

# These constants can be easily modified to change game difficulty
MIN_NUMBER = 1      # Minimum number in the guessing range
MAX_NUMBER = 100    # Maximum number in the guessing range
MAX_ATTEMPTS = 10   # Maximum attempts allowed per game

# ============================================
# UTILITY FUNCTIONS
# ============================================

def clear_screen():
    """
    Clears the terminal screen for better visual presentation.
    
    Uses 'cls' command for Windows and 'clear' for Unix/Linux/Mac.
    The os.name variable returns 'nt' for Windows systems.
    """
    # Check the operating system and use appropriate clear command
    os.system('cls' if os.name == 'nt' else 'clear')


def display_welcome_message():
    """
    Displays the welcome message and game instructions.
    
    This function prints the game title and explains the rules
    to the player before starting the game.
    """
    print("=" * 50)
    print("       WELCOME TO THE NUMBER GUESSING GAME")
    print("=" * 50)
    print(f"\nI'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it.")
    print("After each guess, I'll tell you if you need to go higher or lower.")
    print("\n" + "-" * 50)


def get_player_name():
    """
    Prompts the player to enter their name.
    
    Returns:
        str: The player's name, or 'Player' if no name is entered.
    
    This personalizes the game experience by addressing the player by name.
    """
    name = input("\nEnter your name: ").strip()
    
    # If no name entered, use default name 'Player'
    if not name:
        name = "Player"
    
    return name


def generate_secret_number():
    """
    Generates a random secret number for the player to guess.
    
    Returns:
        int: A random integer between MIN_NUMBER and MAX_NUMBER (inclusive).
    
    Uses the random.randint() function from Python's random module.
    """
    # random.randint(a, b) returns a random integer N such that a <= N <= b
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    return secret


def get_player_guess(attempt_number):
    """
    Prompts the player for their guess and validates the input.
    
    Args:
        attempt_number (int): The current attempt number to display.
    
    Returns:
        int: The player's valid guess, or None if input is invalid.
    
    This function handles:
    - Prompting for input with attempt number
    - Converting string input to integer
    - Validating the guess is within the allowed range
    - Handling non-numeric input errors
    """
    try:
        # Prompt user and convert input to integer
        guess = int(input(f"\nAttempt {attempt_number}/{MAX_ATTEMPTS} - Enter your guess: "))
        
        # Validate guess is within allowed range
        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
            return None  # Return None to indicate invalid input
        
        return guess
    
    except ValueError:
        # Handle case where input cannot be converted to integer
        print("Invalid input! Please enter a whole number.")
        return None


def provide_hint(guess, secret_number):
    """
    Provides a hint to the player based on their guess.
    
    Args:
        guess (int): The player's current guess.
        secret_number (int): The secret number to guess.
    
    Returns:
        bool: True if the guess is correct, False otherwise.
    
    This function compares the guess with the secret number and
    provides feedback to guide the player toward the correct answer.
    """
    # Calculate the difference to determine how close the guess is
    difference = abs(secret_number - guess)
    
    if guess == secret_number:
        # Correct guess!
        return True
    
    elif guess < secret_number:
        # Guess is too low
        if difference <= 5:
            print("Too low, but you're very close! 🔥")
        elif difference <= 15:
            print("Too low, getting warmer! ⬆️")
        else:
            print("Too low! Go higher! ⬆️⬆️")
    
    else:
        # Guess is too high
        if difference <= 5:
            print("Too high, but you're very close! 🔥")
        elif difference <= 15:
            print("Too high, getting warmer! ⬇️")
        else:
            print("Too high! Go lower! ⬇️⬇️")
    
    return False


def calculate_score(attempts_used):
    """
    Calculates the player's score based on attempts used.
    
    Args:
        attempts_used (int): Number of attempts taken to guess correctly.
    
    Returns:
        int: The calculated score (higher is better).
    
    Scoring formula:
    - Base score of 1000 points
    - Minus 100 points for each attempt used
    - Minimum score is 100 points
    """
    # Calculate score: fewer attempts = higher score
    score = 1000 - (attempts_used * 100)
    
    # Ensure minimum score of 100
    if score < 100:
        score = 100
    
    return score


def display_win_message(player_name, attempts, score):
    """
    Displays a congratulatory message when the player wins.
    
    Args:
        player_name (str): The player's name.
        attempts (int): Number of attempts used.
        score (int): The player's final score.
    """
    print("\n" + "🎉" * 20)
    print(f"\nCONGRATULATIONS, {player_name.upper()}!")
    print(f"You guessed the number in {attempts} attempt(s)!")
    print(f"Your score: {score} points")
    print("\n" + "🎉" * 20)
    
    # Add a small delay for dramatic effect
    time.sleep(1)


def display_lose_message(player_name, secret_number):
    """
    Displays a message when the player runs out of attempts.
    
    Args:
        player_name (str): The player's name.
        secret_number (int): The secret number that was to be guessed.
    """
    print("\n" + "😢" * 20)
    print(f"\nSorry, {player_name}! You've run out of attempts.")
    print(f"The secret number was: {secret_number}")
    print("Better luck next time!")
    print("\n" + "😢" * 20)


def play_again():
    """
    Asks the player if they want to play another game.
    
    Returns:
        bool: True if player wants to play again, False otherwise.
    
    Accepts 'y', 'yes', 'n', 'no' (case-insensitive) as valid inputs.
    """
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def play_game(player_name):
    """
    Main game loop that handles a single round of the guessing game.
    
    Args:
        player_name (str): The player's name.
    
    Returns:
        int: The player's score (0 if they lost).
    
    This function:
    1. Generates a secret number
    2. Loops through attempts
    3. Gets and validates player guesses
    4. Provides hints
    5. Determines win/lose condition
    """
    # Generate the secret number for this round
    secret_number = generate_secret_number()
    
    # Track the number of attempts used
    attempts_used = 0
    
    # Main game loop - continues until max attempts reached
    while attempts_used < MAX_ATTEMPTS:
        # Increment attempt counter
        attempts_used += 1
        
        # Get player's guess
        guess = get_player_guess(attempts_used)
        
        # If invalid input, don't count this attempt
        if guess is None:
            attempts_used -= 1  # Give back the attempt
            continue
        
        # Check if guess is correct and provide hint
        if provide_hint(guess, secret_number):
            # Player won!
            score = calculate_score(attempts_used)
            display_win_message(player_name, attempts_used, score)
            return score
    
    # Player ran out of attempts
    display_lose_message(player_name, secret_number)
    return 0


def display_final_stats(games_played, total_score, wins):
    """
    Displays final statistics when the player quits.
    
    Args:
        games_played (int): Total number of games played.
        total_score (int): Cumulative score across all games.
        wins (int): Number of games won.
    """
    print("\n" + "=" * 50)
    print("            FINAL STATISTICS")
    print("=" * 50)
    print(f"  Games Played:  {games_played}")
    print(f"  Games Won:     {wins}")
    print(f"  Win Rate:      {(wins/games_played*100) if games_played > 0 else 0:.1f}%")
    print(f"  Total Score:   {total_score} points")
    print("=" * 50)
    print("\nThank you for playing! Goodbye! 👋")


# ============================================
# MAIN PROGRAM ENTRY POINT
# ============================================

def main():
    """
    Main function that orchestrates the entire game.
    
    This is the entry point of the program. It:
    1. Clears the screen and shows welcome message
    2. Gets the player's name
    3. Runs game rounds until player quits
    4. Tracks and displays statistics
    """
    # Clear screen for fresh start
    clear_screen()
    
    # Display welcome message and instructions
    display_welcome_message()
    
    # Get player's name for personalization
    player_name = get_player_name()
    print(f"\nHello, {player_name}! Let's start the game!")
    
    # Initialize statistics tracking variables
    games_played = 0    # Counter for total games
    total_score = 0     # Cumulative score
    wins = 0            # Counter for wins
    
    # Main program loop - continues until player chooses to quit
    while True:
        # Small delay before starting new game
        time.sleep(1)
        
        # Play one round of the game
        score = play_game(player_name)
        
        # Update statistics
        games_played += 1
        total_score += score
        if score > 0:  # Score > 0 means player won
            wins += 1
        
        # Ask if player wants to continue
        if not play_again():
            break
        
        # Clear screen for new game
        clear_screen()
        print(f"Alright {player_name}, let's play again!")
    
    # Display final statistics before exiting
    display_final_stats(games_played, total_score, wins)


# ============================================
# PROGRAM EXECUTION
# ============================================

# This ensures the main() function only runs when the script
# is executed directly, not when imported as a module
if __name__ == "__main__":
    main()