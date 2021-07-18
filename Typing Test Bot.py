# Variables
import pyautogui
import time

# The Words code
print("Enter the Words from the Type Racer which can be found in inspect element")
print("")
print("Copy and Paste them here: ")
words = input()

#The Frequency
print("Enter the Interval on how close a letter should be typed to another. Ex: 0.03 doing 100+ and 0.005 doing 250+")
print("")
print("Enter the Interval here: ")
Frequency = input()

#The Actual Typing Code
time.sleep(2)
pyautogui.typewrite(words, interval=Frequency);