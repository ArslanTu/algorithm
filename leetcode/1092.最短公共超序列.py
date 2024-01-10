#
# @lc app=leetcode.cn id=1092 lang=python3
#
# [1092] 最短公共超序列
#

# @lc code=start
from collections import Counter


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]



# @lc code=end

