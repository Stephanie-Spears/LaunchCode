import string
from random import shuffle

#alpha = string.ascii_lowercase+string.ascii_uppercase


def caeserShiftSub(secretWord, shift):
    #CaeserShift with Substition Cipher--with Caeser Shift we need only know the number of rotations to decrypt
    #Adding the Substitution Cipher makes it necessary to know the full list of letter substitutions
    
    alpha = string.ascii_lowercase+string.ascii_uppercase
    shift_alpha = alpha[shift:] + alpha[:shift]
    encodingTable = str.maketrans(alpha, shift_alpha)
    return secretWord.translate(encodingTable)
    


#def rosetta(secret, decipher):
#string.ascii_lowercase+string.ascii_uppercase
#  print(cipher)
# print(decipher)
    
secretWord = "Wolf"
shift = 2
#encodingTable = caeserShiftSub(secretWord, shift)
print(caeserShiftSub(secretWord,shift))
#rosetta(secretWord, encodingTable)
