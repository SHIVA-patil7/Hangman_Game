import random

def hangman():
    words = ['python', 'java', 'kotlin', 'javascript']  # List of possible words
    word = random.choice(words)  # Randomly select a word from the list
    guessed_word = ['_'] * len(word)  # Create a list of underscores representing unguessed letters
    guessed_letters = []  # To track guessed letters
    tries = 6  # The number of incorrect guesses allowed

    print("Welcome to Hangman!")

    # Game loop: Runs until the player either wins or loses
    while tries > 0:
        print("\nWord:", ' '.join(guessed_word))  # Display the word with guessed letters
        print("Guessed letters:", ', '.join(guessed_letters))  # Display guessed letters
        print(f"Tries left: {tries}")  # Display the number of tries left

        guess = input("Enter a letter: ").lower()  # Get user input (converted to lowercase)
        
        # Check if the guessed letter was already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)  # Add the guess to the guessed letters list

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            # Update the display of the word with the guessed letter
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            tries -= 1  # Deduct a try if the guess is incorrect

        # Check if the player has won (all letters have been guessed)
        if '_' not in guessed_word:
            print(f"\nCongratulations! You guessed the word '{word}'!")
            break
    else:
        # This part runs if the player runs out of tries
        print(f"\nGame over! The word was '{word}'. Better luck next time!")

# Call the hangman function to start the game
hangman()
