import random 
def choose_word():
    words= ["python", "hangman", "programming","developer","learning","challange"]
    return random.choice(words)
def display_word(word,guessed_letters):
    display=""
    for letter in word:
        if letter in guessed_letters:
            display+=letter+ " "
        else:
            display+="- "
    return display.strip()
def hangman():
    print("Welcome to Hangman")
    secret_word=choose_word()
    guessed_letters=[]
    attempts_left=6
    while attempts_left >0:
        current_display=display_word(secret_word,guessed_letters)
        print(f"\nWord:{current_display}")
        guess=input("Guess a letter: ").lower()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                attempts_left -= 1
        else:
            print("Invalid input. Please enter a single letter.")

        if set(secret_word) <= set(guessed_letters):
            print("\nCongratulations! You guessed the word:", secret_word)
            break

        print(f"Attempts left: {attempts_left}")

    if attempts_left == 0:
        print("\nSorry, you ran out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    hangman()        
