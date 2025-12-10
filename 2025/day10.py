from itertools import combinations
from collections import deque


with open("example.txt") as f:
    light_target = []
    buttons = []
    joltage = []
    for line in f.read().splitlines():
        split_line = line.split()

        light_target.append(split_line[0])
        buttons.append(split_line[1:-1])
        joltage.append(split_line[-1])


def parse_light(light_target: str) -> list[bool]:
    res = []
    for char in light_target[1:-1]:
        if char == "#":
            res.append(True)
        else:
            res.append(False)

    return tuple(res)


def str_to_tuple(button: str) -> tuple[int]:
    res = []
    for char in button[1:-1].split(","):
        res.append(int(char))

    return tuple(res)


def press_light(cur_jolt: list[bool], button: tuple[int]) -> list[bool]:
    new = cur_jolt.copy()
    for idx in button:
        new[idx] = not new[idx]

    return new


def press_jolt(cur_jolt: tuple[int], button: tuple[int]) -> tuple[int]:
    new = list(cur_jolt)
    for idx in button:
        new[idx] += 1

    return tuple(new)


part1: int = 0
part2: int = 0

data: list = []
for i in range(len(buttons)):
    light_target[i] = parse_light(light_target[i])
    buttons[i] = [str_to_tuple(b) for b in buttons[i]]
    joltage[i] = str_to_tuple(joltage[i])

    data.append((light_target[i], buttons[i], joltage[i]))

n_lines = len(data)
for line in data:

    light_target, buttons, joltage_target = line

    n_buttons = len(buttons)
    n_lights = len(light_target)
    n_jolts: int = len(joltage_target)

    found: bool = False
    for light_presses in range(n_buttons + 1):
        for combination in combinations(range(n_buttons), light_presses):
            cur = [False] * n_lights
            for idx in combination:
                cur = press_light(cur, buttons[idx])

            if tuple(cur) == light_target:
                found = True
                break

        if found:
            break

    part1 += light_presses

    start: tuple = tuple([0] * n_jolts)
    buffer = deque([start])
    already_seen: set = {start}

    found: bool = False
    while buffer and not found:
        part2 += 1
        for _ in range(len(buffer)):
            cur_jolt = buffer.popleft()
            for button in buttons:
                new = press_jolt(cur_jolt, button)
                if new == joltage_target:
                    found = True
                    break

                if any(new[j] > joltage_target[j] for j in range(n_jolts)):
                    continue

                if new not in already_seen:
                    already_seen.add(new)
                    buffer.append(new)

            if found:
                break


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
