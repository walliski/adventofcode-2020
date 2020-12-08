with open('input.txt', 'r') as content:
    lines = content.readlines()

opCount = [0] * len(lines)
curInstruction = 0
acc = 0

while (opCount[curInstruction] < 1):
    op, arg = lines[curInstruction].strip().split(" ")

    opCount[curInstruction] += 1

    if op == "acc":
        acc += int(arg)
    elif op == "jmp":
        curInstruction += int(arg)
        continue

    curInstruction += 1

print("Accumulator value before loop exited: ", acc)
