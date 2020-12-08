#! /usr/bin/env python
import pathlib
import re
import copy

def get_result(data):
    acc = 0
    data = [x.split() for x in data]
    cur = 0
    visited = set()
    while cur not in visited:
        visited.add(cur)
        instr = data[cur][0]
        sign = 1 if data[cur][1][0] == '+' else -1
        value = sign*int(data[cur][1][1:])
        if instr == 'acc':
            acc += value
            cur += 1
        elif instr == 'jmp':
            cur += value
        elif instr == 'nop':
            cur += 1
    
    return acc


class InfiniteLoopError(Exception):
    pass

def get_result2(data):
    def try_replace(data, i):
        acc = 0
        cur = 0
        visited = set()
        data = copy.deepcopy(data)
        data[i][0] = 'nop' if data[i][0] == 'jmp' else 'jmp'
        while cur not in visited:
            visited.add(cur)
            instr = data[cur][0]
            sign = 1 if data[cur][1][0] == '+' else -1
            value = sign*int(data[cur][1][1:])
            if instr == 'acc':
                acc += value
                cur += 1
            elif instr == 'jmp':
                cur += value
            elif instr == 'nop':
                cur += 1
            if cur >= len(data):
                return acc
        
        raise InfiniteLoopError

    data = [x.split() for x in data]
    nops = [i for i,x in enumerate(data) if x[0] == 'nop']
    jmps = [i for i,x in enumerate(data) if x[0] == 'jmp']
    for nop in nops:
        try:
            return try_replace(data, nop)
        except InfiniteLoopError:
            pass

    for jmp in jmps:
        try:
            return try_replace(data, jmp)
        except InfiniteLoopError:
            pass
    
    raise Exception('No answer found')

def main():
    data = [line for line in pathlib.Path("input.txt").read_text().split("\n")]
    result = get_result2(data)
    print("done")
    print(result)


if __name__ == "__main__":
    main()
