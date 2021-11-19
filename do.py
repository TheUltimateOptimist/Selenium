s = "["
with open("gescrapteWitze/1. witze-info.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if i > 2:
            category = line.split(": ")[0]
            number = line.split(": ")[1].split("\n")[0]
            s += f"['{category}', {number}], "
s += "]"
print(s)
