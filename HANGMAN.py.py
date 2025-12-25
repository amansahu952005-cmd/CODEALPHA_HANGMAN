import random

def play_hangman():
    # --- Setup ---
    # 1. List of 5 predefined words
    words = ["python", "logic", "snake", "input", "while"]
    
    # 2. Select a random word
    secret_word = random.choice(words)
    
    # 3. Initialize game variables
    attempts_left = 6
    guessed_letters = []
    
    print("--- Welcome to Simple Hangman ---")
    print(f"I have chosen a word. You have {attempts_left} incorrect guesses allowed.")

    # --- Game Loop ---
    while attempts_left > 0:
        
        # 4. Display current state of the word
        # We build a new string every loop to show known letters vs underscores
        display_state = ""
        missing_letters = 0
        
        for char in secret_word:
            if char in guessed_letters:
                display_state += char + " "
            else:
                display_state += "_ "
                missing_letters += 1
        
        print(f"\nWord: {display_state}")
        
        # Check Win Condition
        if missing_letters == 0:
            print("\n🎉 Congratulations! You guessed the word!")
            break
        
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Basic validation (ensure single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue
            
        # Check if already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue
            
        # Add to history
        guessed_letters.append(guess)
        
        # Check if guess is correct or incorrect
        if guess in secret_word:
            print(f"Yes! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"Attempts remaining: {attempts_left}")

    # --- End Game ---
    if attempts_left == 0:
        print(f"\n💀 Game Over! The word was: {secret_word}")

# Run the game
play_hangman()