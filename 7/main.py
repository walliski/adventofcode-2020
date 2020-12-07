import re
from typing import NamedTuple

with open('input.txt', 'r') as content:
    lines = content.readlines()

class Bag:
    def __init__(self, name, count, content):
        self.name = name
        self.count = count
        self.content = content

    def carry_count(self, bagName):
        if len(self.content) > 0:
            return sum((b.carry_count(bagName) for b in self.content))

        return 0

    def __repr__(self):
        contentString = ""
        for c in content:
            contentString += str(c.count) + " " + c.name + " "
        return f"{self.name} - {self.count} of each contains: {contentString}"

bags = []

for line in lines:
    content = []
    name, rawContent = line.split(" bags contain ")
    if rawContent.strip() != "no other bags.":
        contentBags = rawContent.replace("bags", "").replace("bag", "").replace(".", "").split(",")
        for contentBag in contentBags:
            contentBag = contentBag.strip()
            count = int(contentBag.split(" ")[0])
            name = " ".join(contentBag.split(" ")[1:])
            content.append(Bag(name=name, count=count, content=[]))

    bags.append(Bag(name=name, count=1, content=content))

for bag in bags:
    if bag.carry_count("shiny gold") > 0:
        print(bag)

print("Count of bags that can contain a 'shiny gold': ", len([b for b in bags if b.carry_count("shiny gold") > 0]))
