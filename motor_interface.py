from enum import Enum
import socket

class Command(Enum):
    AUTO = 1
    MANUAL = 2
    MOVE = 3
    STOP = 4
    SPEED = 5
    LEFT = 6
    RIGHT = 7
    UP = 8
    DOWN = 9

# maybe we can change it so that each type of command has its own function
def send_motor_command(clientSocket, cmd, values):
    print(f"Sending: {cmd}:{values}")

    # utilize global socket to send the command
    clientSocket.send(f'MOVE {cmd}'.encode())

    # expect an ACK from server :) (debug purposes)
    msg = clientSocket.recv(64).decode()
    if (msg == 'ACK'):
        print('Got ACK. Everything is good')
    else:
        print('Bad Response from server x.x')

    #mysock = socket.create_connection(("127.0.0.1", 8080))
    # mysock.send(f"{cmd}:values")
    #mysock.close()