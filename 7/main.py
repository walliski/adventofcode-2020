import re

with open('input.txt', 'r') as content:
    lines = content.readlines()

# Bag info:
# {
#     "bag name": {
#         "bag name1": 1,
#         "bag name2": 2
#     }
# }

bagInfo = {}
nameRe = re.compile(r'^(?P<name>\S+ \S+) bags')
containsRe = re.compile(r'(?P<count>\d+) (?P<name>\S+ \S+) bags?[.,]')
for line in lines:
    name = nameRe.match(line).group("name")

    contains = {}
    containsIter = containsRe.finditer(line)
    for i in containsIter:
        contains[i.group("name")] = int(i.group("count"))

    bagInfo[name] = contains

def carry_count(bagInfo, target_name, bag_name):
    if target_name == bag_name:
        return 1

    if len(bagInfo[bag_name]) > 0:
        return sum([carry_count(bagInfo, target_name, bag) for bag in bagInfo[bag_name]])

    return 0

def bag_count_inside(bagInfo, target_name, level=0):
    if len(bagInfo[target_name]) == 0:
        return 1

    count = 0
    for bag, contentCount in bagInfo[target_name].items():
        count += bag_count_inside(bagInfo, bag, level + 1) * contentCount

    # We add one unless we are at the top level, to count the bags themselves.
    if level != 0:
        count += 1

    return count

print("Shiny gold is in this many cases:", len([bag for bag in bagInfo.keys() if carry_count(bagInfo, "shiny gold", bag) > 0 and bag != "shiny gold"]))
print("And a shiny gold contains this many bags:", bag_count_inside(bagInfo, "shiny gold"))