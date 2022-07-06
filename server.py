from socket import *
from wsgiref.util import request_uri

# The hosting server port (enterted in the browser as localhost:9000)
port =9000

# The server's entiery socket
serverSocket = socket(AF_INET,SOCK_STREAM)

# Adding the port number to the the server socket
serverSocket.bind(("",port))

# HTTP response
serverSocket.listen(1)

print("The server has been read successfully!")
print("The server Information: \n")

# The loop that goes on as the users keeps seaching
# As many time as they want on the same port
while True:

    #Recivig a request from another socket
    connectionSocket, address = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode('utf-8')

    # Getting the IP address & the port number and printing them
    IP_address = address[0]
    Connected_port = address[1]
    print("IP Address: " + str(IP_address))
    print("Port: " + str(Connected_port))
    workOn=False

    # To only work if there is information from the connected socket
    if sentence != '':

        sentence_list = sentence.split(' ')
        reqFile = sentence_list[1]
        request = (reqFile).split(" ")[0]
        request = request.lstrip('/')
        workOn=True
    else:
        connectionSocket.close()

    # Here are all the cases for the types of requests
    if workOn:
        req=request
        if(req == ''):
            req = 'en'
        print("The user's request is: ", request)
        try:

            # English Wepsite
            if request == '' or request == 'en':
                connectionSocket.send(f"HTTP/1.1 200 ok \r\n".encode())
                disPage= 'main_en.html'
                disfile = open(disPage, "rb")
                response = disfile.read()
                disfile.close()
                connectionSocket.send(f"\r\n".encode())
                connectionSocket.send(response)
                connectionSocket.close()

            # Arabic Wepsite
            elif request == 'ar':
                connectionSocket.send(f"HTTP/1.1 200 ok \r\n".encode())
                disPage = 'main_ar.html'
                disfile = open(disPage, "rb")
                response = disfile.read()
                disfile.close()
                connectionSocket.send(f"\r\n".encode())
                connectionSocket.send(response)
                connectionSocket.close()

            # 307 Temporary Redirect to google.com
            elif request == 'go':
                connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
                response = (b"location: http://www.google.com")
                connectionSocket.send(response)
                connectionSocket.close()

            # 307 Temporary Redirect to cnn.com
            elif request == 'cn':
                connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
                response = (b"location: https://edition.cnn.com")
                connectionSocket.send(response)
                connectionSocket.close()

            # 307 Temporary Redirect to the arabic Birzeit.edu
            elif request == 'bzu':
                connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
                response = (b"location: https://www.birzeit.edu/ar")
                connectionSocket.send(response)
                connectionSocket.close()

            # Open an HTML file
            elif request.endswith('.html'):
                connectionSocket.send(f"HTTP/1.1 200 ok \r\n".encode())
                disfile = open(request, "rb")
                response = disfile.read()
                disfile.close()
                connectionSocket.send(f"\r\n".encode())
                connectionSocket.send(response)
                connectionSocket.close()

            # Open a CSS file
            elif request.endswith('.css'):
                connectionSocket.send(f"HTTP/1.1 200 ok \r\n".encode())
                disfile = open(request, "rb")
                response = disfile.read()
                disfile.close()
                connectionSocket.send(f"\r\n".encode())
                connectionSocket.send(response)
                connectionSocket.close()

            # Open a city jpg picture
            elif request.endswith(".jpg"):
                connectionSocket.send(f"HTTP/1.1 200 ok \r\n".encode())
                try:
                    disfile = open(request, "rb")
                except Exception as exp:
                    disfile = open('city.jpg', "rb")
                response = disfile.read()
                connectionSocket.send(f"\r\n".encode())
                connectionSocket.send(response)
                connectionSocket.close()

            # Open a png picture of game of thrones logo
            elif request.endswith(".png"):
                connectionSocket.send(f"HTTP/1.1 200 ok \r\n".encode())
                try:
                    disfile = open(request, "rb")
                except Exception as exp:
                    disfile = open('gameOfThrones.png', "rb")
                response = disfile.read()
                connectionSocket.send(f"\r\n".encode())
                connectionSocket.send(response)
                connectionSocket.close()

            # Any other Case to give the error file
            else :
                connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
                response = (
                            '<html><title>Error</title><body><center><h1 style="color:red">Error 404: The file is not found</h1><hr><p style= "font-weight: bold;">Omar Tawafshah - 1191768</p><p style= "font-weight: bold;">Ahmaide Al-Awawdeh - 1190823</p><hr><h2>IP: ' + str(
                        IP_address) + ', Port: ' + str(Connected_port) + '</h2></center></body></html>').encode()
                connectionSocket.send(f"\r\n".encode())
                connectionSocket.send(response)
                connectionSocket.close()

        # Also give the error file if an actuall error accured
        except Exception as DidNotWork:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
            response = ('<html><title>Error</title><body><center><h1 style="color:red">Error 404: The file is not found</h1><hr><p style= "font-weight: bold;">Omar Tawafshah - 1191768</p><p style= "font-weight: bold;">Ahmaide Al-Awawdeh - 1190823</p><hr><h2>IP: ' + str(
                IP_address) + ', Port: ' + str(Connected_port) + '</h2></center></body></html>').encode()

        print(sentence)
