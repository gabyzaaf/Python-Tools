import socket
PORT = 4444
HOST = socket.gethostname()


def create_connection():
    """
    This function initialise connection
    AF_INET = IPV4
    SOCK_STREAM = TCP
    :return:
    """
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    hostname = HOST
    port = PORT
    serversocket.bind((hostname,port))
    serversocket.listen(3)
    return serversocket


def create_only_one_communication(serversocket):
    """
    This function create only one communication
    and send message to the client.
    :param serversocket:
    :return:
    """
    while True:
        clientsocket,address = serversocket.accept()
        message  ="the connection with {}".format(address).encode()
        clientsocket.send(message)
        print("Thanks to be connected")
        clientsocket.close()


def main():
    socket_server = create_connection()
    create_only_one_communication(socket_server)


if __name__ == "__main__":
    main()