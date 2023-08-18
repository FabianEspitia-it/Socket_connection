"""
Module: Server Requester
This module sends a string request to server socket and prints if the string exits or not.

PEP8: This code adheres to PEP8 style guidelines.
PEP20: Readability counts.

Author: Fabián Espitia
"""


import socket

SERVER_ADDR = socket.gethostname()
SERVER_PORT = 8000


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_ADDR, SERVER_PORT))
    message = "seek"
    client_socket.send(message.encode("utf-8"))
    server_message = client_socket.recv(1024).decode("utf-8")
    print(server_message)
    client_socket.close()
  
# Program´s Entry Point 
if __name__ == "__main__":
    main()