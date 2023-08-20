"""
Module: Strings generator
This module generates a text file with n random words.

PEP8: This code adheres to PEP8 style guidelines.
PEP20: Readability counts.

Author: Fabián Espitia
"""


# Import the Faker library to generate fake data
from faker import Faker

# Create an instance of the Faker class to generate random data
fake = Faker()


def generate_strings(file_name: str, random_words_quantity: int):
    """
    Generates and writes random words to a text file.

    Parameters:
        file_name (str): The name of the output text file.
        random_words_quantity (int): The number of random words to generate and write.
    """
    with open(file_name, "w") as document:
        for n in range(random_words_quantity):
            document.write(f" {fake.word()} \n")

# Generate random data and write to text files


# Generate 10,000 random words and write to "./10k.txt"
generate_strings("./10k.txt", 10000)

# Generate 100,000 random words and write to "./100k.txt"
generate_strings("./100k.txt", 100000)

# Generate 250,000 random words and write to "./250k.txt"
generate_strings("./250k.txt", 250000)

# Generate 1,000,000 random words and write to "./1M.txt"
generate_strings("./1M.txt", 1000000)
