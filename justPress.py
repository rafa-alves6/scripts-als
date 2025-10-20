import pyautogui
import keyboard
import pyperclip
import time
import threading

# --- Configuration ---
target_x = 653
target_y = 133

# --- User Input ---
while True:
    try:
        first_number = int(input("Enter the starting number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# --- MAIN ACTION FUNCTION ---
def perform_action(navigate_first):
    """
    A single function to handle the entire automation sequence.
    It decrements the number and performs all keyboard/mouse actions.

    Args:
        navigate_first (bool): If True, it presses 'tab' and 'up' first.
    """
    global first_number

    # Decrement the number and copy it to the clipboard
    first_number += 1
    pyperclip.copy(str(first_number))  # Copy the incremented number to the clipboard
    print(f"Incremented number '{first_number}' has been copied to the clipboard.")
    
    # Conditionally press 'tab' and 'up'
    if navigate_first:
        pyautogui.press('tab')
        pyautogui.press('up')

    # Perform the rest of the actions
    pyautogui.moveTo(target_x, target_y)
    pyautogui.click()
    
    # Press Enter
    pyautogui.press('enter')
    
    # Save (Ctrl + S)
    pyautogui.hotkey('ctrl', 's')
    print(f"Action complete. Ctrl + S pressed.")
    
    # Paste (Ctrl + V)
    pyautogui.hotkey('ctrl', 'v')
    print(f"Incremented number '{first_number}' has been pasted.")

# --- Hotkey Wrappers ---
def on_f5_press():
    """For the first item on a page; includes navigation."""
    perform_action(navigate_first=True)

def on_f6_press():
    """For subsequent items; skips initial navigation."""
    perform_action(navigate_first=False)

# --- User Command Handler ---
def handle_user_input():
    """
    Continuously listens for the user commands: 'increment', 'decrement', or 'set new'.
    """
    global first_number
    
    while True:
        user_input = input("\nEnter a command ('increment', 'decrement', 'set new', 'exit'): ").strip().lower()

        if user_input == 'increment':
            first_number += 1
            pyperclip.copy(str(first_number))  # Copy to clipboard after increment
            print(f"Number incremented to {first_number}. Copied to clipboard.")
        elif user_input == 'decrement':
            first_number -= 1
            pyperclip.copy(str(first_number))  # Copy to clipboard after decrement
            print(f"Number decremented to {first_number}. Copied to clipboard.")
        elif user_input == 'set new':
            try:
                new_number = int(input("Enter the new number: "))
                first_number = new_number
                pyperclip.copy(str(first_number))  # Copy to clipboard after setting new number
                print(f"New number set to {first_number}. Copied to clipboard.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")
        elif user_input == 'exit':
            print("Exiting input handling.")
            break
        else:
            print("Invalid command. Please use 'increment', 'decrement', 'set new', or 'exit'.")

# --- Hotkey Setup ---
keyboard.add_hotkey('f5', on_f5_press)
keyboard.add_hotkey('f6', on_f6_press)

print(f"Script is running. Press F5 (with nav) or F6 (without nav). Starting number is {first_number}.")
print("Press Ctrl + C to exit.")

# Start the user input handling in a separate thread
input_thread = threading.Thread(target=handle_user_input, daemon=True)
input_thread.start()

# Keep the script running
try:
    while True:
        time.sleep(1)  # This keeps the main thread alive and responsive to hotkeys
except KeyboardInterrupt:
    print("\nScript terminated by user.")
