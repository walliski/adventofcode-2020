with open('input_test.txt', 'r') as content:
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
