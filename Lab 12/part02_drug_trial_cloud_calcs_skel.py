# 3310 Lab 12
# Part 02 
# 12/20/24 - Rursch
#
#
# You are the researcher for a drug company who has a new blood pressure medicine 
# in trials at four hospitals in the Midwest.  You have gathered four data points 
# in the study:  systolic blood pressure (SBP), diastolic blood pressure (DBP), 
# heart rate (HR), and a patient satisfaction score reflecting the patients’ 
# experiences with medicine and their overall treatment.  Upon gathering the data 
# from the four hospitals, you now need to analyze the data.  
#
# Since you want to use the processing power of the cloud, but can’t share the 
# actual data points.  You used Partially Homomorphic Encryption (phe) to encrypt 
# the data before running this code "in the cloud" to calculate the averages on 
# the encrypted data. 
#
# Syntax: python3 part02_drug_trial_cloud_calcs_skel.py

from phe import paillier
import pickle
from typing import List

def main() -> None:
    # Load the public key and encrypted data from the file
    with open('publicKey.pkl', 'rb') as f:
        publicKey: paillier.PaillierPublicKey = pickle.load(f)

    with open('encryptedData.pkl', 'rb') as f:
        encryptedData: List[List[paillier.EncryptedNumber]] = pickle.load(f)

    # Initialize a list to store the sum of each measurement
    encryptedSums: List[paillier.EncryptedNumber] = [
        publicKey.encrypt(0) for _ in range(len(encryptedData[0]))
    ]

    # TODO:
    # Sum the encrypted measurements for each hospital
    # This is a simple summation exercise just adding values in the 
    # encrypted values. Remember there are four values 
    # for each hospital.
    for hospitalMeasurements in encryptedData:
        for i, measurement in enumerate(hospitalMeasurements):
            encryptedSums[i]+=measurement

    # TODO:
    # Calculate the encrypted average for each measurement
    # Again, just use the summation/number of hospitals for each measurement.
    numHospitals: int = len(encryptedData)
    encryptedAverages: List[paillier.EncryptedNumber] = [encryptedSum / numHospitals for encryptedSum in encryptedSums]  # Add calculation logic here

    # Save the encrypted averages to a file
    with open('encryptedAverages.pkl', 'wb') as f:
        pickle.dump(encryptedAverages, f)

    print("Encrypted averages saved to 'encryptedAverages.pkl'")

if __name__ == '__main__':
    main()
