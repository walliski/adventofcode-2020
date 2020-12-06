with open('input.txt', 'r') as content:
    lines = content.readlines()

charCount = {}
answerCounts = 0

for line in lines:
    if line.isspace():
        answerCounts += len(charCount.keys())
        print(charCount)
        charCount = {}

    for char in line.strip():
        if char not in charCount:
            charCount[char] = 0
        charCount[char] += 1

print("Step 1 sum: ", answerCounts)
