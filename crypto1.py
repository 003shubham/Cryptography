import string
import random

class SimpleSubstitutionCipher:
    def __init__(self):
        self.plain_alphabet = string.ascii_lowercase
        self.cipher_alphabet = ''.join(random.sample(self.plain_alphabet, len(self.plain_alphabet)))

    def encrypt(self, plaintext):
        table = str.maketrans(self.plain_alphabet, self.cipher_alphabet)
        return plaintext.translate(table)

    def decrypt(self, ciphertext):
        table = str.maketrans(self.cipher_alphabet, self.plain_alphabet)
        return ciphertext.translate(table)

# Example usage:
cipher = SimpleSubstitutionCipher()
# message = "hello world"/

'''Only used for alphabatic text'''
message= input("Enter the plain text: ")
encrypted_message = cipher.encrypt(message)
print("Encrypted:", encrypted_message)
decrypted_message = cipher.decrypt(encrypted_message)
print("Decrypted:", decrypted_message)
