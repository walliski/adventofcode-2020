from datetime import datetime

with open('input.txt', 'r') as content:
    numbers = content.readlines()
    numbers = list(map(int, numbers))

# One bruteforce solution, and one that is a bit more intelligent...

def calc(numbers):
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if x + y + z == 2020:
                    return x * y * z

def calcOptimized(numbers):
    numbers.sort()

    numCount = len(numbers) - 1

    i = 0
    j = numCount

    for num in numbers:
        while i <= numCount and j >= 0:
            if numbers[i] + numbers[j] + num == 2020:
                return numbers[i] * numbers[j] * num
            if numbers[i] + numbers[j] + num > 2020:
                j -= 1
            else:
                i += 1
        i = 0
        j = numCount


# Runtime for Bruteforce:
# 0:00:13.549834
print("Running bruteforce:")
start=datetime.now()

for i in range(100):
    calc(numbers)

print("Bruteforce time: ", datetime.now() - start)
print("Bruteforce answer: ", calc(numbers))

# Runtime for optimized:
# 0:00:00.001819

print("Running optimized:")
start=datetime.now()

for i in range(100):
    calcOptimized(numbers)

print("Optimized time: ", datetime.now() - start)
print("Optimized answer: ", calcOptimized(numbers))
