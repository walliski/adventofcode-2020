with open('input.txt', 'r') as content:
    lines = content.readlines()

charCount = {}
answerCounts = 0
groupCount = 0
everyoneCount = 0

for line in lines:
    if line.isspace():
        # Calculate Step 1 sum
        answerCounts += len(charCount.keys())

        # Calculate step 2 count
        for cCount in charCount.values():
            if cCount == groupCount:
                everyoneCount += 1

        # Reset
        charCount = {}
        groupCount = 0
    else:
        groupCount += 1

        for char in line.strip():
            if char not in charCount:
                charCount[char] = 0
            charCount[char] += 1

print("Step 1 sum: ", answerCounts)
print("Step 2 sum: ", everyoneCount)
