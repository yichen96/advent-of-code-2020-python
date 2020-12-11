def read_input(file_path: str) -> list:
    import os
    import sys
    with open(os.path.join(sys.path[0], file_path), "r") as f:
        return f.read().split("\n")

def use_all_adaptors(adapters):
    adapters.sort()

    jolts = 0
    one_diff = 0
    three_diff = 0
    for a in adapters:
        if a - jolts == 3:
            three_diff += 1
        elif a - jolts == 1:
            one_diff += 1

        jolts = a

    return one_diff * (three_diff + 1)


def combinations_adaptors(adapters):
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()

    size = len(adapters)
    checked = {}

    def arrange(i):
        if i == size - 1:
            return 1

        if i in checked:
            return checked[i]

        arrangements = arrange(i + 1)

        if i < size - 2 and adapters[i + 2] <= adapters[i] + 3:
            arrangements += arrange(i + 2)
        if i < size - 3 and adapters[i + 3] <= adapters[i] + 3:
            arrangements += arrange(i + 3)

        checked[i] = arrangements

        return arrangements

    return arrange(0)

if __name__ == "__main__":
    input_lines = read_input("input.txt")
    print(use_all_adaptors([int(num) for num in input_lines]))
    print(combinations_adaptors([int(num) for num in input_lines]))