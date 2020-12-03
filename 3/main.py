with open('input.txt', 'r') as content:
    lines = content.readlines()

width = len(lines[0])
treeCount = 0

for i, line in enumerate(lines):
    if i > 0 and line[(i * 3) % (width - 1)] == "#":
        treeCount += 1

print("Tree count: ", treeCount)
