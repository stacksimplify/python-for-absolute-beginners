"""
Workshop Problem-03: range (Service Schedule)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

Concepts: for loop, range(), the step argument (including a negative step), list(range(...)), f-strings.

Write a program that, for a car serviced every 10000 km:
- Task-1: loop over the first 5 service numbers with range(1, 6) and print each
  milestone like Service 1: 10000 km.
- Task-2: then count DOWN the services left, from 5 to 1, with range(5, 0, -1)
  (a negative step), printing Countdown: 5 down to Countdown: 1, then Service due.
- Task-3: print list(range(1, 6)) to preview the service numbers as a real list.

Expected output: Service 1: 10000 km ... Service 5: 50000 km, Countdown: 5 ... 1, Service due, [1, 2, 3, 4, 5]
"""
