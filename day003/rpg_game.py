print('''
                                                ^             
                                               / \           ^
                         _,-~~~--~~~--._      (   \         / !
                     _,-'               `.__  (    \_.---._/   )
                   ,'                       `-(_` -'       `-. )   
                  /       "--..                \.'           `/  
                 ,             `-.              :  _  .-.  _  : 
                /                 ;             : (0).oYo.(0) ;
              /                    `             \.-'V'"'V'-./
             /                     '              \\^     ^//
    /\      /                      '     :    : .-'\\^   ^//
   ;  \    ;   /                  ,'  _.-`.    `. : \\^_^//
   ;   \   ;  ;`.               ,'~~-'     `.    `.`.`-.-'
    \   |_/   ;  `.        /-'/___.---.      `-.   `.`---.
     \       /     |      /____.---.)))         `-. `---.!
  akg \_____/      (____________))))\\\            `-.\\\\
                                 \\\\                
''')
print("Welcome to the Treasure Island.\nYour mission is to find a treasure.")
passo1 = input("You are in a cross road. On the left has a river. On the right has a forest.\nWhere do you want to go? [left or right]\n")

if "r" in passo1.lower():
    passo2 = input("You see a honeycombe on the tree. Will you take the honey? [Y or N]\n")
    if "n" in passo2.lower():
        passo3 = input("You see a strange person in the forest. Will you talk with him? [Y or N]\n")
        if "n" in passo3.lower():
            passo4 = input("You found a bike. Will you take it? [Y or N]\n")
            if "n" in passo4.lower():
                passo5 = print("A jaguar found you. Will you run or climb the tree? [run or climb]\n")
                if "r" in passo5.lower():
                    print("The jaguar ran faster and killed you.\n\nGAME OVER!\n")
                else:
                    print("The jaguar can climbed the tree and killed you.\n\nGAME OVER!\n")
            else:
                print("The strange saw you and hit you with a stone on the head.\n\nGAME OVER!\n")
        else: 
            passo4 = input("He asked if you want to go to his home in the forest. Will you go? [Y or N]\n")
            if "y" in passo4.lower():
                passo5 = input("On his house, the village is attacked by elephants. What do you do? [run, help, fight]")
                if passo5.lower() == "help":
                    print("The elephants killed you to.\n\nGAME OVER!\n")
                elif passo5.lower() == "fight":
                    print("Are you idiot? Do you know the size of an elephant? It killed you.\n\nGAME OVER!")
                else:
                    passo6 = input("You ran and fell in a hole. You see that it is a cave and you see a small light deeper in the cave. Do you want to check what it is or do you want to go out from the hole? [see or out]\n")
                    if passo6 == "out":
                        print("The strange found you and killed you because you ran from the village.\n\nGAME OVER!\n")
                    else:
                        print("It was a treasure! Congratulations!!! Now, you are a rich man in a forest!\n\nCONGRATULATION!!\n GAME OVER!!!\n")
            else:
                passo5 = input("You se a group of people. Will you ask for help? [Y or N]\n")
                if "y" in passo5.lower():
                    print("They were cannibals. You know what happened, didn't you?\nGAME OVER!\n")
                else:
                    passo6 = input("You see a wild pig running toward you. You climb a tree or fight the pig? [climb or fight]\n")
                    if "climb" == passo6.lower():
                        print("This was the tree with the honeycomb. The bees killed you.\nGAME OVER!\n")
                    else:
                        passo7 = input("The pig was Pumba, from Disney. Will you talk with pumba or leave him? [talk or leave]")
                        if "leave" == passo7.lower():
                            print("Pumba did not like it. He ran and killed you.\nGAME OVER!\n")
                        else:
                            print("It was a bad pumba. He killed you anyway.\nGAME OVER!\n")
    else:
        print("The bees did not like it and killed you.\nGAME OVER!\n")

else:
    passo2 = input("You see something shaking the water. Will you check what is it? [Y or N]\n")
    if "n" in passo2.lower():
        passo3 = input("You see a boat. Will you ride the boat? [Y or N]\n")
        if "n" in passo3.lower():
            passo4 = input("You see a woman drowning in the other side of the river. Will you swim through the river to help her? [Y or N]\n")
            if "n" in passo4.lower():
                passo5 = print("God is seen you do nothing and now you are not able to enter in the paradise anymore.\nGAME OVER!\n")
            else:
                print("You realized you do not know how to swim and you drown.\n\nGAME OVER!\n")
        else: 
            passo4 = input("A small alligator appers close to the boat. Will you jump? [Y or N]\n")
            if "y" in passo4.lower():
                print("The mother of the aligator was close and killed you.\n\nGAME OVER!\n")
            else:
                passo5 = input("The oar fell in the river. Will you use your hands? [Y or N]")
                if "y" in passo5.lower():
                    print("The aligator was still there and pull you to the river by the hands to kill you. \nGAME OVER!\n")
                else:
                    print("The river took you to a waterfall. You fell on that and died.\nGAME OVER!\n")
    else:
        print("It was an aligator. It bite you and pull you to the water to kill you. \nGAME OVER!\n")

                
                    
