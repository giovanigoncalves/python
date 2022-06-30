from random import choice
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = choice(word_list)

print(f"{logo}")

display = []
for letter in chosen_word:
    display += "_"
guesses = []
lives = 6
end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()
    
    while guess in guesses:
        print(f"\nYou already guesses {guess}. Try another.\n")
        guess = input("Guess a letter: ").lower()
    
    guesses += guess
            
    if guess in chosen_word:
        for pos in range(len(chosen_word)):
            if chosen_word[pos] == guess:
                display[pos] = guess
    else:
        print(f'There is no "{guess}" in the word. You lose a life.')
        lives -= 1
    
    if lives == 0:
        print("\nYou lose!\n")
        end_game = True
  
    if "_" not in display:
        end_game = True
        print("You've won!")

    print(f"{' '.join(display)}")

    print(stages[lives])
    
print(f'The correct word is "{chosen_word}"!\n\n')

     