import random

letters = ["a", "b", "c", "d", "e",
           "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o",
           "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y",
           "z", "A", "B", "C", "d", 
           "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N",
           "O", "P", "Q", "R", "S",
           "T", "U", "V", "W", "X",
           "Y", "Z"]

symbols = ["!", "@", "#", "%", "&", "*", "+"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

print("\nWelcome to the Pypassword Generator\n")
n_letters = int(input("Hou many letter would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like in your password?\n"))
n_numbers = int(input("How many numbers would you like in your password?\n"))

password = []
for i in range(0, n_letters):
    password.append(random.choice(letters))

for j in range(0, n_symbols):
    password.append(random.choice(symbols))

for k in range(0, n_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)   

print("Your password is: ", end='')
for charactere in password:
    print(charactere, end='')
print('\n')