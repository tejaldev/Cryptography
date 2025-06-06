# 3310 Lab 01
# Part 02
# 12/13/24 - Rursch

# This program will search a list of lists.
# The program will prompt the user for a character and print out
# the number of times the character appears in each of the lists.

# Frequency function:
#  There are two input variables used by this function: the name of
#  the list of lists and the character for which you are searching.
#  The function prints (not returns) the number of occurrences of
#  that character in each of the lists.

def frequency(inputs: list[list[str]], character: str) -> None:
    # TODO:
    # Loop through the list of lists
    # Count the number of times the character occurs in each list
    # Print the results
        for i in range(len(inputs)):        #loops through the list of lists
            count = 0
            for char in inputs[i]:
                if char==character:
                    count=count+1           #counts the no of times the characte occurs in each list
            print(f"List [{i}]: {count}")

# Main
def main() -> None:
    # A list of lists
    inputs = [
        list("AOLSLAALYJJVVRPLZBHYABDPAOBSLAZAOBURBMVAOLYAOPUNZ"),
        list("ZCXNSMCPROCTYDGHCSUIRYTEBHHCJSMECWTQZCHDKRILLMSJS"),
        list("WSCVKAUSAUDJAUUEAOPLAHSMACDGHAUUSGABXHAGEHASGDARU")
    ]

    charToCount = input("What character do you want to check?  ")
    frequency(inputs, charToCount)

if __name__ == "__main__":
    main()