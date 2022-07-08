#!/usr/local/bin/python3
from datetime import datetime, date, time
# Import time with an alias to prevent colliding with datetime
import time as t

# Pause execution for n seconds
t.sleep(1)

# Start the benchmark time needed to execute
start = t.perf_counter()

# Get current time and date
now = datetime.now()
print("Current time and date: ", now)
print("Year: ", now.year)
print("Month: ", now.month)
print("Day: ", now.day)
print("Hour: ", now.hour)
print("Minute: ", now.minute)
print("Seconds: ", now.second)
print()

#24-hour format
print(now.strftime("Date: %m/%d/%Y Time: %H:%M:%S"))

#12-hour format
print(now.strftime("Date: %m/%d/%Y Time: %I:%M:%S"))

# Create a datetime object
customDate = date(2018, 7, 21) # (year, month, day)
customTime = time(4, 7) # (hour, minute)
customDateTime = datetime.combine(customDate, customTime)
print(customDateTime)

# Stop the benchmark time needed to execute
stop = t.perf_counter()
print("\nExecution time: ", start - stop)
