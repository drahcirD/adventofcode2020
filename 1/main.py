#! /usr/bin/env python
import pathlib
def get_result(data):
    for i, nbr in enumerate(data):
        for nbr2 in data:
            if nbr + nbr2 == 2020:
                return nbr*nbr2
    return False

def get_result2(data):
    for i, nbr in enumerate(data):
        for nbr2 in data:
            for nbr3 in data:
                if nbr + nbr2 + nbr3== 2020:
                    return nbr*nbr2*nbr3
    return False
    
def main():
    data = [int(x) for x in pathlib.Path("input.txt").read_text().split()]
    result = get_result2(data)
    print("done")
    print(result)

if __name__ == "__main__":
    main()
    