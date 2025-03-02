import time
import win32gui
import pygetwindow as gw
from pynput import keyboard
from main import execute_kaggle

# List of common apps where text is written
TEXT_EDITORS = [
    "notepad", "wordpad", "word", "chrome", "firefox", "edge", "visual studio",
    "pycharm", "sublime", "vscode", "cmd", "powershell", "terminal", "explorer", "searchui"
]


TARGET_WORD = "you phrase for opening an application"  # The word to detect when not being written anywhere
typed_buffer = ""  # Buffer to track typed characters


def get_active_window():
    """Returns the active window title and process name."""
    hwnd = win32gui.GetForegroundWindow()  # Get active window handle
    title = win32gui.GetWindowText(hwnd)   # Get window title
    for win in gw.getWindowsWithTitle(title):  # Get app name from window
        return title, win.title.lower()
    return title, ""

def on_press(key):
    global typed_buffer
    """Callback function when a key is pressed."""
    try:
        if key == keyboard.Key.esc:  # Stop the script if 'Esc' is pressed
            # print("Stopping the program...")
            return False

        title, process = get_active_window()
        writing = any(app in process for app in TEXT_EDITORS)  # Check if it's a writing app

        if hasattr(key, 'char') and key.char is not None:  # Ensure it's a character key
            typed_buffer += key.char  # Append to buffer
            typed_buffer = typed_buffer[-len(TARGET_WORD):]


        if writing:
            # print(f"Key '{key.char}' is being written in {title}")
            pass
        else:
            # print(f"Key '{key.char}' is pressed but NOT being written anywhere.")

            if typed_buffer == TARGET_WORD:
                # print(f"⚠ ALERT: '{TARGET_WORD}' was typed but NOT written anywhere!")
                execute_kaggle()     

    except AttributeError:
        # Handle special keys (like Shift, Ctrl)
        if key == keyboard.Key.backspace:
            typed_buffer = typed_buffer[:-1]  # Remove last character on backspace
        elif key == keyboard.Key.esc:
            # print("Stopping the program...")
            return False  # Stop the listener
        # print(f"Special key '{key}' pressed.")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
