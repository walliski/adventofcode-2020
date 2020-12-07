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

def carry_count(bagInfo, target_name, bag_name):
    if target_name == bag_name:
        return 1

    if len(bagInfo[bag_name]) > 0:
        return sum([carry_count(bagInfo, target_name, bag) for bag in bagInfo[bag_name]])

    return 0

print(len([bag for bag in bagInfo.keys() if carry_count(bagInfo, "shiny gold", bag) > 0 and bag != "shiny gold"]))