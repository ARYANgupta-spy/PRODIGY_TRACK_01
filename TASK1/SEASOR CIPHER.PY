# Function to encrypt a string using the Caesar cipher technique
def encrypt(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

# Function to decrypt a string encrypted with the Caesar cipher
def decrypt(string, shift):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
    return cipher

# Main program
text = input("Enter String: ")
s = int(input("Enter Shift Number: "))
option = int(input("1. For Encrypt\n2. For Decrypt\nEnter Your Option: "))
print("Original String:", text)
if option == 1:
    print("After Encryption:", encrypt(text, s))
else:
    print("After Decryption:", decrypt(text, s))
