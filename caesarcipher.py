import string
import os

print("Caesar Cipher by Tyshawn U. Jones")
print("Created approximately Sun 19 Jun 2022 09:57:57 PM EDT")
print("Completed approximately Sun 19 Jun 2022 11:13:07 PM EDT")
print("Description:")
print("Julius Caesar was an emperor who ciphered his messages by shifting the alphabet.")

user_printable = input("Enter the text to be ciphered: ")
user_shift = int(input("Enter the shift the text will be ciphered by: "))


def caesar_cipher(user_printable, user_shift):
    ascii_characters = string.printable
    cipher_shift = ascii_characters[user_shift:] + ascii_characters[:user_shift]
    translation = user_printable.maketrans(ascii_characters, cipher_shift)
    return user_printable.translate(translation)

user_cipher = caesar_cipher(user_printable, user_shift)
print(user_cipher)
quit()
