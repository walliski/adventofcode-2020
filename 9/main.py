with open('input.txt', 'r') as content:
    lines = list(map(int, content.readlines()))

def is_valid(pre, preCount, target):
    pre.sort()
    leftPointer = 0
    rightPointer = len(pre) - 1

    while leftPointer != rightPointer:
        if pre[leftPointer] + pre[rightPointer] == target:
            return True

        if pre[leftPointer] + pre[rightPointer] > target:
            rightPointer -= 1
        else:
            leftPointer += 1

    return False

# Calculate first part
preCount = 25
maxCount = len(lines)
broken = 0

for i in range(preCount, maxCount):
    if not is_valid(lines[i-preCount:i], preCount, lines[i]):
        broken = lines[i]
        print("Broken: ", broken, "on index", i)
        break

# Calculate second part
for i in range(maxCount-1):
    sumValue = lines[i]
    minValue = lines[i]
    maxValue = 0

    j = i+1
    while sumValue < broken and j < maxCount:
        sumValue += lines[j]
        minValue = min(minValue, lines[j])
        maxValue = max(maxValue, lines[j])
        j += 1

    if sumValue == broken:
        print("Min number: ", minValue, "Max value:", maxValue, "sum:", minValue + maxValue)
        break
