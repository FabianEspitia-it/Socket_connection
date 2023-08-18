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

SERVER_ADDR = socket.gethostname()
SERVER_PORT = 8000
CONFIG_FILE = "config.txt"

read_on_query = False


def search_file(config_file: str) -> list[str]:

    """
    Searches the strings files paths into config.txt.

    Args:
        config_file (str): config file.

    Returns:
        list[str]: Strings files paths list.
    """

    files = []
    with open(config_file, "r") as config:
        for line in config:
            if line.startswith("linuxpath="):
                files.append(line.strip().split("=")[1])
    return files


def client_connection(client_socket, client_addr: tuple[str, int]):

    client_message = client_socket.recv(1024).decode("utf-8")
    client_message = client_message.rstrip('\x00')

    try:
        with open(search_file(CONFIG_FILE)[-1], "r") as document:
            client_data = f"DEBUG: Request: {client_message}, IP: {client_addr}"
            start_time = time.time()
            for sentence in document:
                new_sentence = sentence.replace("\n", "").strip()
                if new_sentence == client_message:
                    client_socket.send(
                        f"STRING EXISTS, {client_data}, Execution Time: {round((time.time() - start_time ) * 1000, 2)} ms, TimeStamp: {time.ctime()}  \n".encode("utf-8"))
                    break
            else:
                client_socket.send(
                    f"STRING NOT FOUND, {client_data} , Execution Time: {round((time.time()- start_time) * 1000, 2)} ms, TimeStamp: {time.ctime()}  \n".encode("utf-8"))

    except FileNotFoundError:
        client_socket.send("FILE NOT FOUND".encode("utf-8"))

    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_ADDR, SERVER_PORT))
    server_socket.listen(5)

    while True:
        client_socket, client_addr = server_socket.accept()
        client_thread = threading.Thread(
            name="client_thread", target=client_connection, args=(client_socket, client_addr))
        client_thread.start()


# Program´s Entry Point
if __name__ == "__main__":
    main()
