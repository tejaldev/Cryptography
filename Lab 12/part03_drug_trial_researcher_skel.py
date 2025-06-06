# 3310 Lab 12
# Part 03 
# 12/20/24 - Rursch
#
#
# Now you have received the encrypted averages back from your work in the cloud.
# You now want to decrypt them to share the results with the FDA in an attempt
# to get your drug to the health care market.
# Of course, you have the private key because you created it before you encrypted
# the data with the public key.

from phe import paillier
import pickle
from typing import List

# Load the private key
with open('privateKey.pkl', 'rb') as f:
    privateKey: paillier.PaillierPrivateKey = pickle.load(f)

# Load the encrypted averages
with open('encryptedAverages.pkl', 'rb') as f:
    encryptedAverages: List[paillier.EncryptedNumber] = pickle.load(f)

# TODO:
# Decrypt the averages. This can be accomplished using the decrypt() method
# privateKey.decrypt() will be useful to you.
decryptedAverages: List[float] = [privateKey.decrypt(avg) for avg in encryptedAverages]  # Add logic here to store decrypted averages

print("Decrypted averages:", decryptedAverages)
