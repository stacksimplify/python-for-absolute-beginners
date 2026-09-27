"""
Workshop Problem-04: if / elif / else (Service Due?) (solution)

Concepts: if / elif / else.

Write a program that, for a km reading of 18000, prints the service status
using if / elif / else: "No service yet" when under 10000, "Service soon"
when under 20000, "Service due" when under 30000, and "Service overdue"
otherwise.

Expected output: Service soon
"""

km = 18000
if km < 10000:
    print("No service yet")
elif km < 20000:
    print("Service soon")
elif km < 30000:
    print("Service due")
else:
    print("Service overdue")
