from typing import *


class Node:
    def __init__(self, val: str):
        self.val = val
        self.children: List[Node] = []

def insert(num, root)

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        return findMaximumXOR(nums)


sl = Solution()
examples = [
    ([1,2,3,4,5], 7),
    ([10,100], 0),
    ([500,520,2500,3000], 1020)
]
for example in examples:
    nums, ans = example
    print(f"Output: {sl.maximumStrongPairXor(nums)}, Ans: {ans}")