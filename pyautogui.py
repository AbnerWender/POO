import pyautogui as gui

gui.press('win')
gui.typewrite('notepad')
gui.press('enter')

gui.typewrite('Olá, PyAutoGUI')
gui.hotkey('ctrl', 's')
gui.typewrite('exemplo.txt')
gui.press('enter')