# 3310 Lab 05
# Part 01 & 02
# 12/20/24 - Rursch
#
# In this lab you will encrypt and decrypt a file using a provided
# key and nonce.  The input and output files need to be read and written
# as binary files.
#
# SYNTAX:
#
# Encrypt
#    python part01_encrypt_decrypt_chacha_skel.py encrypt <inputFile> <outputFile> <keyFile> <nonceFile>
#
# Decrypt
#    python part01_encrypt_decrypt_chacha_skel.py decrypt <inputFile> <outputFile> <keyFile> <nonceFile>
#
# XOR Operation
#    python part01_encrypt_decrypt_chacha_skel.py xor <ciphertextFile1> <ciphertextFile2> <knownPlaintextFile> <outputFile>

import os
import sys
from typing import Tuple
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Read file as binary
# Using typing this says read the filename in as a string and return bytes since you want binary
def readFile(filename: str) -> bytes:
    with open(filename, 'rb') as file:
        return file.read()

# Write data to a file as binary
def writeFile(filename: str, data: bytes) -> None:
    with open(filename, 'wb') as file:
        file.write(data)

# Read key/nonce from their respective files
def loadKeyNonce(keyFilename: str, nonceFilename: str) -> Tuple[bytes, bytes]:
    # TODO:  Read the key and nonce values into their respective variables using the readFile function
    key = readFile(keyFilename)
    nonce = readFile(nonceFilename)
    return key, nonce

# Encrypt data using ChaCha20
def chacha20Encrypt(data: bytes, key: bytes, nonce: bytes) -> bytes:
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data)

# Decrypt data using ChaCha20
def chacha20Decrypt(data: bytes, key: bytes, nonce: bytes) -> bytes:
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(data)

# Main function can either encrypt or decrypt using ChaCha20
def main():
    # Check command line arguments
    if len(sys.argv) < 6:
        print("Usage:")
        print("  Encryption: python3 part01_encrypt_decrypt_chacha_skel.py encrypt <inputFile> <outputFile> <keyFile> <nonceFile>")
        print("  Decryption: python3 part01_encrypt_decrypt_chacha_skel.py decrypt <inputFile> <outputFile> <keyFile> <nonceFile>")
        sys.exit(1)

    # Read in the operation (encrypt/decrypt), inputFile, outputFile, keyFile, and nonceFile from the command line
    operation = sys.argv[1].lower()
    inputFilename = sys.argv[2]
    outputFilename = sys.argv[3]
    keyFilename = sys.argv[4]
    nonceFilename = sys.argv[5]

    if operation == 'encrypt':
        # Read the plainText file using the readFile function
        plainText = readFile(inputFilename)

        # Load key and nonce from binary files provided using the loadKeyNonce function
        key, nonce = loadKeyNonce(keyFilename, nonceFilename)

        # Encrypt the plainText using the chacha20Encrypt function
        cipherText = chacha20Encrypt(plainText, key, nonce)

        # Write the cipherText to the outputFilename using the writeFile function
        writeFile(outputFilename, cipherText)
        print(f"File '{inputFilename}' encrypted successfully to '{outputFilename}'.")

    elif operation == 'decrypt':
        # Load key and nonce from files using the loadKeyNonce function
        key, nonce = loadKeyNonce(keyFilename, nonceFilename)

        # Read the input (encrypted) file using the readFile function
        cipherText = readFile(inputFilename)

        # Decrypt the data using the chacha20Decrypt function
        decryptedText = chacha20Decrypt(cipherText, key, nonce)

        # Write the plainText to the outputFilename using the writeFile function
        writeFile(outputFilename, decryptedText)
        print(f"File '{inputFilename}' decrypted successfully to '{outputFilename}'.")

        # Print the decrypted content in ASCII format to check if you properly decrypted
        try:
            print(f"Decrypted content (ASCII): {decryptedText.decode('ascii')}")
        except UnicodeDecodeError:
            print("Warning: The decrypted content contains non-ASCII characters and could not be fully decoded as ASCII.")

    else:
        print("Invalid operation. Please use 'encrypt' or 'decrypt'.")
        sys.exit(1)

# Entry point
if __name__ == "__main__":
    main()
