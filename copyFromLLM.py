import keyboard
import pyautogui as pag
import time

def do_stuff():
    pag.tripleClick()
    pag.hotkey('ctrl', 'c')
    pag.hotkey('alt', 'tab')
    pag.hotkey('ctrl', 'v')
    pag.press('down')

KEY_TO_PRESS = 'f2'
key_pressed = False  # Variável para verificar se a tecla foi pressionada

while True:
    time.sleep(0.2)
    if keyboard.is_pressed(KEY_TO_PRESS) and not key_pressed:  # Verifica se a tecla foi pressionada e não foi executado ainda
        do_stuff()
        key_pressed = True  # Marca que a tecla foi pressionada e a ação foi executada
    elif not keyboard.is_pressed(KEY_TO_PRESS):  # Se a tecla for solta
        key_pressed = False  # Permite que a ação seja executada novamente na próxima vez que a tecla for pressionada
