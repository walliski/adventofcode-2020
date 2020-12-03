with open('input.txt', 'r') as content:
    lines = content.readlines()

slopes = ["1x1", "3x1", "5x1", "7x1", "1x2"]

width = len(lines[0])
treeCounts = {}

for slope in slopes:
    treeCounts[slope] = 0

for i, line in enumerate(lines):
    for slope in slopes:
        x, y = map(int, slope.split("x"))
        # Adding + 1 for i, since we are starting to move from the first line, so if we move 2 lines down, we will end
        # up on line 3, not 2. :thinking:
        if (i + 1) % y == 0 and line[(i * x) % (width - 1)] == "#":
            treeCounts[slope] += 1

multiplied = 1

for slope in treeCounts:
    print("Tree count for ", slope, ": ", treeCounts[slope])
    multiplied *= treeCounts[slope]

print("Multiplied count of all slopes: ", multiplied)
