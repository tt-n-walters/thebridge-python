import time


seconds = 0

while seconds <= 72000:
    print("  " + str(seconds // 3600) + ":" + str(seconds // 60 % 60) + ":" + str(seconds % 60), seconds, time.time(), end="\r")

    seconds = seconds + 1
    # time.sleep(0.0001)
    
print()
