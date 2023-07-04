import pyautogui
import time
import tkinter as tk

def screenshot():
    # time.sleep(5)
    name = time.time()
    name = 'C:/Users/Hamse/OneDrive/Documents/Codes/Github/Python/Screenshot-App/{}.png'.format(name)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,text="Take ScreenShot",command=screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(frame,text="Quit",command=quit)
close.pack(side=tk.LEFT)

root.mainloop()
