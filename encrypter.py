from cryptography.fernet import Fernet
import base64
import hashlib
import os

print("Welcome to AnteZone SHA-256 File Encrypter")
print("[?] Please Install pip install cryptography Before Continuing")
print("[?] Source Code & Instruction Available at")
print("[?] https://www.github.com/AnteZone/SHA-256-File-Encrypter")
print("----------------------------------------------------------------")

def generate_key(password):
    # Derive a key from the password using SHA-256
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_file(filename, password, output_name):
    try:
        key = generate_key(password)
        fernet = Fernet(key)

        with open(filename, 'rb') as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(output_name, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        print("Encrypted successfully.")
    except Exception as e:
        print("Encryption failed:", e)

def decrypt_file(filename, password, output_name):
    try:
        key = generate_key(password)
        fernet = Fernet(key)

        with open(filename, 'rb') as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(output_name, 'wb') as dec_file:
            dec_file.write(decrypted)

        print("Decrypted successfully.")
    except Exception as e:
        print("Decryption failed:", e)

def main():
    action = input("Enter E for Encrypt or D for Decrypt: ").strip().upper()

    if action == 'E':
        filename = input("Enter the filename with extension to encrypt: ").strip()
        password = input("Enter password (leave empty for no password): ").strip()
        output = input("Enter name for encrypted file (with extension): ").strip()
        encrypt_file(filename, password, output)

    elif action == 'D':
        filename = input("Enter the filename with extension to decrypt: ").strip()
        password = input("Enter password (leave empty if none was set): ").strip()
        output = input("Enter name for decrypted file (with extension): ").strip()
        decrypt_file(filename, password, output)
    else:
        print("Invalid option.")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
