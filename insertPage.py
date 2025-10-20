import pyautogui
import pyperclip
import time
import keyboard

# Global variable to store and update the current number
numero_atual = 0

def formatar_numero(numero):
    """
    Formats the number to have at least 3 digits (e.g., 20 -> "020").
    """
    return str(numero).zfill(3)

def executar_sequencia():
    """
    The main action sequence. It's now triggered by the hotkey.
    """
    # Use the global variable to get and update the number
    global numero_atual
    
    numero_formatado = formatar_numero(numero_atual)
    print(f"--- F4 Pressionado ---")
    print(f"Processando número: {numero_formatado}")
    
    # 1. Give yourself a moment to release the F4 key
    time.sleep(0.2)
    
    # 2. Copy the number to the clipboard
    pyperclip.copy(numero_formatado)
    time.sleep(0.2)

    # 3. Paste the number
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)

    # 4. Press 'down' 2x
    pyautogui.press('down', presses=2)
    time.sleep(0.1)

    # 5. Press 'end'
    pyautogui.press('end')
    time.sleep(0.1)

    # 6. Press 'enter' 2x
    pyautogui.press('enter', presses=2)
    time.sleep(0.1)

    # 7. Press ctrl + j
    pyautogui.hotkey('ctrl', 'j')
    time.sleep(0.2)

    # 8. Press ctrl + n
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(0.2)
    
    # 9. Press CTRL + SHIFT + <
    pyautogui.hotkey('ctrl', 'shift', '<')
    
    # 10. Increment the number for the next run
    numero_atual += 1
    print(f"Ação concluída. Próximo número: {numero_atual}. Aguardando F4...")

def main():
    """
    Sets up the hotkey and waits.
    """
    # Use the global variable to set the initial number
    global numero_atual
    
    try:
        numero_inicial_str = input("Digite o número inicial: ")
        numero_atual = int(numero_inicial_str)

        print("\n✅ Script ativado em segundo plano.")
        print("Seu teclado está livre!")
        print("Pressione F4 para executar a ação.")
        print("\n>>> Pressione Ctrl + C a qualquer momento para encerrar o script. <<<")
        listenKey = 'f2'
        # Registers the hotkey. When 'f4' is pressed, it calls the 'executar_sequencia' function.
        # suppress=True ensures the F4 press doesn't leak into other apps.
        keyboard.add_hotkey(listenKey, executar_sequencia, suppress=True)

        # This keeps the script running in the background, waiting for the hotkey.
        # It will wait until you press 'Ctrl + C' in the terminal to stop.
        while True:
            time.sleep(1)  # Keeps the script alive, waiting for the hotkey

    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário (Ctrl + C).")
    except ValueError:
        print("\nErro: O valor inicial precisa ser um número.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()
