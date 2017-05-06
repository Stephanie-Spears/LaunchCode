import string

def decrypt(encrypted_message, shift):
    alpha=string.ascii_lowercase
    decrypted_message=""
    
    for char in encrypted_message:
        decrypted_message += chr(ord(char)-shift)
    return decrypted_message

def encrypt(message, shift):
    alpha=string.ascii_lowercase
    encrypted_message=""
    
    for char in message:
        encrypted_message += chr(ord(char)+shift)
    return encrypted_message
    
    
message="run Rabbit run!"
shift = 1


encrypted_message = encrypt(message, shift)
print(encrypted_message)
decrypted_message = decrypt(encrypted_message, shift)
print(decrypted_message)
