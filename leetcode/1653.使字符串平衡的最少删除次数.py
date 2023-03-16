#
# @lc app=leetcode.cn id=1653 lang=python3
#
# [1653] 使字符串平衡的最少删除次数
#

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # 枚举分界线，同时更新两侧计数，取最小操作数
        s = ' ' + s + ' '
        ans = n = len(s)
        left_b, right_a = 0, s.count('a')
        for ch in s:
            if ch == 'a':
                right_a -= 1
            elif ch == 'b':
                left_b += 1
            ans = min(ans, left_b + right_a)
        return ans
# @lc code=end

sl = Solution()

# p1 = "aababbab"
p1 = "bbaaaaabb"

print(sl.minimumDeletions(p1))