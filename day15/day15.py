from collections import namedtuple

def read_input(file_path: str) -> list:
    import os
    import sys
    with open(os.path.join(sys.path[0], file_path), "r") as f:
        return f.read().split(",")

Number = namedtuple('Number', ['last', 'prev'])

def get_number(seq, stop):
    count = {}
    number = -1
    i = 1
    for n in seq: # starting numbers
        number = n
        last, _ = count.get(number, Number(0,0))
        count[number] = Number(i, last)
        i += 1
    for m in range(i, stop + 1): # rest
        last, prev = count.get(number, Number(0,0))
        if prev:
            number = last - prev
            last, prev = count.get(number, Number(0,0))
            count[number] = Number(m, last)
        else:
            number = 0
            last, _ = count.get(number, Number(0,0))
            count[number] = Number(m, last)
    return number


if __name__ == "__main__":
    input_lines = read_input("input.txt")
    print(get_number([int(x) for x in input_lines], 2020))
    print(get_number([int(x) for x in input_lines], 30000000))

