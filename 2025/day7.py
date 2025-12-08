with open("input.txt") as f:
    data = []
    for i, line in enumerate(f.read().splitlines()):
        if i % 2 != 0:
            continue

        data.append(line)

part1: int = 0
part2: int = 0

first_ray: int = data[0].index("S")
rays: set[int] = {first_ray}
unique_rays: dict[int, int] = {first_ray: 1}
for line in data[1:]:
    new_rays: set[int] = set()
    for ray in rays:
        if line[ray] != "^":
            new_rays.add(ray)
            continue

        for offset in [-1, 1]:
            new_rays.add(ray + offset)
            if ray + offset not in unique_rays:
                unique_rays[ray + offset] = 0

            unique_rays[ray + offset] += unique_rays[ray]

        unique_rays[ray] = 0
        part1 += 1

    rays = new_rays

for count in unique_rays.values():
    part2 += count

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
