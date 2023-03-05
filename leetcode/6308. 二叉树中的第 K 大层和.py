# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from heapq import heappush, nlargest
from typing import Optional


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = [root]
        nums = []
        while queue:
            n = len(queue)
            layer_sum = 0
            while n:
                cur = queue.pop(0)
                layer_sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                n -= 1
            heappush(nums, layer_sum)
        if len(nums) < k:
            return -1
        return nlargest(k, nums)[k - 1]



sl = Solution()

p1 = 

print(sl)