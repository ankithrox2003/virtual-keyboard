import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize hand detector
detector = HandDetector(detectionCon=0)

# Define the keys layout
keys = [["Delete", "Space"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", "'"],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]]

# Initialize text
finalText = ""

# Initialize the keyboard controller
keyboard = Controller()

# Function to draw buttons
def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]), 20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 2 if button.text == "Space" else 4, (255, 255, 255), 4)
    return img

# Button class
class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

# Create button list
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        if key == "Space":
            buttonList.append(Button([j * 100 + 50, 100 * (len(keys) - 1 - i) + 50], key, size=[250, 95]))
        elif key == "Delete":
            buttonList.append(Button([j * 500 + 450, 100 * (len(keys) - 1 - i) + 50], key, size=[250, 85]))
        else:
            buttonList.append(Button([j * 100 + 50, 100 * (len(keys) - 1 - i) + 50], key))

# Main loop
while True:
    success, img = cap.read()
    
    # Flip the image horizontally
    img = cv2.flip(img, 1)
    
    img = detector.findHands(img)
    lmList, bBoxInfo = detector.findPosition(img)
    img = drawAll(img, buttonList)
    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 2 if button.text == "Space" else 4, (255, 255, 255), 4)
                l, _, _ = detector.findDistance(8, 12, img, draw=False)
                print(l)

                # When Clicked
                if l > 45 and l < 50:
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 2 if button.text == "Space" else 4, (255, 255, 255), 4)
                    if button.text == "Space":
                        finalText += " "
                        keyboard.press(' ')
                        keyboard.release(' ')
                    elif button.text == "Delete":
                        finalText = finalText[:-1]
                        keyboard.press('\b')
                        keyboard.release('\b')
                    else:
                        finalText += button.text
                        keyboard.press(button.text.lower())
                        keyboard.release(button.text.lower())
                    sleep(0.25)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
