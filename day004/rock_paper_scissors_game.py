rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
person = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
pc = random.randint(0, 2)

choices = [rock, paper, scissors]

print("Computer chose:")
print(choices[pc])

print("You chose:")
print(choices[person])

if choices[pc] == rock:
    if choices[person] == paper:
        print("\nYou Won!!!\n")
    elif choices[person] == rock:
        print("\nIt's a draw!\n")
    else:
        print("\nYou lose!\n")
        
elif choices[pc] == scissors:
    if choices[person] == rock:
        print("\nYou Won!!!\n")
    elif choices[person] == scissors:
        print("\nIt's a draw!\n")
    else:
        print("\nYou lose!\n")
        
        
else:
    if choices[person] == scissors:
        print("\nYou Win!!!\n")
    elif choices[person] == paper:
        print("\nIt's a draw!\n")
    else:
        print("\nYou lose!\n")
        