from art import logo
import os
from random import randint
from time import sleep


def ask_card(player):
    card = randint(1, 13)
    if card > 10:
        card = 10
    elif card == 1:
        if (sum(player) + 11) > 21:
            card = 1
        else:
            card = 11
    player.append(card)    
    return player
                    
def pc_jogando(pc):
    while sum(pc) < 18:
        pc = ask_card(pc)
    return pc

def pc_joga(pc):
    if sum(pc) < 18:
        pc = ask_card(pc)
    return pc

def compare(you_score, pc_score):
    if pc_score > 21:
        return "Computer went over!\nYou Win!"
    elif you_score > 21:
        return "You went over!\n You Lose!"
    elif you_score == pc_score:
        return "It's draw!"
    elif pc_score == 21:
        return "Computer won with a Blackjack!\nYou Lose!"
    elif you_score == 21:
        return "You won with a Blackjack!\nYou Win!"
    elif you_score > pc_score:
        return "You win!"
    else:
        return "You lose!"
        

def blackjack():
    os.system("clear")
    print(logo)

    you = []
    pc = []

    for _ in range(2):
        you = ask_card(you)
        pc = ask_card(pc)
        
    print(f"Computer's first card: {pc[0]}")

    should_continue = True
    while should_continue:

        print(f"Your cards: {you}, current score: {sum(you)}")
        if sum(pc) <= 17:
            pc = ask_card(pc)
            sleep(.3)
            print(f"    Computer got a card")
        elif sum(pc) > 21:
            should_continue = False
            
        if sum(you) > 21:
            should_continue = False
        else:
            sleep(.3)
            res = input("Type 'y' to get another card or type 'n' to pass: ")       
            if res == 'y':
                you = ask_card(you)
                sleep(.3)
                print(f"    You got the card: {you[-1]}")
                pc = pc_joga(pc)
                
            elif res == 'n':
                pc = pc_jogando(pc)
                should_continue = False
            else:
                invalid = True
                while invalid:
                    res = input("Type 'y' to get another card, type 'n' to pass: ")
                    if res == 'y':
                        invalid = False
                    elif res == 'n':
                        invalid = False
                        should_continue = False

    sleep(.3)
    print(f"\n\n    Your final hand: {you}, final score: {sum(you)}")
    sleep(.3)
    print(f"    Computer's final hand: {pc}, final score: {sum(pc)}\n\n")

    sleep(.5)

    you_score = sum(you)
    pc_score = sum(pc)
    
    print(compare(you_score, pc_score))
    
    invalid = True
    while invalid:
        new_game = input("\n\nDo you want to go again? Type 'y' or 'n': ")
        if new_game == 'y':
            invalid = False
            blackjack()
        elif new_game == 'n':
            invalid = False
            print("GoodBye")
        
blackjack()