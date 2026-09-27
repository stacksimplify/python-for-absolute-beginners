# Concept-01: dir() shows what is inside a module; math.sqrt is one of the tools it lists
# Question: How do we see what math offers, and then use one of those tools? (dir(math), then math.sqrt(144) -> 12.0)
import math

# dir() lists every name inside a module.
all_names = dir(math)

# Python keeps a few private names of its own. They start with an underscore, so skip them.
math_tools = [tool for tool in all_names if not tool.startswith("_")]

print("names in math:", len(all_names))
print("tools you can use:", len(math_tools))
print(", ".join(math_tools))

# math.sqrt is one of those tools. Reach for it with a dot.
print("square root of 144 is:", math.sqrt(144))

# Concept-02: math.floor rounds DOWN, math.ceil rounds UP, unlike round() which goes to the nearest
# Question-1: How do we round 4.7 DOWN to the nearest whole number? (math.floor(4.7) -> 4)
# Question-2: How do we round 4.2 UP to the nearest whole number? (math.ceil(4.2) -> 5)
import math

# E1: First, the round() you met in Section 02. It goes to whichever whole number is NEAREST.
print("round(4.7):", round(4.7))
print("round(4.2):", round(4.2))

# E2: Second, floor and ceil. They IGNORE which is nearer and always go their own way.
print("floor of 4.7 is:", math.floor(4.7))
print("ceil of 4.2 is:", math.ceil(4.2))

# Concept-03: math also holds handy constants; math.pi is the value of pi
# Question: How do we use the exact value of pi without typing the digits ourselves? (math.pi)
import math
print("pi is about:", math.pi)

print("floor of pi is:", math.floor(math.pi))
print("ceil of pi is:", math.ceil(math.pi))

# Concept-04: the statistics module is another batteries-included toolbox; statistics.mean gives the average
# Question: How do we find the average (mean) of a list of scores [85, 90, 78, 92, 88] without adding them up and dividing ourselves? (statistics.mean)
import statistics

scores = [85, 90, 78, 92, 88]

# E1: by hand with a running total, the way Section 06 taught it
total = 0
for score in scores:
    total += score
print("by hand:", total / len(scores))

# E2: the statistics module does the same work in one call
print("statistics.mean:", statistics.mean(scores))
