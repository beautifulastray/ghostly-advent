import re

def is_vowels(n):
    count = 0
    for a in ['a', 'e', 'i', 'o', 'u']:
        count += n.count(a)
    if count >= 3:
        return True
    else:
        return False

def is_doubles(n):
    if re.search(r"(.)\1", n) != None:
        return True
    else:
        return False

def is_naughty(n):
    for a in ['ab', 'cd', 'pq', 'xy']:
        if a in n:
            return True
    return False

def is_nice(n):
    return is_vowels(n) and is_doubles(n) and not is_naughty(n)


def main():
    with open('input.txt') as strings:
        nice_string = 0
        for line in strings:
            if is_nice(line):
                nice_string += 1
        print(nice_string)


if __name__ == "__main__":
    main()
    