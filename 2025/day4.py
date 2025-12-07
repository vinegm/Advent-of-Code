with open("input.txt") as f:
    data = f.read().splitlines()
    data = [list(line) for line in data]


def get_removable_rolls(data: list[list[str]]) -> int:
    res: int = 0

    n_row: int = len(data)
    n_col: int = len(data[0])

    remove_list: list[tuple[int, int]] = []
    for i in range(n_row):
        for j in range(n_col):
            if data[i][j] == ".":
                continue

            n_neighbors: int = 0
            for di in dirs:
                for dj in dirs:
                    tdi = i + di
                    if tdi < 0 or tdi >= n_row:
                        continue

                    tdj = j + dj
                    if tdj < 0 or tdj >= n_col:
                        continue

                    if data[tdi][tdj] == "@":
                        n_neighbors += 1

            # The roll counts itself as a neighbor
            if n_neighbors < 5:
                remove_list.append((i, j))
                res += 1

    for i, j in remove_list:
        data[i][j] = "."

    return res


dirs: list = [-1, 0, 1]
part1: int = 0
part2: int = 0

n_removed_rolls: int = get_removable_rolls(data)
part1 = n_removed_rolls
part2 = n_removed_rolls

while n_removed_rolls != 0:
    n_removed_rolls = get_removable_rolls(data)
    part2 += n_removed_rolls

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
