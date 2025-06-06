# 3310 Lab 03
# Part 01
# 12/13/24 - Rursch

# This program will conduct a trigram analysis on the ciphertext file.
# It then finds the starting indices for the most common trigrams and calculates
# the distances between the starting indices.  A function is provided to help
# the student find the common factors of the differences.  This common factor
# will determine the key length.
# 
# The user will be prompted to visually assess the common factor(s) and enter
# the key length they want to try.  The progam splits the ciphertext into 
# multiple monoalphabetic shift-by-n ciphers and performs frequency analysis on 
# each cipher.  The frequency results are printed and suggestions are made as to 
# which character has been substituted for the letter E.  Remember, the normal 
# distribution of characters in the English language (descending order) has
# E, T, and A as the most commonly used characters.  
#
# The user will be prompted for the keyword and the solution using that keyword
# is then printed. The user can determine if they found the correct solution or if they
# want to try variant of the keyword.
#
# SYNTAX:   python3 part01_skel.py ciphertext.txt
#           python3 part01_skel.py <ciphertext_file>


import sys

# readIn:
#   Reads in a file and returns its contents as a single uppercase string.
def readIn(filename: str) -> str:
    with open(filename, 'r') as file:
        return ''.join(line.strip().upper() for line in file)


# trigramAnalysis:
#   Counts the occurrences of each trigram in the ciphertext.
#   Identifies the most frequent trigrams, their positions, and differences.
def trigramAnalysis(ciphertext: str) -> None:
    from math import gcd
    from functools import reduce

    def findGCD(numbers: list[int]) -> int:
        return reduce(gcd, numbers)

    trigramCounts = {}
    trigramPositions = {}

    # Sliding window to find trigrams
    for i in range(len(ciphertext) - 2):
        trigram = ciphertext[i:i+3]
        trigramCounts[trigram] = trigramCounts.get(trigram, 0) + 1
        trigramPositions.setdefault(trigram, []).append(i)

    # Sort trigrams by frequency
    sortedTrigrams = sorted(trigramCounts.items(), key=lambda x: x[1], reverse=True)

    # Print the five most common trigrams
    print("Most Common Trigrams:")
    for trigram, count in sortedTrigrams[:5]:
        positions = trigramPositions[trigram]
        differences = [positions[j] - positions[j-1] for j in range(1, len(positions))]
        # TODO:
        #   Calculate the commonDivisor using the function findGCD
        #   You may use your own logic if you wish, but the find GCD has
        #   been provided to make this relatively simple for you.  
        commonDivisor = findGCD(differences)
        print(f"Trigram: {trigram}\n Count: {count}\n Positions: {positions}\n Differences: {differences}\n GCD: {commonDivisor}\n")

# splitIntoXCiphers:
#   Splits the ciphertext into keyLength number of monoalphabetic shift-by-n ciphers.
def splitIntoXCiphers(keyLength: int, ciphertext: str):
    xCiphers = ['' for _ in range(keyLength)]

    for i, char in enumerate(ciphertext):
        xCiphers[i % keyLength] += char
    
    for i, cipher in enumerate(xCiphers):
        print(f"Cipher {i}: {cipher}")
    
    return xCiphers

# frequency:
#   Calculates the frequency of each character in the given cipher text.
def frequency(cipher: str) -> dict:
    freq = {}
    for char in cipher:
        freq[char] = freq.get(char, 0) + 1
    return freq

# shiftChars:
#   Shifts characters in each cipher based on the most likely plaintext characters.
#   Displays frequency analysis for each cipher and allows the user to provide a keyword.
def shiftChars(xCiphers: list):
    suggestedKey = []
    for i, cipher in enumerate(xCiphers):
        print(f"Analyzing Cipher {i}:")
        freq = frequency(cipher)
        sortedFreq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        print(f"Frequency for Cipher {i}:")
        for char, count in sortedFreq:
            print(f"{char}: {count}")

        # Corresponding alphabets for most frequent characters
        print("Corresponding alphabets:")
        for char, count in sortedFreq[:3]:
            shift = (ord(char) - ord('E')) % 26
            shiftedAlphabet = ''.join(chr((i + shift) % 26 + 65) for i in range(26))
            print(f"{char}: Shifted Alphabet (setting E to {char}): {shiftedAlphabet}")


    key = input("Enter the keyword you think will decrypt the ciphertext: ").strip().upper()
    return key
    for i, cipher in enumerate(xCiphers):
        print(f"\nAnalyzing Cipher {i}:")
        freq = frequency(cipher)
        sortedFreq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        print(f"Frequency for Cipher {i}:")
        for char, count in sortedFreq:
            print(f"{char}: {count}")

        # Corresponding alphabets for most frequent characters
        print("Corresponding alphabets:")
        for char, count in sortedFreq[:3]:
            print(f"{char}: Likely corresponds to 'E', 'T', or 'A'")

    key = input("Enter the keyword you think will decrypt the ciphertext: ").strip().upper()
    return key

# decrypt:
#   Decrypts the ciphertext using the given Vigenere key. 
def decrypt(ciphertext: str, key: str) -> str:
    keyRepeated = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    plaintext = []
    for c, k in zip(ciphertext, keyRepeated):
        decryptedChar = chr(((ord(c) - ord(k)) % 26) + 65)
        plaintext.append(decryptedChar)
    return ''.join(plaintext)

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <ciphertext_file>")
        sys.exit(1)

    filename = sys.argv[1]
    ciphertext = readIn(filename)
    print(f"\nCiphertext Loaded:\n{ciphertext}\n")

    # Trigram Analysis
    trigramAnalysis(ciphertext)

    # Determine Key Length
    keyLength = int(input("\nWhat is the likely key length? "))
    
    # Split into X ciphers
    xCiphers = splitIntoXCiphers(keyLength, ciphertext)

    # Frequency Analysis and Key Derivation
    while True:
        key = shiftChars(xCiphers)

        # Decrypt Ciphertext
        plaintext = decrypt(ciphertext, key)
        print(f"\nDecrypted Plaintext:\n{plaintext}")
        
        retry = input("\nDo you want to try another keyword? (yes/no): ").strip().lower()
        if retry != 'yes':
            break   

if __name__ == "__main__":
    main()
