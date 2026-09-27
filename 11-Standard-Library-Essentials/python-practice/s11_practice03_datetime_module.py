"""
Practice Problem-03: datetime module

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
"""
Problem-2 (Sale Day From Text): Write a program that parses the text "2026-11-27" (the store's sale day) into a date (use datetime.strptime
           with the format "%Y-%m-%d"), then prints these labeled lines:
             Task-1: the parsed date formatted as "%d %B %Y" (use strftime).
             Task-2: the year of the parsed date (use .year).

Expected output:
sale day: 27 November 2026
year: 2026
"""
