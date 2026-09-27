"""
Practice Problem-02: append and read lines (solution)

Concepts: mode "a" (append), reading a file line by line, strip(), input().
"""
from pathlib import Path

"""
Problem-1: Orders Log.
Write a program that writes "order-1" to "orders_log.txt", then appends "order-2" and "order-3" to the same file, then:
  Task-1: read the file line by line and print each line as "order: <text>" (strip the newline).
  Task-2: read the whole file again with .readlines() and print how many orders there are, as "orders logged: <count>".

Expected output:
order: order-1
order: order-2
order: order-3
orders logged: 3
"""
with open("orders_log.txt", "w", encoding="utf-8") as f:
    f.write("order-1\n")
with open("orders_log.txt", "a", encoding="utf-8") as f:
    f.write("order-2\n")
    f.write("order-3\n")
with open("orders_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("order:", line.strip())

# Problem-1 Task-2: readlines() gives the whole file as a list, so len() counts the orders
with open("orders_log.txt", "r", encoding="utf-8") as f:
    all_orders = f.readlines()
print("orders logged:", len(all_orders))

Path("orders_log.txt").unlink()

"""
Problem-2 (Write a Program): Add an Order.
Write a program that asks the user for an order, writes "Today's orders:" to "daily_orders.txt", appends the typed order to the same file, then reads the file back and prints it.

Example run (you type "Wireless Mouse"): Today's orders: / Wireless Mouse
"""
order = input("Enter an order: ")
with open("daily_orders.txt", "w", encoding="utf-8") as f:
    f.write("Today's orders:\n")
with open("daily_orders.txt", "a", encoding="utf-8") as f:
    f.write(order + "\n")
with open("daily_orders.txt", "r", encoding="utf-8") as f:
    print(f.read())
Path("daily_orders.txt").unlink()
