
# maybe we can change it so that each type of command has its own function
def send_motor_command(clientSocket, cmd, values):

    command_type = 'MOVE'
    if (cmd in ['MANUAL', 'AUTONOMOUS']):
        command_type = 'MODE'
    elif (cmd in ['FASTER', 'SLOWER']):
        command_type = 'SPEED'
    print(f"Sending: {command_type}:{cmd}:{values}")

    # utilize global socket to send the command
    clientSocket.send(f'{command_type} {cmd}'.encode())