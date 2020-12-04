#! /usr/bin/env python
import pathlib
import re

def get_result(data):
    count = 0
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    for passport in data:
        present_fields = {key.split(":")[0] for key in passport.split()}
        missing_fields = required_fields - present_fields
        if len(missing_fields) == 0 or (len(missing_fields) == 1 and 'cid' in missing_fields):
            count += 1
    return count


def get_result2(data):
    count = 0
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    _validators = {
        'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
        'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
        'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
        'hgt': lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
        'hcl': lambda x: re.match(r"^#[0-9a-f]{6}$", x),
        'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda x: re.match(r"^[0-9]{9}$", x),
        'cid': lambda x: True
    }
    for passport in data:
        present_fields = {key: val for key,val in [pair.split(":") for pair in passport.split()]}
        missing_fields = required_fields - set(present_fields.keys())
        if not (len(missing_fields) == 0 or (len(missing_fields) == 1 and 'cid' in missing_fields)):
            continue
            
        for key, value in present_fields.items():
            if not _validators[key](value):
                break
        else:
            print(passport)
            print('='*30)
            count += 1
    return count

def main():
    data = [line for line in pathlib.Path("input.txt").read_text().split("\n\n")]
    result = get_result2(data)
    print("done")
    print(result)

if __name__ == "__main__":
    main()
    