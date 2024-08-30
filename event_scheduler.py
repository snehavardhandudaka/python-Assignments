from datetime import datetime
import calendar

def create_event(date, event):
    with open('events.txt', 'a') as f:
        f.write(f"{date}: {event}\n")

def view_calendar(month, year):
    return calendar.month(year, month)

date = '2024-08-30'
event = 'Team Meeting'
create_event(date, event)
print(view_calendar(8, 2024))
