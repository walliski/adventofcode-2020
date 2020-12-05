with open('input.txt', 'r') as content:
    lines = content.readlines()

# b1 f0
# r1 l0

print("Step 1: ", max(map((lambda x: int(x[:7].replace("B","1").replace("F","0"), 2) * 8 + int(x[7:].replace("R","1").replace("L","0"), 2)), lines)))