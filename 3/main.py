#! /usr/bin/env python
import pathlib
from functools import reduce
def get_result(data):
    x, y = 0,0
    trees = 0
    width = len(data[0])
    while y < len(data):
        if data[y][x % width] == "#":
            trees += 1
        x+=3
        y+=1
        
    return trees

def get_result2(data):

    def calc(data, x_speed, y_speed):
        x, y = 0,0
        trees = 0
        width = len(data[0])
        while y < len(data):
            if data[y][x % width] == "#":
                trees += 1
            x+=x_speed
            y+=y_speed
        return trees
    
    inputs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = [calc(data, *input_) for input_ in inputs]
    return reduce(lambda x, y: x * y, results)
    
def main():
    data = [line for line in pathlib.Path("input.txt").read_text().split("\n")]
    result = get_result2(data)
    print("done")
    print(result)

if __name__ == "__main__":
    main()
    