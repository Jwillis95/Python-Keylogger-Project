## Python-Keylogger-Project


#Ethical Considerations

This project is purely for educational purposes, and I do not endorse or encourage any malicious use of this code. This project is simply designed to demonstrate my understanding of keyloggers and Python, and misuse of this project could result in legal action against those responsible. I take no responsibility for what others may choose to do with this information.


#Python Keylogger Project

This is a project primarily demonstrating a Python keylogger. It uses pynput to capture user input, which is the encrypted and sent to a server using sockets.


#Prerequisites

- Python3
- The proper libraries: Socket, Pynput, Cryptography

While socket is a default library, Pynput and Cryptography can be installed by entering "pip install pynput cryptography" into your terminal.


#Instructions

This keylogger is built to function on two separate computers. "PyKey.py" is intended to run on a target machine, which upon execution will send that device's keystrokes to the server, which will run "keylogger server.py".
Enter the "PyKey.py" and "keylogger server.py" files, and enter the host IP address in place of "Your server IP here".
Run "keylogger server.py" first, followed by "PyKey.py". The terminal should indicate that the server is running, and that "PyKey.py" was successfully executed.
You should be able to view the keystrokes from your target computer within "Keystroke Log Desktop.txt".


#Primary Files

PyKey.py - The file which runs on the target machine. This file will connect to the keylogger server and send encrypted keystrokes, as well as save aforementioned keystrokes locally in "Keystroke Log.txt".
keylogger server.py - Receives keystrokes from PyKey.py and encrypts the data, writing the decrypted data to "Keystroke Log Desktop.txt".


#Additional Files

control.py - Demonstrates the ability of the Controller module to send commands to both a keyboard or mouse. While not utilized in the keylogger itself, this code was featured in a tutorial I followed, and the capabilities outlined in this file could prove interesting in future projects.
listen.py - Tracks the (x,y) coordinates of your mouse, outputting the coordinates to the terminal. Included for similar reasons as "control.py".
keys.py - What I used to generate the keys to decrpyt incoming keystrokes.


#Contact

Feel free to contact me on Github, and I will answer any questions I can.


#Acknowledgements

"Building a keylogger using Pythong + Pynput" - buildwithpython 
https://youtube.com/playlist?list=PLhTjy8cBISEoYoJd-zR8EV0NqDddAjK3m&si=WNsil91c_uvRhWGK
