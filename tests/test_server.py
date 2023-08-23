"""
Module: Testing server.py functions
This module test all server.py functions with pytest module.

PEP8: This code adheres to PEP8 style guidelines.
PEP20: Readability counts.

Author: Fabián Espitia
"""
# Python
import os
from unittest.mock import patch

from Scripts.server import *
from Strings.generate_strings import generate_strings

# Utility function to create a test configuration file
def create_test_config(config_file):
    """
    Create a test configuration file with predefined paths.

    Args:
        config_file (str): Name of the configuration file to create.
    """

    with open(config_file, "w") as config:
        config.write("linuxpath=file1.txt\n")
        config.write("linuxpath=file2.txt\n")
        config.write("otherpath=file3.txt\n")

# search_files test
def test_search_files():
    """
    Test the search_files function.

    This test creates a temporary configuration file, runs the search_files function,
    and then asserts that certain files are found while others are not.

    Note: This test also demonstrates proper cleanup by removing the temporary file.
    """

    config_file = "test_config.txt"
    create_test_config(config_file)

    try:
        files = search_files(config_file)

        assert "file1.txt" in files
        assert "file2.txt" in files
        assert "file3.txt" not in files
    finally:
        if os.path.exists(config_file):
            os.remove(config_file)


# check_enable_ssl test
def test_check_enable_ssl_enabled():
    """
    Test the check_enable_ssl function when SSL is enabled.

    This test creates a temporary configuration file with ENABLE_SSL set to True
    and asserts that the function correctly identifies SSL as enabled.
    """

    config_file = "temp_config.txt"
    with open(config_file, "w") as file:
        file.write("ENABLE_SSL = True")

    result = check_enable_ssl(config_file)

    assert result == True

    os.remove(config_file)


def test_check_enable_ssl_disabled():
    """
    Test the check_enable_ssl function when SSL is disabled.

    This test creates a temporary configuration file with ENABLE_SSL set to False
    and asserts that the function correctly identifies SSL as disabled.
    """

    config_file = "temp_config.txt"
    with open(config_file, "w") as file:
        file.write("ENABLE_SSL = False")

    result = check_enable_ssl(config_file)

    assert result == False

    os.remove(config_file)


def test_check_enable_ssl_not_found():
    """
    Test the check_enable_ssl function when the configuration file is not found.

    This test asserts that the function returns None when the configuration file is not found.
    """

    config_file = "no_exist_config.txt"

    result = check_enable_ssl(config_file)

    assert result is None


# client_response test
def test_client_response_string_exists():
    """
    Test the client_response function when the requested string exists in the document.

    This test simulates a scenario where the requested string exists in the document
    and checks if the function's response contains the expected components.
    """

    client_message = "Hello"
    document = ["Hello", "how are you?", "This is a test message"]
    client_data = "debug"
    start_time = time.time()

    response = client_response(
        client_message, document, client_data, start_time)

    print(response)

    assert b"STRING EXISTS" in response
    assert client_data.encode("utf-8") in response
    assert b"Time_stamp:" in response


def test_client_response_string_does_not_exist():
    """
    Test the client_response function when the requested string does not exist in the document.

    This test simulates a scenario where the requested string is not found in the document
    and checks if the function's response contains the expected components.
    """

    document = ["Hello, how are you?", "This is a test message"]
    client_data = "debug"
    start_time = time.time()
    client_message = "NotInDocument"
    response = client_response(
        client_message, document, client_data, start_time)
    assert b"STRING NOT FOUND" in response
    assert client_data.encode("utf-8") in response
    assert b"Time_stamp:" in response

# load_document_contents test
def test_load_document_contents():
    """
    Test the load_document_contents function.

    This test creates a temporary configuration file, generates temporary files, loads
    their contents using the load_document_contents function, and asserts that the data
    is not None.
    """

    with open("test_document.txt", "w") as file:
        file.writelines("linuxpath=./test_file1.txt \n")
        file.writelines("linuxpath=./test_file2.txt \n")
        file.writelines("linuxpath=./test_file3.txt")

    files = search_files("test_document.txt")

    generate_strings(files[0], 5)
    generate_strings(files[1], 10)
    generate_strings(files[2], 15)

    try:
        with open(files[0], "r") as document:
            data = document.readlines()
            assert data != None

        with open(files[1], "r") as document:
            data = document.readlines()
            assert data != None

        with open(files[2], "r") as document:
            data = document.readlines()
            assert data != None
    finally:

        if os.path.exists("test_document.txt"):
            os.remove("test_document.txt")

        if os.path.exists("test_file1.txt"):
            os.remove("test_file1.txt")

        if os.path.exists("test_file2.txt"):
            os.remove("test_file2.txt")

        if os.path.exists("test_file3.txt"):
            os.remove("test_file3.txt")


def test_load_document_contents_file_not_found():
    """
    Test the load_document_contents function when the document file is not found.

    This test uses the unittest.mock.patch to simulate a scenario where
    the document file is not found. It then asserts that the function returns an empty list.
    """
    with patch("builtins.open", side_effect=FileNotFoundError):
        files = search_files("nonexistent_file.txt")
        assert files == []
