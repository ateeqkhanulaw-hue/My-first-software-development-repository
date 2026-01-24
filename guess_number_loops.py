import random


def play_game():
    """Main game function using loops."""
    # Generate random number between 1-50
    secret_number = random.randint(1, 50)
    max_attempts = 7
    attempts = 0
    
    print("\n=== GUESS THE NUMBER ===")
    print("I'm thinking of a number between 1 and 50.")
    print(f"You have {max_attempts} attempts.\n")
    
    # WHILE LOOP - repeats until correct guess or out of attempts
    while attempts < max_attempts:
        attempts += 1
        
        # Get user guess
        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts} - Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            attempts -= 1  # Don't count invalid input
            continue
        
        # Check guess
        if guess == secret_number:
            print(f"\n🎉 Correct! You got it in {attempts} attempts!")
            return True
        elif guess < secret_number:
            print("Too low! Go higher. ⬆️")
        else:
            print("Too high! Go lower. ⬇️")
    
    # Out of attempts
    print(f"\n😢 Game Over! The number was {secret_number}")
    return False


def main():
    """Main function with play again loop."""
    print("\n" + "=" * 35)
    print("   WELCOME TO GUESS THE NUMBER!")
    print("=" * 35)
    
    # FOR LOOP - track statistics
    games_played = 0
    games_won = 0
    
    # WHILE LOOP - play again loop
    while True:
        if play_game():
            games_won += 1
        games_played += 1
        
        # Ask to play again
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    # Display final stats
    print("\n--- FINAL STATS ---")
    print(f"Games Played: {games_played}")
    print(f"Games Won: {games_won}")
    print("Thanks for playing! 👋")


if __name__ == "__main__":
    main()