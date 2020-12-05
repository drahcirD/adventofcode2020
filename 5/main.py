#! /usr/bin/env python
import pathlib
import re
from dataclasses import dataclass
import typing


@dataclass(frozen=True)
class BoardingCard:
    partition: str

    @property
    def row(self) -> int:
        low, high = 0, 127
        for c in self.partition[:7]:
            mid = (high + low) // 2
            if c == "F":
                high = mid
            elif c == "B":
                low = mid + 1
        return mid if c == "F" else mid + 1

    @property
    def col(self) -> int:
        low, high = 0, 7
        for c in self.partition[7:]:
            mid = (high + low) // 2
            if c == "L":
                high = mid
            elif c == "R":
                low = mid + 1
        return mid if c == "L" else mid + 1

    @property
    def id(self) -> int:
        return self.row * 8 + self.col


def get_result(data):
    high = float("-inf")
    for card in data:
        seat_id = BoardingCard(card).id
        if seat_id > high:
            high = seat_id

    return high


def get_result2(data):
    seats = [False for row in range(128) for col in range(8)]
    for card in data:
        seats[BoardingCard(card).id] = True

    for seat_id, seat in enumerate(seats):
        if not seat and seats[seat_id - 1] and seats[seat_id + 1]:
            return seat_id


def main():
    data = [line for line in pathlib.Path("input.txt").read_text().split("\n")]
    result = get_result2(data)
    print("done")
    print(result)


if __name__ == "__main__":
    main()
