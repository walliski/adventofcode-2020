with open('input.txt', 'r') as content:
    lines = content.readlines()

def run_program(program):
    opCount = [0] * len(program)
    curInstruction = 0
    acc = 0

    while (curInstruction < len(program) and opCount[curInstruction] < 1):
        op, arg = program[curInstruction].strip().split(" ")

        opCount[curInstruction] += 1

        if op == "acc":
            acc += int(arg)
            curInstruction += 1
        elif op == "jmp":
            curInstruction += int(arg)
        elif op == "nop":
            curInstruction += 1

    exitCode = 1

    if curInstruction >= len(program):
        exitCode = 0

    return {
        "acc": acc,
        "exitCode": exitCode
    }

crash = run_program(lines)
print("Accumulator value before loop exited: ", crash["acc"])

for i in range(len(lines)):
    op, arg = lines[i].strip().split(" ")

    if op == "acc":
        continue

    newOp = ""
    if op == "jmp":
        newOp = "nop"
    elif op == "nop":
        newOp = "jmp"

    fixed = lines.copy()
    fixed[i] = fixed[i].replace(op, newOp)

    result = run_program(fixed)
    if result["exitCode"] == 0:
        print("Acc value on successful run?", result["acc"])
        break
