#TODO: Create a letter using starting_letter.txt

with open("./Input/Letters/starting_letter.txt", mode="r") as file1:
    letter = file1.readlines()

with open("./Input/Names/invited_names.txt", mode="r") as file2:
    names_list = file2.readlines()

for name in range(len(names_list) - 1):
    names_list[name] = names_list[name].strip("\n")

for name in names_list:
    letter[0] = letter[0].replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final_letter:
        for line in letter:
            final_letter.write(line)
