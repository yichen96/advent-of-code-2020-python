def read_input(file_path: str) -> list:
    import os
    import sys
    with open(os.path.join(sys.path[0], file_path), "r") as f:
        return f.read().split('\n')

def count_trees(map: list, start: tuple, vector: tuple) -> int:
    """
    Count the number of '#' trees encountered by following 
    the movement of vector until reach the last line.
    """
    x, y = start
    count = 0
    width = len(map[0])
    while y < len(map)-1:
        x += vector[0]
        y += vector[1]
        if x >= width:
            x -= width
        if map[y][x] == '#':
            count += 1
    return count

if __name__ == "__main__":
    from functools import reduce
    input_map = read_input("input.txt")
    print(reduce((lambda x, y: x * y), 
                [count_trees(input_map, (0,0), vector) 
                for vector in 
                [(1,1), (3,1), (5,1), (7,1), (1,2)]]))