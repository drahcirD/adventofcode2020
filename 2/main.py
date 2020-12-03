#! /usr/bin/env python
import pathlib
from collections import Counter
def get_result(data):
    count = 0
    for line in data:
        rule, letter, password = line.split()
        letter = letter[0]
        mini, maxi = [int(x) for x in rule.split("-")]
        cnt = Counter(password)
        if mini <= cnt[letter] <= maxi:
            count += 1
        
    return count

def get_result2(data):
    count = 0
    for line in data:
        rule, letter, password = line.split()
        letter = letter[0]
        pos1, pos2 = [int(x)-1 for x in rule.split("-")]
        if (password[pos1] == letter) ^ (password[pos2] == letter):
            count+=1
        
    return count
    
def main():
    data = [line for line in pathlib.Path("input.txt").read_text().split("\n")]
    result = get_result2(data)
    print("done")
    print(result)

if __name__ == "__main__":
    main()
    