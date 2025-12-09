import math

with open("input.txt") as f:
    data = []
    for line in f.read().splitlines():
        coords = line.split(",")
        data.append([int(num) for num in coords])


def distance_from_each(data: list) -> list:
    already_seen: set = set()
    distances: list = []
    for coord in data:
        already_seen.add(tuple(coord))
        for other in data:
            if tuple(other) in already_seen:
                continue

            distance = math.dist(coord, other)
            distances.append((distance, tuple(coord), tuple(other)))

    distances.sort()
    return distances


def connect_circuits(
    circuits: list[set], coord_i: tuple, coord_j: tuple, i_set: set, j_set: set
) -> None:
    if i_set is not None and j_set is not None:
        if i_set == j_set:
            return

        j_circuit = j_set
        i_set.update(j_circuit)

        circuits.remove(j_circuit)
        return

    if i_set is not None:
        i_set.add(coord_j)
        return

    if j_set is not None:
        j_set.add(coord_i)
        return

    circuits.append({coord_i, coord_j})


def solve_part1(circuits: list[set]) -> int:
    result: int = 1

    sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    for i in range(3):
        result *= len(sorted_circuits[i])

    return result


part1: int = 1
part2: int = 0

# Depends on input data, change n_connections to 10 if using the example
part1_n_connections: int = 1000
part1_done: bool = False

dist_pair: list = distance_from_each(data)

last_connection: tuple = ()
circuits: list[set] = [{tuple(coord)} for coord in data]
for i in range(len(dist_pair)):
    _, coord_i, coord_j = dist_pair[i]

    if i >= part1_n_connections and not part1_done:
        part1 = solve_part1(circuits)
        part1_done = True

    i_set: set = None
    j_set: set = None
    for circuit in circuits:
        if coord_i in circuit:
            i_set = circuit

        if coord_j in circuit:
            j_set = circuit

        if i_set is not None and j_set is not None:
            break

    connect_circuits(circuits, coord_i, coord_j, i_set, j_set)

    if len(circuits) == 1:
        last_connection = (coord_i, coord_j)
        break

i_coord, j_coord = last_connection
part2 = i_coord[0] * j_coord[0]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
