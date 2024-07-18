# Python Keylogger Project

## Ethical Considerations

This project is purely for educational purposes, and I do not endorse or encourage any malicious use of this code. This project is simply designed to demonstrate my understanding of keyloggers and Python, and misuse of this project could result in legal action against those responsible. I take no responsibility for what others may choose to do with this information.

## Overview

This project demonstrates a Python keylogger using pynput for capturing user input and cryptography for encrypting and transmitting data to a server using sockets.

## Prerequisites

- Python 3
- Required libraries: Socket, Pynput, Cryptography

To install the necessary libraries, run the following command in your terminal:

pip install pynput cryptography

## Instructions

### Running the Keylogger
1. Run `keys.py` to generate a key for encryption. This key will be used to encrypt and decrypt the keystrokes. Store the generated key securely.
2. Replace `"Your server IP here"` in `PyKey.py` with your server's IP address.
3. Run `keylogger_server.py` on your server machine first.
4. Run `PyKey.py` on the target machine (the machine you want to monitor).
5. Check the server terminal for confirmation that the server is running and receiving data.
6. View the keystrokes logged in `Keystroke Log Desktop.txt` on your server.

## Primary Files

- `PyKey.py`: Runs on the target machine to capture and send keystrokes.
- `keylogger_server.py`: Receives encrypted keystrokes from `PyKey.py` and logs them.
- `keys.py`: Used to generate encryption keys.

## Additional Files

- `control.py`: Demonstrates using the Controller module to manipulate keyboard and mouse inputs.
- `listen.py`: Outputs mouse coordinates to the terminal.

## Contact

Feel free to contact me on GitHub for any questions or feedback.

## Acknowledgements

Thanks to the tutorial "Building a keylogger using Python + Pynput" by buildwithpython on YouTube.
