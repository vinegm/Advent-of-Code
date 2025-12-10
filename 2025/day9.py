with open("input.txt") as f:
    data = []
    for line in f.read().splitlines():
        coords = line.strip()
        coords = list(map(int, coords.split(",")))
        data.append(coords)


def get_inside_point(grid: list[list[str]]) -> tuple[int, int]:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != ".":
                continue

            on_border = False
            borders_crossed = 0
            for i in range(x, -1, -1):
                # continuous borders
                if grid[y][i] != "#" or on_border:
                    on_border = False
                    continue

                borders_crossed += 1
                on_border = True

            if borders_crossed % 2 == 1:
                return (x, y)

    raise ValueError("No inside point found")


def flood_fill(grid: list[list[str]], start: tuple[int, int]) -> None:
    n_rows = len(grid)
    n_cols = len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    buffer = [start]
    while buffer:
        x, y = buffer.pop()
        if grid[y][x] != ".":
            continue

        grid[y][x] = "#"

        for dx, dy in dirs:
            nx = x + dx
            if nx < 0 or nx >= n_cols:
                continue

            ny = y + dy
            if ny < 0 or ny >= n_rows:
                continue

            if grid[ny][nx] == ".":
                buffer.append((nx, ny))


def connect_points(
    grid: list[list[str]], low: int, high: int, fixed: int, vertical=True
) -> None:
    for y in range(low, high + 1):
        if vertical:
            grid[y][fixed] = "#"
        else:
            grid[fixed][y] = "#"


def mark_green_tiles(grid: list[list[str]]) -> None:
    compressed_coords = []
    # mark coordinates
    for x, y in data:
        comp_x, comp_y = x_map[x], y_map[y]
        compressed_coords.append((comp_x, comp_y))
        grid[comp_y][comp_x] = "#"

    # mark connections
    n_compressed = len(compressed_coords)
    for i in range(n_compressed):
        ax, ay = compressed_coords[i]
        bx, by = compressed_coords[(i + 1) % n_compressed]

        if ax == bx:
            low_y, high_y = sorted([ay, by])
            connect_points(grid, low_y, high_y, ax, vertical=True)
            continue

        if ay == by:
            low_x, high_x = sorted([ax, bx])
            connect_points(grid, low_x, high_x, ay, vertical=False)
            continue

    inside_point = get_inside_point(grid)
    flood_fill(grid, inside_point)


def is_enclosed(p1, p2, grid, x_map, y_map):
    p1x, p1y = p1
    p2x, p2y = p2

    p1x, p1y = x_map[p1x], y_map[p1y]
    p2x, p2y = x_map[p2x], y_map[p2y]

    low_x, high_x = sorted([p1x, p2x])
    low_y, high_y = sorted([p1y, p2y])

    for x in range(low_x, high_x + 1):
        if grid[low_y][x] != "#" or grid[high_y][x] != "#":
            return False

    for y in range(low_y, high_y + 1):
        if grid[y][low_x] != "#" or grid[y][high_x] != "#":
            return False

    return True


# I had no idea how to implement part 2 due to
# performance issues with large coordinates.
# credits for this comment for the tips/hints:
# https://www.reddit.com/r/adventofcode/comments/1pichj2/comment/nt5guy3/
# https://github.com/sleekmountaincat/aoc2025/blob/main/src/day9/q2.ts
xs: list = []
ys: list = []
for coord in data:
    x, y = coord

    xs.append(x)
    ys.append(y)

uniq_xs = sorted(set(xs))
uniq_ys = sorted(set(ys))

# compressed coordinate mapping
x_map: dict = {x: i for i, x in enumerate(uniq_xs)}
y_map: dict = {y: i for i, y in enumerate(uniq_ys)}

grid: list[list[str]] = []
for _ in range(len(uniq_ys)):
    grid.append(["."] * len(uniq_xs))

mark_green_tiles(grid)

part2: int = 0
part1: int = 0

already_checked: set = set()
for i_coord in data:
    ix, iy = i_coord

    already_checked.add((ix, iy))
    for j_coord in data:
        jx, jy = j_coord
        if (jx, jy) in already_checked:
            continue

        dist_x: int = abs(ix - jx) + 1
        dist_y: int = abs(iy - jy) + 1

        area = dist_x * dist_y
        if area > part1:
            part1 = area

        if not is_enclosed(i_coord, j_coord, grid, x_map, y_map):
            continue

        if area > part2:
            part2 = area


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
