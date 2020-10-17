def update(): # method that loops some activity every 10 seconds
    import time
    while True:
        # do some activity
        time.sleep(10) # pauses program for 10 seconds

update() # calls method "update" which will infinitely loop
