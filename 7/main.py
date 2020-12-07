import re

with open('input.txt', 'r') as content:
    lines = content.readlines()

bagInfo = {}
for line in lines:
    nameMatch = re.match(r'^(?P<name>\S+ \S+) bags', line)
    name = nameMatch.group("name")

    contains = {}
    containsIter = re.finditer(r'(?P<count>\d+) (?P<name>\S+ \S+) bags?[.,]', line)
    for i in containsIter:
        contains[i.group("name")] = int(i.group("count"))

    bagInfo[name] = contains
