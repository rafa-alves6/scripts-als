import pyautogui as pag
import keyboard
import time

KEY_TO_PRESS = 'f9'

# This flag will help us know if the key was already being held down
key_was_pressed = False

print("Script is running. Press F9 to execute the actions. Press Ctrl+C to quit.")

while True:
    try:
        # Check if the key is currently pressed
        if keyboard.is_pressed(KEY_TO_PRESS):
            # If it's pressed now, but wasn't pressed in the previous check
            if not key_was_pressed:
                print(f"'{KEY_TO_PRESS}' key pressed, executing actions...")
                # --- YOUR ACTIONS START HERE ---
                pag.doubleClick()
                pag.hotkey('ctrl', 'c')
                time.sleep(0.1)	
                pag.hotkey('alt', 'tab')
                time.sleep(0.1)
                pag.hotkey('ctrl', 'v')
                time.sleep(0.1)
                pag.press('down')
                # --- YOUR ACTIONS END HERE ---
                
                # Set the flag to True so these actions don't repeat while the key is held down
                key_was_pressed = True
        else:
            # If the key is not pressed, reset the flag
            key_was_pressed = False
            
        # A small delay to prevent the loop from consuming too much CPU
        time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nScript terminated by user.")
        break