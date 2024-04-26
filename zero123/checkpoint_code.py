import os
import signal
import time

def send_signal(pid):
    while True:
        print("Sending SIGUSR1 to process with ID:", pid)
        os.kill(pid, signal.SIGUSR1)
        time.sleep(600)  # pause for 10 minutes

if __name__ == "__main__":
    pid = int(input("Enter the process ID: "))
    send_signal(pid)