import pyautogui
import keyboard
import time

end = False
temp1 = time.time()
tick = 0

while end != True:
    #if keyboard.is_pressed("h") == True:

        #print(mouse.get_position())

    temp2 = time.time()
    if temp2 - temp1 >= 0.05:
        tick = tick + 1
        pyautogui.moveTo(3321, 542)
        pyautogui.click()
    
        if tick % 10 == 0:
            pyautogui.moveTo(2135, 472)
            pyautogui.click()
            pyautogui.moveTo(2135, 572)
            pyautogui.click()

        if tick % 50 == 0:
            pyautogui.moveTo(3431, 62)
            pyautogui.click()
    
    

    if keyboard.is_pressed("s") == True:
        end = True