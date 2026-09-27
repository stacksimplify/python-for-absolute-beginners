# Concept-01: break stops the loop early; leave as soon as you are done
# Question: How do we stop as soon as we find the first score of 90 or above in [70, 95, 60, 88]? (break exits the loop right away)
# E1: no break - the loop announces the answer and then keeps checking the rest anyway
scores = [70, 95, 60, 88]
for score in scores:
    if score >= 90:
        print("first 90+:", score)
    print("still checking:", score)   # 95 is "still checking" right after we found it
# E2: break leaves the loop on the line that found the answer
scores = [70, 95, 60, 88]
for score in scores:
    if score >= 90:
        print("first 90+:", score)
        break
    print("still checking:", score)
print("done checking")

# Concept-02: break also exits a while True loop - the SAME search as Concept-01, now without a for
# Question: How do we find the first score of 90 or above in [70, 95, 60, 88] again, this time with a while True loop? (while True never ends on its own, so break is the only way out)
# E1: the older trick is a FLAG - but it only stops the loop at the NEXT trip to the top
scores = [70, 95, 60, 88]
i = 0
running = True
while running:
    if scores[i] >= 90:
        print("first 90+:", scores[i])
        running = False
    print("still checking:", scores[i])   # 95 is reported as "still checking" AFTER we found it
    i += 1
# E2: break leaves on the line that found it, so the turn really does stop
# CAREFUL: a while True that walks an index MUST be sure to find its match. With no 90+ score in
# the list, scores[i] would run past the end and raise IndexError - guaranteeing the exit is YOUR job.
scores = [70, 95, 60, 88]
i = 0
while True:
    if scores[i] >= 90:
        print("first 90+:", scores[i])
        break
    print("still checking:", scores[i])
    i += 1
print("done checking")

# Concept-03: continue skips the rest of THIS turn and jumps to the next item
# Question: How do we skip "Tom" but still give chocolate to every other name in ["Sam", "Tom", "Ben"]? (continue jumps to the next turn without leaving the loop)
# E1: no continue - we announce the skip, then hand Tom a chocolate anyway
names = ["Sam", "Tom", "Ben"]
for name in names:
    if name == "Tom":
        print("skipping", name)
    print("Give chocolate to:", name)
# E2: continue ends THIS turn, so the print below is never reached for Tom
names = ["Sam", "Tom", "Ben"]
for name in names:
    if name == "Tom":
        print("skipping", name)
        continue
    print("Give chocolate to:", name)
print("done")

# Concept-04: continue guards a loop by skipping bad values before the real work
# Question: How do we add up only the scores of 80 or above in [70, 95, 60, 88] and skip the rest? (continue past the low ones so the total stays clean)
scores = [70, 95, 60, 88]
total = 0
for score in scores:
    if score < 80:
        print("skipping low score:", score)   # without this line you never SEE the guard work
        continue
    total += score
print("total of 80+:", total)

# Concept-05: continue works inside a while loop too - but move the counter FIRST or it loops forever
# Question: How do we print the odd numbers 1 to 7 and skip the even ones with a while loop? (bump the counter before continue, or the skip freezes the loop)
# E1: counter AFTER the continue - the skip jumps back to the top with n unchanged, so the same
# even number is tested forever. This HANGS. Never uncomment it; Ctrl+C stops a runaway loop.
# n = 0
# while n < 7:
#     if n % 2 == 0:
#         continue      # n never moves, so this same even n is tested again, and again...
#     print("odd:", n)
#     n += 1
# E2: counter FIRST, so every turn moves n on before the skip can happen
n = 0
while n < 7:
    n += 1
    if n % 2 == 0:
        continue
    print("odd:", n)
print("done")

# Concept-06: pass is a do-nothing placeholder; the turn CARRIES ON, which is what makes it different from continue
# Question: How do we leave one branch empty on purpose, and still finish the rest of that turn? (pass does nothing and falls through; continue would jump to the next name)
# E1: an empty branch is not allowed - Python needs at least one line inside every block, so this
# file would not even start: IndentationError: expected an indented block after 'if' statement
# names = ["Sam", "Tom", "Ben"]
# for name in names:
#     if name == "Tom":
#     else:
#         print("greet", name)
# E2: pass fills the branch, and the turn carries on to the line below
names = ["Sam", "Tom", "Ben"]
for name in names:
    if name == "Tom":
        pass    # nothing special for Tom yet - fill this in later
    else:
        print("greet", name)
    print("logged", name)  # runs for EVERY name, Tom included - a continue here would have skipped it
print("done")

# Concept-07: A for loop can carry an else; it runs ONLY if the loop finished without break
# Question: How do we tell "Amy" was NOT in the list ["Sam", "Tom", "Ben"] after checking every name? (the else fires only because break never fired - the "searched all, found none" case)
# E1: the older way - track it with a flag. It works, but the flag is one more thing to keep in
# step: forget the found = True line and it reports "not found" for a name that IS in the list.
names = ["Sam", "Tom", "Ben"]
found = False
for name in names:
    if name == "Amy":
        found = True
        break
if not found:
    print("Amy is not in the list")
# E2: for ... else - the loop tracks it for you, and there is no flag to forget
names = ["Sam", "Tom", "Ben"]
for name in names:
    if name == "Amy":
        print("found Amy")
        break
else:
    print("Amy is not in the list")

# Concept-08: The same for else is SKIPPED when break fires - proving the rule
# Question: How do we see that finding "Sam" in ["Sam", "Tom", "Ben"] and breaking makes the else stay silent? (break fired, so the else block is skipped)
# This is Concept-07's second example with ONE name changed, "Amy" -> "Sam". Amy was never in the
# list so the break never fired and the else ran; Sam IS in it, so the break fires and the else is skipped.
names = ["Sam", "Tom", "Ben"]
for name in names:
    if name == "Sam":
        print("found Sam")
        break
else:
    print("Sam is not in the list")

# Concept-09: else works on a while loop too - it runs only if the while ended without break
# Question: How do we tell a countdown from 3 that finished on its own from one that a break cut short at n == 2? (the while else runs after a natural finish, but a break skips it)
# E1: the break is RIGHT THERE, but a countdown from 3 never reaches 4, so it never fires
# and the else runs. The else depends on whether break FIRED, not on whether break EXISTS.
n = 3
while n >= 1:
    if n == 4:
        print("stopped early")
        break
    print("countdown", n)
    n -= 1
else:
    print("finished on its own")

# E2: the SAME code with ONE number changed - n does reach 2, so the break fires and the else is SKIPPED
n = 3
while n >= 1:
    if n == 2:
        print("stopped early")
        break
    print("countdown", n)
    n -= 1
else:
    print("finished on its own")
