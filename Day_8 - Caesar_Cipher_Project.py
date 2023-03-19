"""
In this assignment I wrote a code that implemented the Caesar Cipher encryption technique.
"""

from art import logo_Caesar_Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, cipher_direction):
    """
   This function will combine both of the encrypt and the decrypt functions of the Caesar Cipher encryption technique.
    """
    cipher_msg = ""
    if  cipher_direction == "decode":
        shift_amount *= -1
        
    for letter in plain_text:
        if letter in alphabet:
            tr_index = alphabet.index(letter)
            new_index = (tr_index + shift_amount) % 26
            cipher_msg += alphabet[new_index]
        else:
            cipher_msg += letter
    
    print(f"The {cipher_direction}d text is: {cipher_msg}")
    

while keep_going == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    keep_going = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if keep_going == 'no':
        print('Goodbye !')
