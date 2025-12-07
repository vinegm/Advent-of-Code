with open("input.txt") as f:
    data = f.read().split(",")

part1: int = 0
part2: int = 0

# Part 1
for val_range in data:
    low, high = map(int, val_range.split("-"))
    for val in range(low, high + 1):
        val_str: str = str(val)

        val_len: int = len(val_str)
        if val_len % 2 == 1:
            continue

        middle_index: int = val_len // 2
        for i in range(middle_index):
            if val_str[i] != val_str[middle_index + i]:
                break

            if i == middle_index - 1:
                part1 += val
                break

# Part 2
for val_range in data:
    low, high = map(int, val_range.split("-"))
    for val in range(low, high + 1):
        val_str: str = str(val)
        val_len: int = len(val_str)

        found = False
        for chunk_size in range(1, val_len):
            if val_len % chunk_size != 0:
                continue

            num_repetitions = val_len // chunk_size
            if num_repetitions < 2:
                continue

            pattern = val_str[:chunk_size]
            if pattern * num_repetitions == val_str:
                found = True
                part2 += val
                break

        if found:
            continue

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
