import time

seconds = 0
minutes = 0
hours = 0

while True:
    print(hours, minutes, seconds)

    seconds = seconds + 1
    if seconds == 60:
        minutes = minutes + 1
        seconds = 0
    
    if minutes == 60:
        hours = hours + 1
        minutes = 0
    
    time.sleep(0.001)
