"""
This is called DocString
"""

# This is add function
def add(number1, number2):  # Defining the function to add
    """
    this is the function document
    """
    return number1 + number2

NUM1 = 4
NUM2 = 5

TOTAL = add(NUM1, NUM2)

print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
