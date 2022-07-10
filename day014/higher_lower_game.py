import random
from art import logo, vs
from data import data
import os


def compare(res, dict1=dict(), dict2=dict()):
    if res == "a" and dict1["follower_count"] >= dict2["follower_count"]:
        return "correct A"
    elif res == "a" and dict1["follower_count"] <= dict2["follower_count"]:
        return "incorrect"
    elif res == "b" and dict1["follower_count"] <= dict2["follower_count"]:
        return "correct B"
    elif res == "b" and dict1["follower_count"] >= dict2["follower_count"]:
        return "incorrect"


def option(dict=dict()):
    return f"{dict['name']}, {dict['description']}, from {dict['country']}"


os.system("clear")

score = 0
n_data = len(data)
chosen1 = random.choice(data)
compareA = option(chosen1)
while n_data > 1:
    print(logo)
    
    if score > 0:
        print(f"You're right! Current score: {score}")
        
    print(f"Compare A: {compareA}")

    chosen2 = chosen1
    while chosen2 == chosen1:
        chosen2 = random.choice(data)

    print(vs)
    
    compareB = option(chosen2)
    print(f"Against B: {compareB}")

    res = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    answer = compare(res, chosen1, chosen2)
    if answer == "correct A":
        score += 1
        data.remove(chosen2)
        os.system("clear")
    elif answer == "correct B":
        score += 1
        chosen1 = chosen2
        compareA = compareB
        data.remove(chosen1)
        os.system("clear")
    else:
        os.system("clear")
        print(f"Sorry, that's wrong. Final score: {score}")
        print(f"{len(data)}")
        break
    
    n_data = len(data)
    if n_data == 1:
        print(f"\nYou got all right! You need to work too. Leave the social medias kkkk\n\n")
        print(f"Final score: {score}\n")
