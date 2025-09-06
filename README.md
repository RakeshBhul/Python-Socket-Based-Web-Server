#Python Web Server
This project is a simple web server written in Python. It's designed to demonstrate the fundamental concepts of network programming using Python's built-in socket module. The server listens for incoming connections and responds with a basic HTTP message.

#Features
Lightweight: The server is a single Python script with no external dependencies.

TCP/IP: It uses the TCP protocol for reliable, stream-based communication.

HTTP Response: It sends a standard HTTP/1.1 200 OK response to any client that connects.

Multi-Connection: It can handle multiple connections sequentially in a loop.

#How to Use
Clone the Repository

git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
Run the Server
Execute the script from your terminal. You might need to use python3 depending on your system's configuration.

python your_server_script_name.py
You will see the following output:

Socket has been created
Socket bind is complete. Now we can proceed to make it listen...
Socket is now listening
Connect to the Server
Open a web browser and navigate to http://localhost:8080.
You should see the message "Hello from Kali Web Server!" displayed in your browser.
Alternatively, you can use a command-line tool like curl:

curl localhost:8080
The terminal will show the raw HTTP response:

HTTP/1.1 200 OK
Hello from Kali Web Server!
Code Explanation
The code is a simple loop that handles incoming connections.

socket.socket() creates the socket object, which acts as the endpoint for network communication.

mySocket.bind((HOST, PORT)) assigns the socket to a specific address and port (localhost on port 8080).

mySocket.listen(10) puts the server in a listening state, waiting for a connection request.

mySocket.accept() is the crucial part that waits for and accepts an incoming connection. It returns a new socket for the client and their address.

connection.sendall(response) sends the HTTP response back to the client.

connection.close() closes the connection with the client, and the loop starts over, waiting for the next request.
