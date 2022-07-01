import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    shift_amount %= 26
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
        else:
            pos = alphabet.index(letter)
            new_pos = pos + shift_amount
            if new_pos >= 26:
                new_pos -= 26
            if new_pos < 0:
                new_pos += 26
            end_text += alphabet[new_pos]
    print(f"The {cipher_direction}d text is {end_text}\n")

print(art.logo)

stay = True         
while stay:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    res = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n")
    
    if res == "yes":
        stay = True
    elif res == "no":
        print("\nGood Bye\n")
        stay = False
    else:
        print("Invalid answer!")
        invalid = True
        while invalid:
            res = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n")
            if res in ["yes", "no"]:
                print("\nGoodBye\n")
                invalid = False
                stay = False