"""
Add two random numbers together

Requires no setup. 
"""
import random

# Instructions:
# Download this file
# Run it with 
# python -i docs.py
# This will run the file and leave you at the command prompt, with the file imported.
# Now try 
# help(add)

def add (num1, num2):
    """
    Add two numbers.

    Postional arguments:
    num1 -- an integer or double number (no default)
    num2 -- an integer or double number (no default)

    Returns:
    Sum of the two numbers.
    """
   
    return num1 + num2    


    
numA = random.random() * 10
numB = random.random() * 10    
print(add(numA, numB))



