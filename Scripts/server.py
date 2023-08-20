"""
Module: Searching Server
This module recieves a string, search it in a document and finally response if the string exits or not.

PEP8: This code adheres to PEP8 style guidelines.
PEP20: Readability counts.

Author: Fabián Espitia
"""


import socket
import threading
import time
import ssl

# Constants
SERVER_ADDR = socket.gethostname()
SERVER_PORT = 8000
CONFIG_FILE = "config.txt"
REREAD_ON_QUERY = True
CERT_FILE = "../SSL/server.crt"
KEY_FILE = "../SSL/server.key"


def search_files(config_file: str) -> list[str]:
    """
    Searches the strings files paths into config.txt.

    Args:
        config_file (str): config file.

    Returns:
        list[str]: Strings files paths list.
    """

    files = []
    try:
        with open(config_file, "r") as config:
            for line in config:
                if line.startswith("linuxpath="):
                    files.append(line.strip().split("=")[1])
    except FileNotFoundError:
        print(f"Config file '{config_file}' not found.")
    return files


def client_response(client_message: str, document: list[str], client_data: str, start_time: int) -> str:
    """
    Generates a response for the client based on the provided message and document.

    Args:
        client_message (str): Client's message to search for.
        document (list[str]): List of sentences to search within.
        client_data (str): Client's data for debugging.
        start_time (int): Starting time for performance measurement.

    Returns:
        str: Response message.
    """
    word_number = 1

    for sentence in document:
        new_sentence = sentence.replace("\n", "").strip()
        if new_sentence == client_message:
            message = f"STRING EXISTS, {client_data}, Execution_time: {round((time.time() - start_time ) * 1000, 2)} ms, Time_stamp: {time.ctime()}, Word_in_line: {word_number}  \n".encode(
                "utf-8")
            break
        word_number += 1

    else:
        message = f"STRING NOT FOUND, {client_data} , Execution_time: {round((time.time()- start_time) * 1000, 2)} ms, Time_stamp: {time.ctime()}  \n".encode(
            "utf-8")

    return message


def client_connection(client_socket, client_addr: tuple[str, int]):
    """
    Handles the client connection.

    Args:
        client_socket: Client's socket object.
        client_addr (tuple[str, int]): Client's address.
    """

    client_message = client_socket.recv(1024).decode("utf-8")
    client_message = client_message.rstrip('\x00')
    client_data = f"DEBUG: Request: {client_message}, Client_IP: {client_addr}"
    files = search_files(CONFIG_FILE)

    if REREAD_ON_QUERY:
        try:
            with open(files[-2], "r") as document:
                start_time = time.time()
                client_socket.send(client_response(
                    client_message, document, client_data, start_time))
        except FileNotFoundError as error:
            client_socket.send(
                f"ERROR: {error}, FILE NOT FOUND".encode("utf-8"))
    else:
        cached_document = load_document_contents(CONFIG_FILE)
        start_time = time.time()
        client_socket.send(client_response(
            client_message, cached_document, client_data, start_time))

    client_socket.close()


def load_document_contents(config_file: str) -> list[str]:
    """
    Loads and returns the contents of the document from the config file.

    Args:
        config_file (str): Path to the config file.

    Returns:
        list[str]: List of lines from the document.
    """
    files = search_files(config_file)
    with open(files[-2], "r") as document:
        data = document.readlines()
    return data


def check_enable_ssl(config_file: str) -> bool:
    """
    Checks if SSL is enabled based on the config file.

    Args:
        config_file (str): Path to the config file.

    Returns:
        bool: True if SSL is enabled, False otherwise.
    """
    with open(config_file, "r") as file:
        for line in file:
            if line.startswith("ENABLE_SSL"):
                state = line.strip().split("=")[1].strip()
                return state == "True"


def main():
    """
    Program's main entry point
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_ADDR, SERVER_PORT))
    server_socket.listen(5)

    while True:

        client_socket, client_addr = server_socket.accept()

        if check_enable_ssl(CONFIG_FILE):
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ssl_context.load_cert_chain(
                certfile=CERT_FILE, keyfile=KEY_FILE)
            ssl_client_socket = ssl_context.wrap_socket(
                client_socket, server_side=True)
            client_thread = threading.Thread(
                name="client_thread", target=client_connection, args=(ssl_client_socket, client_addr))
            client_thread.start()

        else:
            client_thread = threading.Thread(
                name="client_thread", target=client_connection, args=(client_socket, client_addr))
            client_thread.start()


# Program's Entry Point
if __name__ == "__main__":
    main()
