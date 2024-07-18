from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse = Controller()
    mouse.position = (1000,200)

controlMouse()


def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Test!")

controlKeyboard()
