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


def send_motor_command(cmd, values):
    print(f"Sending: {cmd}:{values}")
    #mysock = socket.create_connection(("127.0.0.1", 8080))
    # mysock.send(f"{cmd}:values")
    #mysock.close()