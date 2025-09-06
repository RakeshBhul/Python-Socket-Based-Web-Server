import socket
import sys

HOST = ""  # Empty string means all available interfaces
PORT = 8080  # Arbitrary non-privileged port

# Create socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket has been created')

# Bind socket to host and port
try:
    mySocket.bind((HOST, PORT))
except socket.error as msg:
    print('Binding has failed. Error Code: ' + str(msg.errno) + ' Message: ' + str(msg.strerror))
    sys.exit()

print('Socket bind is complete. Now we can proceed to make it listen...')

# Start listening
mySocket.listen(10)
print('Socket is now listening')

# Accept connections
while True:
    connection, address = mySocket.accept()
    print('Connected with ' + address[0] + ':' + str(address[1]))

    # Send a simple HTTP response
    response = b"""\
HTTP/1.1 200 OK

Hello from Kali Web Server!
"""
    connection.sendall(response)
    connection.close()
