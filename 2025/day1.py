with open("input.txt") as f:
    data = f.read().splitlines()

part1 = 0
part2 = 0

dial = 50
for instruction in data:
    side = instruction[0]
    rotations = int(instruction[1:])

    part2 += rotations // 100
    move = rotations % 100

    if side == "L":
        old_dial = dial
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

print(f"Password Part 1: {part1}")
print(f"Password Part 2: {part2}")
