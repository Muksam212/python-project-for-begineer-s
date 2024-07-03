import time

print("Press Enter To Start, Press Ctrl+C To Stop")

while True:
    try:
        input()
        start_time = time.time()
        print("Started")
    except KeyboardInterrupt:
        print("Stopped")
        end_time = time.time()
        print("Total time: ", round(end_time - start_time, 2), 'secs')
        break