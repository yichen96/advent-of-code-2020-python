def read_input(file_path: str) -> list:
    import os
    import sys
    with open(os.path.join(sys.path[0], file_path), "r") as f:
        return f.read().split("\n\n")

def count_answers_any(group_answer: str) -> int:
    return len(set(list(group_answer.replace("\n",""))))

def count_answers_all(group_answer: str) -> int:
    from collections import defaultdict
    group_answer = group_answer.split("\n")
    count = 0
    people_count = 0
    answer_map = defaultdict(int)
    for answer in group_answer:
        people_count += 1
        for char in answer:
            answer_map[char] += 1
    for k in answer_map:
        if answer_map[k] == people_count:
            count += 1
    return count


if __name__ == "__main__":
    group_answers = read_input("input.txt")
    print(sum([count_answers_any(group_answer) for group_answer in group_answers]))
    print(sum([count_answers_all(group_answer) for group_answer in group_answers]))