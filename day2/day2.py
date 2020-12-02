from typing import Callable

def read_input(file_path: str) -> list:
    import os
    import sys
    with open(os.path.join(sys.path[0], file_path), "r") as f:
        return f.read().split('\n')

def is_valid_occurrence(password: str) -> bool:
    """
    Check if given password is valid.
    Example: '1-3 b: cdefg' means at cdefg must contain at least 1 b at most 3 b,
    thus password is not valid because it contains no b.

    :type password: str
    :rtype: bool
    """
    import re
    min_occurrence, max_occurrence, letter, pwd = re.split(': |-| ',password)
    return int(min_occurrence) <= pwd.count(letter) <= int(max_occurrence)

def count_valid_passwords(passwords: list, validity_check: Callable[[str], bool]) -> int:
    """
    Return the count of valid passwords given in a list

    :type passwords: List[str]
    :rtype: int
    """
    count = 0
    for password in passwords:
        if validity_check(password):
            count += 1
    return count

def is_valid_position(password: str) -> bool:
    """
    Check if given password is valid.
    Example: '1-3 b: cdefg' is invalid: neither position 1 nor position 3 contains b.

    :type password: str
    :rtype: bool
    """
    import re
    first_index, second_index, letter, pwd = re.split(': |-| ',password)
    return (pwd[int(first_index)-1] == letter) ^ (pwd[int(second_index)-1] == letter)


if __name__ == "__main__":
    passwords = read_input("input.txt")
    print("part 1 result: ", count_valid_passwords(passwords, is_valid_occurrence))
    print("part 1 result: ", count_valid_passwords(passwords, is_valid_position))