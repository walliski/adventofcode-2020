with open('input.txt', 'r') as content:
    lines = content.readlines()

# We can just convert the numbers into binary like this: b->1, f->0 and r->1, l->0
seats = list(map((lambda x: int(x[:7].replace("B","1").replace("F","0"), 2) * 8 + int(x[7:].replace("R","1").replace("L","0"), 2)), lines))
print("Step 1: ", max(seats))

# Check through all seats and see if the one before and after are taken, but middle on is not.
# Not really optimal I guess, a lot of lookups. Sorting and finding a hole might be more efficient.
for i in range(min(seats), max(seats)):
    if (i - 1 in seats) and not (i in seats) and (i + 1 in seats):
        print("Step 2: ", i)
        break
