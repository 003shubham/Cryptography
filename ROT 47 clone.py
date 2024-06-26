message = str(input("Enter the plain text: "))

def rot47(text):
    result = ""
    key = int(input("Enter the key: "))
    for char in text:
        ascii_val = ord(char)
        if (key <= ascii_val <= key+93):
            # Rotate the printable ASCII characters
            result += chr(33 + ((ascii_val + 14) % 94))
        else:
            # Leave non-printable characters unchanged
            result += char
    return result

encrypted_message = rot47(message)
print("Encrypted:", encrypted_message)

# To decrypt, simply apply ROT47 again
decrypted_message = rot47(encrypted_message)
print("Decrypted:", decrypted_message)
