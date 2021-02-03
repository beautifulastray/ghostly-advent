import re

def is_pairs(n):
    if re.search(r'(\w\w).*\1', n) != None:
        return True
    else:
        return False

def is_middles(n):
    if re.search(r'(\w).\1', n) != None:
        print(n)
        print(re.search(r'(\w).\1', n))
        return True
    else:
        return False

def is_nice(n):
    return is_pairs(n) and is_middles(n)


def main():
    with open('input.txt') as strings:
        nice_string = 0
        for line in strings:
            if is_nice(line):
                nice_string += 1
        print(nice_string)


if __name__ == "__main__":
    main()
    