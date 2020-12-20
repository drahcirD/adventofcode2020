#! /usr/bin/env python
import pathlib
from math import cos, sin, radians

def get_result(data):
    x, y = 0, 0
    _translation = {
        0: 'E',
        90: 'S',
        180: 'W',
        270: 'N'
    }
    cur = 'E'
    deg = 0
    for move in data:
        d = move[0]
        l = int(move[1:])
        if d == 'F':
            d = cur

        if d == 'N':
            y += l
        elif d == 'E':
            x += l
        elif d == 'S':
            y -= l
        elif d == 'W':
            x -= l
        elif d == 'R':
            deg += l
            cur = _translation[abs(deg % 360)]
        elif d == 'L':
            deg -= l
            cur = _translation[abs(deg % 360)]

    return abs(x) + abs(y)



def get_result2(data):
    x, y = 0, 0
    def translate(way, deg):
        x,y = way
        deg = radians(deg)
        return [x*cos(deg) - y*sin(deg), x*sin(deg) + y*cos(deg)]
    way = [10,1]
    for move in data:
        d = move[0]
        l = int(move[1:])
        if d == 'F':
            x += l*way[0]
            y += l*way[1]
        elif d == 'N':
            way[1] += l
        elif d == 'E':
            way[0] += l
        elif d == 'S':
            way[1] -= l
        elif d == 'W':
            way[0] -= l
        elif d == 'R':
            way = translate(way, 360 - l % 360)
        elif d == 'L':
            way = translate(way, l % 360)

    return abs(x) + abs(y)


def main():
    data = [line for line in pathlib.Path("input.txt").read_text().split("\n")]
    result = get_result2(data)
    print("done")
    print(result)


if __name__ == "__main__":
    main()
