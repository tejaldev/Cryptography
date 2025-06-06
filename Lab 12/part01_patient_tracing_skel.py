# 3310 Lab 12
# Part 01 
# 12/20/24 - Rursch
#
#
# Using Private Set Intersection (PSI) subfield
# of Multi-Party Computation (MPC)
#
# This program will read in the movement data on an individual
# who has contracted COVID-19.  You will compare those
# hashes to see if you have come in contact with the individual.
# It should not reveal the individual's information, just the location
# and time you were both in the same place.
# 
# This is a very simplified version of what actually happened in 
# COVID-19 contact tracing, but it demonstrates the basic concepts.
# 
# Syntax: python3 part01_patient_tracing_skel.py 


import hashlib
import json
from typing import List, Dict, Any

def hashData(data: str) -> str:
    # We are using SHA-256 as the OPPRF 
    return hashlib.sha256(data.encode()).hexdigest()

def main() -> None:
    # Read the hashed patient data from the file
    with open("hashedPatientData.json", "r") as file:
        hashedPatientData: Dict[str, Any] = json.load(file)

    # Simulated student locations with timestamps (in plaintext)
    studentData: List[Dict[str, str]] = [
        {"location": "MUPandaExpress", "time": "2024-11-12T11:00:00"},  
        {"location": "Coover1041LabA", "time": "2024-11-12T13:30:00"},
        {"location": "Durham171Lecture", "time": "2024-11-12T09:30:00"}
    ]

    # Hash the student's locations
    hashedStudentData: Dict[str, str] = {
        hashData(f"{entry['location']}|{entry['time']}"): "present"
        for entry in studentData
    }

    # Find common hashed locations (intersection of keys)
    commonHashes: List[str] = list(set(hashedPatientData.keys()) & set(hashedStudentData.keys()))

    # Retrieve original locations and times from the student's data
    commonLocations: List[Dict[str, str]] = [
        entry for entry in studentData
        if hashData(f"{entry['location']}|{entry['time']}") in commonHashes
    ]

    # Output the results
    print("Common locations found:", commonLocations)

if __name__ == '__main__':
    main()
