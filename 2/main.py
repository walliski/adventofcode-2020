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

print("Valid count: ", validCount)
