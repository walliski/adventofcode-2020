from datetime import datetime

with open('input.txt', 'r') as content:
    numbers = content.readlines()
    numbers = list(map(int, numbers))

# A more optimal solution is to sort the list of numbers, and after that take a look at the numbers from left side
# and right side, and see if those summed are the magic number. A lot more effective than the brute force solution.
# Works also with three numbers, just loop over all numbers as the third number, and then do the check from left and
# right for the two other ones.

def calc(numbers):
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if x + y + z == 2020:
                    print(x * y * z)
                    return

# Calculate runtime. ~0.1 second per run for the 10 runs.
start=datetime.now()

for i in range(10):
    calc(numbers)

print(datetime.now() - start)
