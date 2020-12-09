def read_input(file_path: str) -> list:
    import os
    import sys
    with open(os.path.join(sys.path[0], file_path), "r") as f:
        return f.read().split("\n")


def find_invalid(nums, window_size=25):
    n = len(nums)

    for x in range(window_size, n):
        good = False

        for i in range(x-window_size, x-1):
            if good:
                break

            for j in range(i+1, x):
                if nums[i] + nums[j] == nums[x]:
                    good = True
                    break
                
        if not good:
            return nums[x]

def solve(nums):
    target = find_invalid(nums)
    n = len(nums)

    for i in range(n):
        total = nums[i]

        for j in range(i+1, n):
            total += nums[j]
            
            if total == target:
                return min(nums[i:j+1]) + max(nums[i:j+1])
            if total > target:
                break

if __name__ == "__main__":
    input_lines = read_input("input.txt")
    print(find_invalid([int(input_line) for input_line in input_lines])) 
    print(solve([int(input_line) for input_line in input_lines]))      