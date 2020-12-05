def read_input(file_path: str) -> list:
    import os
    import sys
    with open(os.path.join(sys.path[0], file_path), "r") as f:
        return f.read().split('\n')

def pass2id(boarding_pass: str, value_map: dict) -> int:
    row = [value_map[value] * 2**index  for index, value in enumerate(boarding_pass[6::-1])]
    col = [value_map[value] * 2**index  for index, value in enumerate(boarding_pass[10:6:-1])]

    return sum(row) * 8 + sum(col)


if __name__ == "__main__":
    boarding_passes = read_input("input.txt")
    value_map = {'F': 0, 'B': 1, 'R': 1, 'L': 0}
    boarding_passes_id = [pass2id(boarding_pass, value_map) for boarding_pass in boarding_passes]
    print(max(boarding_passes_id))
    boarding_passes_id = sorted(boarding_passes_id)
    print(
    set(range(boarding_passes_id[0],boarding_passes_id[-1])).difference(boarding_passes_id)
        )