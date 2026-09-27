# The datetime module works with dates and times.

# Concept-01: dir() shows what is inside the datetime module, the same way it did for math and random
# Question: What does the datetime module hold, and where does the datetime we import come from?
import datetime

all_names = dir(datetime)
datetime_tools = [tool for tool in all_names if not tool.startswith("_")]

print("names in datetime:", len(all_names))
print("tools you can use:", len(datetime_tools))
print(", ".join(datetime_tools))

# Concept-02: Build a date with datetime(year, month, day), fixed here so the output never changes
# Question: How do we store a specific date like June 17, 2026 so we can use it in our code?
# datetime.now() would give the current time
from datetime import datetime, timedelta
event = datetime(2026, 6, 17)
print("the date is:", event)

# Concept-03: Read a date's parts with its .year, .month, and .day attributes
# Question: How do we pull out just the year, month, or day number from a date we already have, like datetime(2026, 6, 17)?
from datetime import datetime, timedelta
event = datetime(2026, 6, 17)
print("year:", event.year)
print("month:", event.month)
print("day:", event.day)

# Concept-04: strftime formats a date as text (%Y year, %m month, %d day, %B full month name)
# Question: How do we turn a date into a text string that reads naturally, like '17 June 2026' instead of showing computer format? (strftime is the tool)
from datetime import datetime, timedelta
event = datetime(2026, 6, 17)
print("formatted:", event.strftime("%Y-%m-%d"))
print("friendly: ", event.strftime("%d %B %Y"))

# Concept-05: timedelta is a length of time you can add or subtract
# Question: How do we add 7 days to a date like datetime(2026, 6, 17) to find when an event happens a week later? (timedelta(days=7))
from datetime import datetime, timedelta
event = datetime(2026, 6, 17)
one_week_later = event + timedelta(days=7)
print("one week later:", one_week_later.strftime("%d %B %Y"))

# Concept-06: strptime is the reverse of strftime; it reads a date OUT of a text string
# Question: How do we turn the text "2026-06-17" (say from a file) back into a real date we can use? (strptime parses text into a date)
from datetime import datetime, timedelta
parsed = datetime.strptime("2026-06-17", "%Y-%m-%d")
print("parsed date:", parsed)
print("parsed year:", parsed.year)

# Concept-07: subtracting two dates gives a timedelta; its .days tells how many days apart they are
# Question: How do we find how many days until an event, like from datetime(2026, 6, 3) to datetime(2026, 6, 17)? (subtract the dates; the result is a timedelta, read its .days)
from datetime import datetime, timedelta
event = datetime(2026, 6, 17)
today = datetime(2026, 6, 3)
days_left = event - today
print("days until event:", days_left.days)
