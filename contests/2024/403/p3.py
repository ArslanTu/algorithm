"""
weekply contest p3
"""
from typing import *


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        pieces = []
        last_piece = []
        for i in range(n):
            if len(last_piece) == 0:
                last_piece.append(nums[i])
                continue
            if nums[i] < 0:
                last_piece.append(nums[i])
            else:
                if last_piece[-1] >= 0:
                    total += last_piece[-1]
                    last_piece = [nums[i]]
                else:
                    pieces.append(list(last_piece))
                    last_piece = [nums[i]]
        pieces.append(list(last_piece))
        for piece in pieces:
            if piece[0] < 0:
                for i in range(len(piece)):
                    total += piece[i] * (-1) ** (i)
            else:
                first_sum = 0
                second_sum = piece[0]
                for i in range(len(piece)):
                    first_sum += piece[i] * (-1)**(i)
                    if i > 0:
                        second_sum += piece[i] * (-1)**(i - 1)
                total += max(first_sum, second_sum)
        return total




def test():
    """
    test func
    """
    sl = Solution()
    # examples = [([1, -2, 3, 4], 10), ([-14, -13, -20], -7)]
    examples = [([-14, -13, -20], -7)]
    for example in examples:
        nums, ans = example
        print(f"Output: {sl.maximumTotalCost(nums)}, Ans: {ans}")


if __name__ == "__main__":
    test()
