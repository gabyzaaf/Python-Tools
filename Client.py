import socket
PORT = 4444
HOST = socket.gethostname()
MAX_BUFFER_SIZE = 1024


def create_connection():
    """
    This function create a connection between you and the server
    You need to initialise a PORT > 1024 because you don't need permission
    :return:
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = HOST
    port = PORT
    client.connect((host, port))
    return client

def receive_message(client):
    """
    This function receive a message from client
    :param client:
    :return:
    """
    #: 1024 is the maximal size of byte can be send by port.
    message = client.recv(MAX_BUFFER_SIZE)
    print(message.decode('ascii'))

def close_connection(client):
    client.close()


if __name__ == "__main__":
    client_conn = create_connection()
    receive_message(client_conn)
    close_connection(client_conn)
