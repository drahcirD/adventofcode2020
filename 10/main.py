#! /usr/bin/env python
import pathlib
from collections import Counter, defaultdict
from functools import lru_cache

def get_result(data):
    data = sorted([int(x) for x in data])
    last = 0
    diffs = Counter({1:0, 3:1})
    for jolt in data:
        diffs[jolt - last] += 1
        last = jolt
    print(diffs)
    return diffs[1] * diffs[3]


    

def get_result2(data):
    data = [0]+ sorted([int(x) for x in data])
    paths = defaultdict(int)
    paths[0] = 1

    for adapter in data:
        for diff in range(1, 4):
            next_adapter = adapter + diff
            if next_adapter in data:
                paths[next_adapter] += paths[adapter]
    return paths[max(data)]

    


def main():
    data = [line for line in pathlib.Path("input.txt").read_text().split("\n")]
    result = get_result2(data)
    print("done")
    print(result)


if __name__ == "__main__":
    main()
