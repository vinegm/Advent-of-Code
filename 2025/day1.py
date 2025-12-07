with open("input.txt") as f:
    data = f.read().splitlines()

part1: int = 0
part2: int = 0

dial: int = 50
for instruction in data:
    side: str = instruction[0]
    rotations: int = int(instruction[1:])

    part2 += rotations // 100
    move: int = rotations % 100

    if side == "L":
        old_dial: int = dial
        dial -= move

        if old_dial != 0 and dial <= 0:
            part2 += 1
    else:
        dial += move
        if dial >= 100:
            part2 += 1

    dial %= 100

    if dial == 0:
        part1 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
