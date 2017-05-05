import string
from random import shuffle

#alpha = string.ascii_lowercase+string.ascii_uppercase
plainText = raw_input("What is your plaintext? ")
shift = int(raw_input("What is your shift? "))

def caesar(plainText, shift): 

    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
        cipherText = ""
        cipherText += finalLetter

    print ("Your ciphertext is: ", cipherText)

    return cipherText

caesar(plainText, shift)

#def caesarShiftSub(secretWord, shift):
    #CaeserShift with Substition Cipher--with Caeser Shift we need only know the number of rotations to decrypt
    #Adding the Substitution Cipher makes it necessary to know the full list of letter substitutions
    
 #   alpha = string.ascii_lowercase+string.ascii_uppercase
   # shift_alpha = alpha[shift:] + alpha[:shift]
  #  encodingTable = str.maketrans(alpha, shift_alpha)
    #return secretWord.translate(encodingTable)
    


#def rosetta(secret, decipher):
#string.ascii_lowercase+string.ascii_uppercase
#  print(cipher)
# print(decipher)
    
secretWord = "wolf"
shift = 2
#encodingTable = caeserShiftSub(secretWord, shift)
print(caesarShiftSub(secretWord,shift))
#rosetta(secretWord, encodingTable)
