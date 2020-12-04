import re

with open('input.txt', 'r') as content:
    data = content.read()

fields = {
    "byr": {
        "required": True
    },
    "iyr": {
        "required": True
    },
    "eyr": {
        "required": True
    },
    "hgt": {
        "required": True
    },
    "hcl": {
        "required": True
    },
    "ecl": {
        "required": True
    },
    "pid": {
        "required": True
    },
    "cid": {
        "required": False
    }
}

infoRe = r'(\s|byr:(?P<byr>\S+)|iyr:(?P<iyr>\S+)|eyr:(?P<eyr>\S+)|hgt:(?P<hgt>\S+)|hcl:(?P<hcl>\S+)|ecl:(?P<ecl>\S+)|pid:(?P<pid>\S+)|cid:(?P<cid>\S+))*?[\r\n]{2}'
validCount = 0

for pMatch in re.finditer(infoRe, data):
    valid = True
    for key, data in fields.items():
        if data["required"] and not pMatch.group(key):
            valid = False
            break

    if valid:
        validCount += 1

print("Step 1 valid passes: ", validCount)