# 3310 Lab 01
# Part 03
# 12/13/24 - Rursch
# This program will conduct cryptanalysis on a Shift by N cipher using an
#exhaustive key search.
#
# You will read the ciphertext file in as an argument from the command line.
#
# The function analyze() will read in the ciphertext and then conduct an
# exhaustive key search that outputs its key (the N) and the answer in each trial.
#
# SYNTAX: python3 part03_skel.py ciphertext.txt
# Example output:
# Testing shift by 0:
# NQNPJHFYXFSIITLXX
#
# Testing shift by 1:
# MPMOIGEXWERHHSKWW
#
# Testing shift by 2:
# LOLNHFDWVDQGGRJVV
#
# Testing shift by 3:
# KNKMGECVUCPFFQIUU
#
# Testing shift by 4:
# JMJLFDBUTBOEEPHTT
#
# Testing shift by 5:
# ILIKECATSANDDOGSS
import sys
def readFile(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()
def analyze(ciphertext: str) -> None:
# TODO:
# Convert the ciphertext to uppercase.
# Loop the entire ciphertext
# through every possible shift value to
# brute force the decryption of this shift-by-n cipher.
# A nested loop will be useful.
# Print each shift value and the resulting potential solution.
# The logic from part01 will come in handy here. Remember in
# part 01 you were encrypting, but here you are decrypting.
        ciphertext= ciphertext.upper()      #converts to upper case
        for shift in range(26):  # Try all possible shifts
            testCipherStr = ""  #declare the test cipher string
            for char in ciphertext:         #loop through entire ciphertext
                if char.isalpha():  # Only shift alphabetic characters
                    testCipherStr += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                else:
                    testCipherStr += char  # Preserve non-alphabetic characters
            print(f"Testing shift by {shift}:\n{testCipherStr}\n")
#Main
def main() -> None:
    if len(sys.argv) < 2:
        print("Not enough values")
        print("Usage: python3 part03_skel.py ciphertext.txt")
        return
    ciphertext=readFile(sys.argv[1])
    analyze(ciphertext)

if __name__ == "__main__":
    main()