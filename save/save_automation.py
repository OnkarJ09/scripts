import schedule
import time
import pyautogui


def job():
    pyautogui.hotkey('ctrl', 's')
    print("Saved")

# Schedule task every 10 seconds
schedule.every(10).seconds.do(job)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Scheduler stopped.")
    