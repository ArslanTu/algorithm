#
# @lc app=leetcode.cn id=1637 lang=python3
#
# [1637] 两点之间不包含任何点的最宽垂直面积
#

# @lc code=start
from itertools import pairwise
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return max([y - x for x, y in pairwise(sorted([point[0] for point in points]))])
# @lc code=end

