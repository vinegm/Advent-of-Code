with open("input.txt") as f:
    data = f.read().strip()


def parse_range(range_str: str) -> tuple[int, int]:
    low, high = map(int, range_str.split("-"))
    return low, high


def compress_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges.sort(key=lambda x: x[0])

    merged = []
    cur_low, cur_high = ranges[0]

    for i in range(1, len(ranges)):
        low, high = ranges[i]
        if low <= cur_high + 1:
            cur_high = max(cur_high, high)
            continue

        merged.append((cur_low, cur_high))
        cur_low, cur_high = low, high

    merged.append((cur_low, cur_high))
    return merged


ranges, values = data.split("\n\n")
ranges = ranges.splitlines()
for i, val_range in enumerate(ranges):
    val_range = parse_range(val_range)
    ranges[i] = val_range

ranges = compress_ranges(ranges)

part1: int = 0
for value in map(int, values.splitlines()):
    for val_range in ranges:
        low, high = val_range
        if low <= value <= high:
            part1 += 1
            break

part2: int = 0
for val_range in ranges:
    low, high = val_range
    part2 += high - low + 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
