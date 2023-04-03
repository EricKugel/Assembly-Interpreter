acc = 0
locations = {}
labels = {}
lines = []
constants = "-0123456789.="

with open("input.txt", "r") as file:
    lines = [line.strip().split(",") for line in file.readlines()]
for i, line in enumerate(lines):
    if line[0] != "" and line[1] != "DC":
        labels[line[0]] = i

line_number = 0
while line_number < len(lines):
    label, op, loc = lines[line_number]
    val = 0
    if len(loc) > 0 and all([letter in constants for letter in loc]):
        val = int(loc.replace("=", ""))
    elif loc in locations.keys():
        val = locations[loc]

    if op == "LOAD":
        acc = val
    elif op == "STORE":
        locations[loc] = acc
    elif op == "ADD":
        acc += val
    elif op == "SUB":
        acc -= val
    elif op == "MULT":
        acc *= val
    elif op == "DIV":
        acc //= val
    elif op == "BG":
        if acc > 0:
            line_number = labels[loc] - 1
    elif op == "BL":
        if acc < 0:
            line_number = labels[loc] - 1
    elif op == "BE":
        if acc == 0:
            line_number = labels[loc] - 1
    elif op == "BU":
        line_number = labels[loc] - 1
    elif op == "READ":
        locations[loc] = int(input())
    elif op == "PRINT":
        print(val)
    elif op == "DC":
        locations[label] = val
    elif op == "END":
        break
    line_number += 1
    
print("ACC: " + str(acc))
print("--------------------")
print()
print("\n".join([str(loc) + " => " + str(value) for (loc, value) in locations.items()]))