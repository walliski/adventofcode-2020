with open('input.txt', 'r') as content:
    lines = content.readlines()

# Exitcode 1 means that we crashed in a loop
initialState = {
    "curInstruction": 0,
    "acc": 0,
    "opCount": [0] * len(lines),
    "exitCode": 0
}

def run_program(program, state):
    opCount = state["opCount"]
    curInstruction = state["curInstruction"]
    acc = state["acc"]

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

    return {
        "curInstruction": curInstruction,
        "acc": acc,
        "opCount": opCount,
        "exitCode": 1
    }

crash = run_program(lines, initialState)
print("Accumulator value before loop exited: ", crash["acc"])
