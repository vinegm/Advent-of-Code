with open("input.txt") as f:
    data = [list(map(int, line.strip())) for line in f]


def get_best_batteries(batteries: list[int], index: int, bat: int, size: int) -> int:
    if size == 0:
        return bat

    l_high: int = 0
    l_high_index: int = 0
    for j in range(len(batteries) - index - size + 1):
        if batteries[index + j] > l_high:
            l_high = batteries[index + j]
            l_high_index: int = index + j

    best_bat: int = bat * 10 + l_high
    best_bat: int = get_best_batteries(batteries, l_high_index + 1, best_bat, size - 1)

    return best_bat


part1: int = 0
part2: int = 0
for batteries in data:
    part1 += get_best_batteries(batteries, 0, 0, 2)
    part2 += get_best_batteries(batteries, 0, 0, 12)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
