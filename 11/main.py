#! /usr/bin/env python
import pathlib
from collections import Counter, defaultdict
from functools import lru_cache


def get_result(data):
    def update(data):
        new_data = [[None] * len(data[0]) for _ in range(len(data[0]))]
        for row in range(1, len(data) - 1):
            for seat in range(1, len(data[row]) - 1):
                occ = 0
                if seat == ".":
                    new_data[row][seat] = "."
                    continue
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == j == 0:
                            continue
                        if data[row + i][seat + j] == "#":
                            occ += 1
                if data[row][seat] == "L" and occ == 0:
                    new_data[row][seat] = "#"
                elif data[row][seat] == "#" and occ >= 4:
                    new_data[row][seat] = "L"
                else:
                    new_data[row][seat] = data[row][seat]
        return new_data

    for row in range(len(data)):
        data[row] = "." + data[row] + "."
    data.insert(0, "." * len(data[0]))
    data.append("." * len(data[0]))

    while True:
        new_data = update(data)
        if new_data == data:
            break
        data = new_data

    sum_ = 0
    for row in range(1, len(data) - 1):
        for seat in range(1, len(data[row]) - 1):
            if data[row][seat] == "#":
                sum_ += 1
    return sum_


def get_result2(data):
    def update(data):
        new_data = [[None] * len(data[0]) for _ in range(len(data[0]))]
        directions = [
            (i, j) for i in range(-1, 2) for j in range(-1, 2) if not (i == j == 0)
        ]
        for row in range(1, len(data) - 1):
            for seat in range(1, len(data[row]) - 1):
                occ = 0
                if seat == ".":
                    new_data[row][seat] = "."
                    continue

                for direction in directions:
                    i, j = row, seat
                    while 0 < i < len(data) - 1 and 0 < j < len(data[0]) - 1:
                        i, j = (i + direction[0], j + direction[1])
                        if data[i][j] == "L":
                            break
                        elif data[i][j] == "#":
                            occ += 1
                            break

                    if data[row][seat] == "L" and occ == 0:
                        new_data[row][seat] = "#"
                    elif data[row][seat] == "#" and occ >= 5:
                        new_data[row][seat] = "L"
                    else:
                        new_data[row][seat] = data[row][seat]
        return new_data

    for row in range(len(data)):
        data[row] = "." + data[row] + "."
    data.insert(0, "." * len(data[0]))
    data.append("." * len(data[0]))

    while True:
        new_data = update(data)
        if new_data == data:
            break
        data = new_data

    sum_ = 0
    for row in range(1, len(data) - 1):
        for seat in range(1, len(data[row]) - 1):
            if data[row][seat] == "#":
                sum_ += 1
    return sum_


def main():
    data = [line for line in pathlib.Path("input.txt").read_text().split("\n")]
    result = get_result2(data)
    print("done")
    print(result)


if __name__ == "__main__":
    main()
