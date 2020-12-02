# 7-8 p: ppppppdx

with open('input.txt', 'r') as content:
    lines = content.readlines()

validCount = 0

for line in lines:
    splitLine = line.replace(":", "")
    minMaxCounts, letter, password = splitLine.split(" ")
    minCount, maxCount = minMaxCounts.split("-")

    if int(minCount) <= password.count(letter) <= int(maxCount):
        validCount += 1

print("Valid count step 1: ", validCount)

validCount = 0

for line in lines:
    splitLine = line.replace(":", "")
    positions, letter, password = splitLine.split(" ")
    posA, posB = positions.split("-")

    if (password[int(posA) - 1] == letter) != (password[int(posB) - 1] == letter):
        validCount += 1

print("Valid count step 2: ", validCount)
