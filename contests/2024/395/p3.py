"""
weekply contest p1
"""
from typing import *

class Solution:
    def find_rec(s: str, cur_pos):


    def find(x: int) -> list[int]:



    def minEnd(self, n: int, x: int) -> int:
        x_bin = bin(x)[2:]
        a = len(x_bin)
        st = (2 ** (a - 1))
        end = (2 ** a) - 1
        nums = []
        for i in range(st, end + 1):
            if (i & x) == x:
                nums.append(i)
        if len(nums) >= n:
            return nums[n - 1]

        turn = (n // len(nums))
        n = n % len(nums)

        if n > 0:
            added = turn << a
            return nums[n - 1] + added
        else:
            added = (turn - 1) << a
            return nums[-1] + added





def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        (3, 4, 6),
        (2, 7, 15),
        (5, 1, 9),
        (2, 7, 15),
        (3, 2, 6),
        (6715154, 7193485, 0),
        (35867441, 21379379, 0),
        (8117750, 77156578, 0),
    ]
    for example in examples:
        n, x, ans = example
        print(f"Output: {sl.minEnd(n, x)}, Ans: {ans}")


if __name__ == "__main__":
    test()
