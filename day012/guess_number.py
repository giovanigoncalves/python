import os, random
from art import logo


def difficulty(level):
    if level == "easy":
        life = 10
    elif level == "hard":
        life = 5
    else:
        return "Invalid Answer!"
    return life
 
def compare(user_guess, pc_number):
    global life
    if user_guess == pc_number:
        return f"You got it! The answer was {pc_number}"
    elif user_guess > pc_number:
        life -= 1
        return "Too high."
    elif user_guess < pc_number:
        life -= 1
        return "Too low."
        
def play_game():
    global life
    os.system("clear")
    print(logo)
    print("\nWelcome to the Number Guessing Game!\n\n")
    print("I'm thinking of a number between 1 and 100.")

    pc_number = random.randint(1, 100)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    life = difficulty(level)
    if life == "Invalid Answer!":
        print(life)
        invalid = True
        while invalid:
            level = input("Choose a difficulty. Type 'easy' pr 'hard': ")
            life = difficulty(level)
            if life != "Invalid Answer!":
                invalid = False
            else:
                print(life)
                
    should_continue = True
    while should_continue:
        
        print(f"You have {life} attempts remaining to guess the number.")
        
        user_guess = int(input("Make a guess: "))
        if user_guess < 1 or user_guess > 100:
            invalid = True
            while invalid:
                print("Invalid answer!")
                user_guess = int(input("Make a guess: "))
                if user_guess > 1 or user_guess < 100:
                    invalid = False
                    
        res = compare(user_guess, pc_number)
        print(res)
        
        if user_guess == pc_number or life == 0:
            should_continue = False
            
    if life == 0:
        print("You do not have attempts anymore.\nYou Lose!")
        print(f"The correct answer was {pc_number}.")

    play_again = input("\nGuess again! Type 'y' or 'n': ")
    if play_again == 'y':
        play_game()
    elif play_again == 'n':
        print("Goodbye! See you!")
    else:
        invalid = True
        while invalid:
            print("Invalid answer!")
            play_again = input("\nGuess again! Type 'y' or 'n': ")
            if play_again == 'y':
                play_game()
            elif play_again == 'n':
                invalid = False
                print("Goodbye! See you!")
            
play_game()