# 3310 Lab 10
# Part 02 
# 12/20/24 - Rursch
#
# ISU Lottery generates lottery numbers for two consecutive days of the month
# using a pseudorandom number generator (PRNG).  Part of the lab is determining
# what the seed(s) are for the random number generator.                              
#
# You have to figure out the winning numbers for November 12 based upon
# the numbers for November 11 given in the lab instructions.  
# 
#
import random
from typing import List

# Generates a winning lottery number for today and tomorrow
def generateLottery(dateOfGeneration: str, timeInSeconds: int) -> List[str]:
    # timeInSeconds = [0, 1, ..., 86400]
    # dateOfGeneration = MM/DD/YYYY
    lotteryNumbers: List[str] = []

    # Add the date and the seconds to get the seed
    seed: int = int(dateOfGeneration.replace("/", "")) + timeInSeconds
    random.seed(seed)

    # Generate lottery number for the current day
    randomNumbers: List[str] = []
    for i in range(10):
        randomNumbers.append(str(random.randrange(0, 10)))
    lotteryNumbers.append('-'.join(randomNumbers))

    # Generate lottery number for the next day
    # Reset the list for the next day's numbers
    randomNumbers = []  
    for i in range(10):
        randomNumbers.append(str(random.randrange(0, 10)))
    lotteryNumbers.append('-'.join(randomNumbers))

    # Return an array of two values
    # lotteryNumbers[0] = Today's lottery number
    # lotteryNumbers[1] = Tomorrow's lottery number
    return lotteryNumbers

def main() -> None:
    # TODO:  Call the generateLottery function with the correct seed values to generate the 
    #   winning numbers.
    date= "11/11/2024"
    target = "8-3-9-5-7-4-4-7-6-7"
    for timeinsec in range(86041):
        lotteryNumbers = generateLottery(date, timeinsec)
        if lotteryNumbers[0] == target:
            break
    
    print("Numbers are: ", lotteryNumbers)


if __name__ == '__main__':
    main()
