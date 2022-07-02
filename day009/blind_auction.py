from art import logo
# To use system to clear previous output, 
# hiding the answer of the previous user.
import os 

# function to calc the highest value in the bids dict
def highest_bid(dict):
    highest = 0
    winner = ''
    for value in dict:
        if dict[value] > highest:
            highest = dict[value]
            winner = value
    print(f"The winer is {winner} with a bid of ${highest}.\n\n")
    
print(logo)
print("Welcome to the secret auction program.")

bids = {}
cont = True
while cont:
    name = input("what is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids[name] = bid
    
    res = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if res == 'yes':
        cont = True
        os.system("clear")
    elif res == 'no':
        cont = False
        os.system("clear")
    else:
        invalid = True
        while invalid:
            print("Invalid answer!")
            res = input("Are there any other bidders? Type 'yes' or 'no'.\n")
            if res in ["yes", "no"]:
                invalid = False
                os.system("clear")
                if res == "no":
                    cont = False
        
os.system("clear")        
highest_bid(bids)