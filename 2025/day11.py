with open("input.txt") as f:
    machines = {}
    for line in f.read().splitlines():
        machine, outputs = line.split(":")
        machines[machine] = tuple(outputs.split())


def count_paths(graph: dict, start: str, target: str) -> int:
    cache: dict[str, int] = {}
    visiting: set[str] = set()

    def _count(node: str) -> int:
        if node == target:
            return 1

        if node in cache:
            return cache[node]

        visiting.add(node)
        total = 0
        for nxt in graph.get(node, ()):
            total += _count(nxt)

        visiting.remove(node)
        cache[node] = total

        return total

    return _count(start)


part1: int = 0
part2: int = 0

if "you" in machines:
    part1 = count_paths(machines, "you", "out")

if "svr" in machines:
    paths_dac_out = count_paths(machines, "dac", "out")
    paths_fft_dac = count_paths(machines, "fft", "dac")
    paths_svr_fft = count_paths(machines, "svr", "fft")

    part2 = paths_fft_dac * paths_svr_fft * paths_dac_out

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
