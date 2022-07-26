from random import randint, choice, shuffle


def generate_password():
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

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(4, 6))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password = password_letter + password_symbol + password_number
    shuffle(password)

    return "".join(password)
