import pyautogui
import time


loop_interval = 720
total_iteration = 0

while True:
    # Delay before starting the keypress simulation
    time.sleep(2)

    # Simulate holding down the keys Ctrl + Shift + 1
    print("-loom simulation starting-")
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('1')

    # Delay to hold the keys for a moment
    time.sleep(2)

    # Release the keys
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')

    total_iteration = total_iteration + 1
    print("Screenshot done. Total iteration: "+ str(total_iteration))

    # Countdown timer
    for remaining in range(loop_interval, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        print(f"Time left before next loom simulation: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)
