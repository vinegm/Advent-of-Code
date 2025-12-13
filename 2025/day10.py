from itertools import product


with open("input10.txt") as f:
    lights = []
    buttons = []
    joltages = []
    for line in f.read().splitlines():
        split_line = line.split()

        lights.append(split_line[0])
        buttons.append(split_line[1:-1])
        joltages.append(split_line[-1])


def str_to_tuple(button: str) -> tuple[int]:
    res = []
    for char in button[1:-1].split(","):
        res.append(int(char))

    return tuple(res)


def build_ops_patterns(buttons: list[tuple[int]], n_jolts: int, n_lights: int):
    ops = {}
    patterns = {}
    for pressed in product((0, 1), repeat=len(buttons)):
        jolt = [0] * n_jolts
        lights = [0] * n_lights

        for i, press in enumerate(pressed):
            if press:
                for idx in buttons[i]:
                    if idx < n_jolts:
                        jolt[idx] += 1

                    if idx < n_lights:
                        lights[idx] = not lights[idx]

        lights_tup = tuple(lights)
        if lights_tup not in patterns:
            patterns[lights_tup] = []

        ops[pressed] = tuple(jolt)
        patterns[lights_tup].append(pressed)

    return ops, patterns


def min_presses_jolt(ops: dict, patterns: dict, target: tuple[int]) -> int:
    cache: dict[tuple[int], int] = {}
    visiting: set[tuple[int]] = set()

    def _min(remaining: tuple[int]) -> int:
        if all(r_light == 0 for r_light in remaining):
            return 0

        if remaining in cache:
            return cache[remaining]

        visiting.add(remaining)
        min_presses = float("inf")

        lights_list: list[int] = []
        for x in remaining:
            lights_list.append(x % 2)

        lights = tuple(lights_list)
        for pressed in patterns.get(lights, ()):
            diff = ops[pressed]

            new_target_list: list[int] = []
            for a, b in zip(diff, remaining):
                new_target_list.append((b - a) // 2)

            new_target = tuple(new_target_list)
            if new_target in visiting:
                continue

            candidate = sum(pressed) + 2 * _min(new_target)
            if min_presses > candidate:
                min_presses = candidate

        visiting.remove(remaining)
        cache[remaining] = min_presses
        return min_presses

    return _min(target)


data: list = []
for i in range(len(buttons)):
    new_lights = []
    for char in lights[i][1:-1]:
        if char == "#":
            new_lights.append(1)
        else:
            new_lights.append(0)

    new_lights = tuple(new_lights)
    buttons[i] = [str_to_tuple(b) for b in buttons[i]]
    joltages[i] = str_to_tuple(joltages[i])

    data.append((new_lights, buttons[i], joltages[i]))


part1: int = 0
part2: int = 0

for line in data:
    lights, buttons, joltage_target = line

    n_buttons = len(buttons)
    n_lights = len(lights)
    n_jolts: int = len(joltage_target)

    ops, patterns = build_ops_patterns(buttons, n_jolts, n_lights)

    min_count = float("inf")
    for pressed_buttons in patterns[lights]:
        count = sum(pressed_buttons)
        if count < min_count:
            min_count = count

    part1 += min_count

    part2 += min_presses_jolt(ops, patterns, joltage_target)


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
