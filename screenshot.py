import pyautogui
import time

def screenshot():
    # time.sleep(5)
    name = time.time()
    name = 'C:/Users/Hamse/OneDrive/Documents/Codes/Github/Python/Screenshot-App/{}.png'.format(name)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()

screenshot()