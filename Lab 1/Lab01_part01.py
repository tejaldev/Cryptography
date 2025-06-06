# 3310 Lab 01
# Part 01
# 12/13/24 - Rursch

# This program will prompt the user for a sentence and an integer number of positions
# to shift each character in the ASCII table.
#  
# In this specific case that integer will be three, but please do not hardcode this value.
#
# The program passes the sentence to a function named modify().
#
# The function modify() returns a string that shifts the key
# three characters to the left.  Mathematically, because A(65) becomes
# D (65+3)%26, it is called a right shift.    
#
# Below is an example of the key:
# abcdefghijklmnopqrstuvwxyz
# DEFGHIJKLMNOPQRSTUVWXYZABC


# Modify function:
#  Takes in a list and then
#  iterates through it
#  It converts all characters to uppercase and shifts the
#  key three to the left. The actual character values get larger.
#  It returns a string.
def modify(sentence: list[str], shift: int) -> str:
    result = []
    for char in sentence:
        # TODO:
        # Convert to uppercase.  Use ord() to convert to asii.  
        # Remember A is 65 in ASCII and there are 26 characters in the English language
        upperCase = char.upper()        #converts to uppercase
        shiftedChar = chr((ord(upperCase)-65 + shift )%26 +65 )     #key 3 to left
        result.append(shiftedChar)
    return ''.join(result)

# Main
def main() -> None:
    sentence: list[str] = list(input("Write a sentence without spaces: "))
    shift: int = int(input("Enter the shift value (positive for mathematically shifting to the right, negative for mathematically shifting to the left): "))
    result: str = modify(sentence, shift)
    print(f"Encrypted sentence: {result}")

if __name__ == "__main__":
    main()
   