"""
Workshop Problem-03: datetime module (Service Date) (solution)

Concepts: datetime(y, m, d), strftime, timedelta.

Write a program that builds a datetime bought for 15 March 2024 and a service date 180 days after it
(add a timedelta of 180 days), then prints these labeled lines:
  Task-1: bought formatted as "%d %B %Y" (use strftime).
  Task-2: the year of bought (use .year).
  Task-3: service formatted as "%d %B %Y" (use strftime).

Expected output:
bought: 15 March 2024
year: 2024
service due: 11 September 2024
"""
from datetime import datetime, timedelta

bought = datetime(2024, 3, 15)
# Task-1: print bought formatted as day month year
print("bought:", bought.strftime("%d %B %Y"))
# Task-2: print the year of bought
print("year:", bought.year)
service = bought + timedelta(days=180)
# Task-3: print service date formatted as day month year
print("service due:", service.strftime("%d %B %Y"))
