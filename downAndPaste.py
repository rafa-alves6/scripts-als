import pyautogui as pag
import keyboard

mat = "MAT. "

def downAndPaste():
    while keyboard.is_pressed('f9'):
        pag.press('home')
        pag.hotkey('ctrl','v')          # Digita o conteúdo da string mat
        pag.press('down')       # Pressiona a seta para baixo

print("Pressione F9 para iniciar o loop. Solte a tecla para parar.")

# Loop principal
while True:
    if keyboard.is_pressed('f9'):
        downAndPaste()
