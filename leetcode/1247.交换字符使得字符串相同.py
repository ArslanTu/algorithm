#
# @lc app=leetcode.cn id=1247 lang=python3
#
# [1247] 交换字符使得字符串相同
#

# @lc code=start
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        n = len(s1)
        num_01 = num_10 = 0
        for idx in range(n):
            if s1[idx] == 'x' and s2[idx] == 'y':
                num_01 += 1
            elif s1[idx] == 'y' and s2[idx] == 'x':
                num_10 += 1
        if (((num_01 & 1) == 0) and ((num_10 & 1) != 0)) or (((num_01 & 1) != 0) and ((num_10 & 1) == 0)):
            return -1
        ans = (num_01 >> 1) + (num_10 >> 1) + (num_01 & 1) * 2
        return ans
# @lc code=end

