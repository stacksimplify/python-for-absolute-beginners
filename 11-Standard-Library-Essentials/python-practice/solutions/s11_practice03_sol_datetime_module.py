"""
Practice Problem-03: datetime module (solution)

Concepts: datetime(y, m, d), strftime, strptime, reading parts, timedelta.

Problem-1 (Ship and Arrival Dates): Write a program that builds a datetime ship_date for 5 March 2026 and an arrival_date 5 days
           after it (add a timedelta of 5 days), then prints these labeled lines:
             Task-1: ship_date formatted as "%d %B %Y" (use strftime).
             Task-2: the month of ship_date (use .month).
             Task-3: arrival_date formatted as "%d %B %Y" (use strftime).
             Task-4: the days in transit: subtract ship_date from arrival_date and read .days.

Expected output:
ship date: 05 March 2026
month: 3
arrival date: 10 March 2026
days in transit: 5
"""
from datetime import datetime, timedelta

ship_date = datetime(2026, 3, 5)

# Problem-1 Task-1: print ship_date formatted as day month year
print("ship date:", ship_date.strftime("%d %B %Y"))
# Problem-1 Task-2: print the month of ship_date
print("month:", ship_date.month)

arrival_date = ship_date + timedelta(days=5)
# Problem-1 Task-3: print arrival_date formatted as day month year
print("arrival date:", arrival_date.strftime("%d %B %Y"))
# Problem-1 Task-4: print the days in transit (arrival_date minus ship_date, read .days)
days_in_transit = arrival_date - ship_date
print("days in transit:", days_in_transit.days)

"""
Problem-2 (Sale Day From Text): Write a program that parses the text "2026-11-27" (the store's sale day) into a date (use datetime.strptime
           with the format "%Y-%m-%d"), then prints these labeled lines:
             Task-1: the parsed date formatted as "%d %B %Y" (use strftime).
             Task-2: the year of the parsed date (use .year).

Expected output:
sale day: 27 November 2026
year: 2026
"""
sale_day = datetime.strptime("2026-11-27", "%Y-%m-%d")
# Problem-2 Task-1: print the parsed date formatted as day month year
print("sale day:", sale_day.strftime("%d %B %Y"))
# Problem-2 Task-2: print the year of the parsed date
print("year:", sale_day.year)
