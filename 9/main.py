#! /usr/bin/env python
import pathlib
from collections import deque


def get_result(data, preamble=25):
    def get_additions(data):
        add = deque()
        for i, nbr in enumerate(data[:-1]):
            for nbr2 in data[i+1:]:
                add.append(nbr + nbr2)
        return add
    data = [int(x) for x in data]
    nbrs = deque(data[:preamble], maxlen=preamble)
    valid_numbers = get_additions(list(nbrs))
    data = data[preamble:]
    for i, nbr in enumerate(data):
        if nbr not in valid_numbers:
            return nbr
        nbrs.append(nbr)
        valid_numbers = get_additions(list(nbrs))

    raise Exception('no answer')

def get_result2(data, find=1309761972):
    data = [int(x) for x in data]
    data = data[:data.index(find)]
    length = 2
    while length < 100:
        start = 0
        while start+length-1 < len(data):
            subset = data[start:start+length-1]
            total = sum(subset)
            if total == find:
                return min(subset) + max(subset)
            start+=1
        length +=1

    raise Exception('No answer')

def main():
    data = [line for line in pathlib.Path("input.txt").read_text().split("\n")]
    result = get_result2(data)
    print("done")
    print(result)


if __name__ == "__main__":
    main()
