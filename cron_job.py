# Start doing a task at specific time at specific intervals and stop at specific time

import schedule
import time
import datetime
import sys


def start_doing():
    nows = datetime.datetime.now()
    print ("Started at :" + str(nows.strftime("%d-%m-%Y %H:%M")))


def stop_doing():
    nows = datetime.datetime.now()
    print ("Stopped at :" + str(nows.strftime("%d-%m-%Y %H:%M")))
    sys.exit()


schedule.every().day.at("09:30").do(start_doing)  # Start the task at 9.30 AM

while True:
    schedule.run_pending()
    # Delay the task for 30 minutes interval
    time.sleep(1800)
    start_doing()
    schedule.every().day.at('17:30').do(stop_doing)  # Stop the task at 5.30 PM

