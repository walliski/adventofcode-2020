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
        curInstruction += 1
    elif op == "jmp":
        curInstruction += int(arg)
    elif op == "nop":
        curInstruction += 1

print("Accumulator value before loop exited: ", acc)
