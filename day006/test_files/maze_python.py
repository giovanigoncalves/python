# Maze script for day006 in 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_tonorth():
    while not is_facing_north():
        turn_left()
        
def check():
    if not right_is_clear() and not front_is_clear():
        turn_left()
        if not front_is_clear():
            turn_left()
            move()
            turn_toleft()
            move()
            turn_tonorth()
            if front_is_clear():
                move()         
            else:
                turn_toleft()
                move()
                turn_tonorth()
                if front_is_clear():
                    move()
        else:
            move()
            if right_is_clear():
                turn_tonorth()
                move()
            else:
                turn_toright()
                move()
                turn_todown()
                while front_is_clear():
                    move()
    turn_tonorth()

def turn_toright():
    turn_tonorth()
    turn_left()
    turn_left()
    turn_left()
    
def turn_todown():
    turn_tonorth()
    turn_left()
    turn_left()

def turn_toleft():
    turn_tonorth()
    turn_left()
 
while not at_goal():
    turn_tonorth()
    check()
    if right_is_clear():
        turn_toright()
        while front_is_clear():
            move()
    elif front_is_clear():
        while front_is_clear():
            move()
    else:
        turn_toleft()
        if front_is_clear():
            turn_todown()
            if front_is_clear():
                while front_is_clear():
                    move()
        else:
            turn_todown()
            move()
            turn_toleft()
            move()
            while not right_is_clear():
                move()
         