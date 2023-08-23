"""
Module: Server Requester
This module sends a string request to server socket and prints if the string exits or not.

PEP8: This code adheres to PEP8 style guidelines.
PEP20: Readability counts.

Author: Fabián Espitia
"""

# Python
import socket
import ssl

# Import necessary values from server module
from server import check_enable_ssl, CONFIG_FILE, CERT_FILE

# Constants
SERVER_ADDR = socket.gethostname()
SERVER_PORT = 8000


def main():
    """
    Program main entry point
    """

    # Create client's socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_ADDR, SERVER_PORT))
    message = input("¿Which word do you wanna search?: ")

    if check_enable_ssl(CONFIG_FILE):
        # If SSL is enabled, create an SSL context and connect using SSL
        ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        ssl_context.load_verify_locations(CERT_FILE)
        # If there are problems with the server_hostname, change the variable to server_hostname = "DESKTOP-LAROQRJ"
        ssl_socket = ssl_context.wrap_socket(
            client_socket, server_hostname=SERVER_ADDR)
        ssl_socket.send(message.encode("utf-8"))
        server_message = ssl_socket.recv(1024).decode("utf-8")
        print(f"{server_message} - SSL ACTIVE")
        ssl_socket.close()
    else:
        # If SSL is not enabled, send and receive data over the regular socket
        client_socket.send(message.encode("utf-8"))
        server_message = client_socket.recv(1024).decode("utf-8")
        print(server_message)
        client_socket.close()


# Program's Entry Point
if __name__ == "__main__":
    main()
