#! /usr/bin/env python
import pathlib
from collections import Counter


def get_result(data):
    count = 0
    for group in data:
        count += len(set(group.replace("\n", "")))

    return count


def get_result2(data):
    count = 0
    for group in data:
        counts = Counter(group)
        n_members = counts.pop("\n", 0) + 1
        count += len([x for x, n in counts.items() if n == n_members])
    return count


def main():
    data = [line for line in pathlib.Path("input.txt").read_text().split("\n\n")]
    result = get_result2(data)
    print("done")
    print(result)


if __name__ == "__main__":
    main()
