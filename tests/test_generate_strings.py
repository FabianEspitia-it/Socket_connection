"""
Module: Testing generate_strings function
This module test the generate_strings function with pytest module.

PEP8: This code adheres to PEP8 style guidelines.
PEP20: Readability counts.

Author: Fabián Espitia
"""

# Python
import pytest
import os

from Strings.generate_strings import generate_strings

# Parametrized test definition for the generate_strings function


@pytest.mark.parametrize(
    "file_name_input, random_words_quantity_input",
    [
        ("./5.txt", 5),
        ("./10.txt", 10),
        ("./15.txt", 15),
        ("./20.txt", 20),
        ("./25.txt", 25)
    ]
)
def test_generate_params(file_name_input, random_words_quantity_input):
    """
    Test the generate_strings function with different input parameters.

    This test utilizes parameterization to execute the generate_strings function with
    various file sizes and quantities of random words. It then checks if the number of
    lines in the generated file matches the specified number of random words.

    Args:
        file_name_input (str): Path of the output file.
        random_words_quantity_input (int): Number of random words to generate.
    """

    try:
        # Call the generate_strings function with the input parameters
        generate_strings(file_name_input, random_words_quantity_input)

        # Verification of the result
        with open(file_name_input, "r") as file:
            lines = len(file.readlines())
            assert lines == random_words_quantity_input
    finally:
        # Cleanup: Remove the generated file after the test
        if os.path.exists(file_name_input):
            os.remove(file_name_input)
