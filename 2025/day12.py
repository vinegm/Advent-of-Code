with open("input.txt") as f:
    data = f.read().strip().split("\n\n")

presents: list = []
for present_str in data[:-1]:
    space_required: int = 0
    for line in present_str.splitlines():
        for char in line:
            if char == "#":
                space_required += 1

    presents.append(space_required)

requirements: list = []
for line in data[-1].splitlines():
    area, fit_presents = line.split(":")

    area = tuple(int(val) for val in area.split("x"))
    fit_presents = tuple(int(val) for val in fit_presents.split())

    requirements.append((area, fit_presents))

part1: int = 0
part2: int = 0

for area, fit_presents in requirements:
    area_x, area_y = area
    total_area = area_x * area_y

    present_area: int = 0
    for i, req_present in enumerate(fit_presents):
        present_area += presents[i] * req_present

    if present_area <= total_area:
        part1 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
