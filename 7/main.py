#! /usr/bin/env python
import pathlib
import re
from collections import defaultdict

def parse_rules(data):
    rules = {}
    for line in data:
        bag = re.match(r"([a-z]+ [a-z]+)(?= bags contain)", line).group()
        match = re.findall(r"(?<=contain )([0-9]+) ([a-z]+ [a-z]+)", line)
        if match:
            contains = match
            match = re.findall(r"(?<=, )([0-9]+) ([a-z]+ [a-z]+)", line)
            contains.extend([x for x in match])
            rules[bag] = contains
    return rules



def get_result(data):
    def search_bag(rules, key):
        res = False
        for bag in rules.get(key, []):
            if bag[1] == 'shiny gold':
                return True
            res |= search_bag(rules, bag[1])
            if res:
                return True
            
        return False

    rules = parse_rules(data)
    count = 0
    for key in rules:
        count += search_bag(rules, key)
    return count


def get_result2(data):
    def search_bag(rules, key):
        count = 0
        bags = rules.get(key, [])
        for bag in bags:
            count += int(bag[0]) * (1 + search_bag(rules, bag[1]))
        return count
    
    rules = parse_rules(data)
    return search_bag(rules, 'shiny gold')

def main():
    data = [line for line in pathlib.Path("input.txt").read_text().split("\n")]
    result = get_result2(data)
    print("done")
    print(result)


if __name__ == "__main__":
    main()
