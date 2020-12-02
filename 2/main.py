# 7-8 p: ppppppdx

with open('input.txt', 'r') as content:
    lines = content.readlines()

validCount, validCount2 = 0, 0

for line in lines:
    minMaxCounts, letter, password = line.replace(":", "").split(" ")
    minCount, maxCount = map(int, minMaxCounts.split("-"))

    if minCount <= password.count(letter) <= maxCount:
        validCount += 1

    if (password[minCount - 1] == letter) != (password[maxCount - 1] == letter):
        validCount2 += 1

print("Valid count step 1: ", validCount)
print("Valid count step 2: ", validCount2)
