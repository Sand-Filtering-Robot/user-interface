'''
Host Socket will be in the motion control software
'''
import socket

def main():
    s = socket.create_server(("127.0.0.1", 8080))
    s.listen(1)
    try:
        while True:
            conn, addr = s.accept()
            value = s.recv(12) # having issue here
            print(str(value))
    except Exception as e:
        s.close()
        print(e)


if __name__ == "__main__":
    main()