import pyautogui
import time
import random

def move_mouse():
    screenWidth, screenHeight = pyautogui.size()
    while True:
       
        x = random.randint(0, screenWidth)
        y = random.randint(0, screenHeight)
        
        pyautogui.moveTo(x, y, duration=0.5)
        
        time.sleep(random.randint(5, 30))

if __name__ == "__main__":
    move_mouse()
