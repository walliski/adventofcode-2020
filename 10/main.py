with open('input.txt', 'r') as content:
    lines = list(map(int, content.readlines()))

# Add the first and last:
lines.append(0)
lines.append(max(lines)+3)

# Get how many 1 and 3 diffs there are
lines.sort()

diffs = {"1": 0, "2": 0, "3": 0}

for i in range(len(lines)-1):
    diffs[str(lines[i+1] - lines[i])] += 1

print("Diff counts:", diffs)
print("Step 1 answer:", diffs["1"] * diffs["3"])


# Part 2

# Not my solution, I got stuck at trying to look forward and figure out the amount of combinations like that.
# I was also looking at one element at a time, and while I figured out that that wont work in all cases, I still
# could not figure out how to take them all into consideration...

# Here is a solution borrowed from the great internet though:

from collections import Counter

# Counter is like a dict, but returns 0 by default if element not set.
combs = Counter()

# There is 1 way to get to the first element
combs[0] = 1

# 1: because we have the value for 0 already.
for line in lines[1:]:
    combs[line] = combs[line-1] + combs[line-2] + combs[line-3]

print("Step 2 answer:", combs[lines[-1]])
