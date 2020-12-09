with open('input.txt', 'r') as content:
    lines = list(map(int, content.readlines()))

def is_valid(pre, preCount, target):
    print(pre)
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

preCount = 25
maxCount = len(lines)

for i in range(preCount, maxCount):
    if not is_valid(lines[i-preCount:i], preCount, lines[i]):
        print("Broken: ", lines[i], "on index", i)
        break
