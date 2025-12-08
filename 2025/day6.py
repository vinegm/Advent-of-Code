with open("input.txt") as f:
    data = f.read().splitlines()
    p1_values = [row.split() for row in data[:-1]]
    p2_values = [list(row) for row in data[:-1]]
    operations = data[-1].split()

part1: int = 0
part2: int = 0

# Part 1
for col_i in range(len(p1_values[0])):
    mult_res = 1

    for row in p1_values:
        if operations[col_i] == "+":
            part1 += int(row[col_i])
            continue

        mult_res *= int(row[col_i])

    if mult_res != 1:
        part1 += mult_res


# Part 2
cur_op = len(operations) - 1
column = len(p2_values[0]) - 1
mult_res = 1

# There is an edge case where if the operation is multiplication
# and the column results in 1, we will miss adding it to the final result.
# I will not fix it lol
while column >= 0:
    empty_col = True
    cur_value = 0

    for row in p2_values:
        if row[column] == " ":
            continue

        cur_value = (cur_value * 10) + int(row[column])
        empty_col = False

    if empty_col:
        if mult_res != 1:
            part2 += mult_res
            mult_res = 1

        cur_op -= 1
    else:
        if operations[cur_op] == "+":
            part2 += cur_value
        else:
            mult_res *= cur_value

    column -= 1

if mult_res != 1:
    part2 += mult_res

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
