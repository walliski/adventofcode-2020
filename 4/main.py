import re

with open('input.txt', 'r') as content:
    data = content.read()

fields = {
    "byr": {
        "required": True,
        "validate": (lambda x: isinstance(x, int) or (x.isdigit() and (1920 <= int(x) <= 2002)))
    },
    "iyr": {
        "required": True,
        "validate": (lambda x: isinstance(x, int) or (x.isdigit() and (2010 <= int(x) <= 2020)))
    },
    "eyr": {
        "required": True,
        "validate": (lambda x: isinstance(x, int) or (x.isdigit() and (2020 <= int(x) <= 2030)))
    },
    "hgt": {
        "required": True,
        "validate": (lambda x: check_hgt(x))
    },
    "hcl": {
        "required": True,
        "validate": (lambda x: re.match(r'^#[a-f0-9]{6}$', x))
    },
    "ecl": {
        "required": True,
        "validate": (lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    },
    "pid": {
        "required": True,
        "validate": (lambda x: re.match(r'^[0-9]{9}$', x))
    },
    "cid": {
        "required": False
    }
}

def check_hgt(x):
    heightRe = re.compile(r'(?P<value>\d+)(?P<unit>cm|in)')
    mat = heightRe.match(x)

    if not mat:
        return False

    if mat.group("unit") == "cm" and mat.group("value") and mat.group("value").isdigit() and 150 <= int(mat.group("value")) <= 193:
        return True
    elif mat.group("unit") == "in" and mat.group("value") and mat.group("value").isdigit() and 59 <= int(mat.group("value")) <= 76:
        return True

    return False

infoRe = r'(\s|byr:(?P<byr>\S+)|iyr:(?P<iyr>\S+)|eyr:(?P<eyr>\S+)|hgt:(?P<hgt>\S+)|hcl:(?P<hcl>\S+)|ecl:(?P<ecl>\S+)|pid:(?P<pid>\S+)|cid:(?P<cid>\S+))*?[\r\n]{2}'
validCount1 = 0
validCount2 = 0

for pMatch in re.finditer(infoRe, data):
    valid1 = True
    for key, data in fields.items():
        if data["required"] and not pMatch.group(key):
            valid1 = False
            break

    if valid1:
        validCount1 += 1

    valid2 = True
    for key, data in fields.items():
        print(pMatch.group(key))
        
        if data["required"] and (pMatch.group(key) == None or not data["validate"](pMatch.group(key))):
            valid2 = False
            break

    if valid2:
        validCount2 += 1

print("Step 1 valid passes: ", validCount1)
print("Step 2 valid passes: ", validCount2)