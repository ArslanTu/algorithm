#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#

# @lc code=start
from math import ceil


class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0: return '0'
        ans = ""
        while n:
            if n == 1:
                ans = '1' + ans
                return ans
            elif n == -1:
                ans = '11' + ans
                return ans
            else:
                if (n & 1) == 1:
                    ans = '1' + ans
                else:
                    ans = '0' + ans
                if n > 0:
                    n = -(n // 2)
                else:
                    n = ceil((-n) / 2)
        return ans

# @lc code=end

sl = Solution()
p1 = 4
print(sl.baseNeg2(p1))