
def read_input(file_path: str) -> list:
    import os
    import sys
    with open(os.path.join(sys.path[0], file_path), "r") as f:
        return f.read().split()

def two_sum(nums: list, target: int) -> tuple:
    """
    Return the two numbers that their sum makes the target number.
    Assume only 1 pair exists.

    :type nums: List[str]
    :type target: int
    :rtype: Tuple[int]
    """
    nums = [int(n) for n in nums]
    for i in range(len(nums)):
        search_for = target - nums[i]
        for j in range(i+1,len(nums)):
            if nums[j] == search_for:
                return nums[i], search_for
    return None, None

def three_sum(nums: list, target: int) -> tuple:
    """
    Return the three numbers that their sum makes the target number.
    Assume only 1 solution exists.

    :type nums: List[str]
    :type target: int
    :rtype: Tuple[int]
    """    
    nums = [int(n) for n in nums]
    for i in range(len(nums)):
        search_for = target - nums[i]
        num1, num2 = two_sum(nums[i+1:],search_for)
        if num1 is not None:
            return nums[i], num1, num2

if __name__ == "__main__":
    numbers = read_input("input.txt")
    num1, num2 = two_sum(numbers, 2020)
    print("part 1 result: ", num1*num2)
    num1, num2, num3 = three_sum(numbers, 2020)
    print("part 2 result: ", num1*num2*num3)

