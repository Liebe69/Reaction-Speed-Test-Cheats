import pyautogui
#this program is for the human benchmark reaction speed test
# (https://humanbenchmark.com/tests/reactiontime)

#creates the main loop
while True:
    #looks for the image of the text that says "click" and then clicks on it within 70 ms MAX
    try:
        x,y = pyautogui.locateCenterOnScreen("cheat.png",confidence = 0.7,grayscale=True, region=(848,388,203,76))
        pyautogui.click(x,y)
    except: pass
