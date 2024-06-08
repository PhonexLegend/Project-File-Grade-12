#Write a random number generator that generates random numbers between 1 and 6 (simulates dice).
import random

def roll_dice():
    """
    Simulates rolling a six-sided die (standard dice).
    """
    return random.randint(1, 6)

# Test the function
print("Rolling the dice...")
result = roll_dice()
print("The result is:", result)
