#
# @lc app=leetcode.cn id=1638 lang=python3
#
# [1638] 统计只差一个字符的子串数目
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        # 暴力，枚举
        # ans = 0
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         diff = 0
        #         k = 0
        #         while i + k < len(s) and j + k < len(t):
        #             if s[i + k] != t[j + k]:
        #                 diff += 1
        #             if diff == 1:
        #                 ans += 1
        #             if diff > 1:
        #                 break
        #             k += 1
        # return ans
        m, n = len(s), len(t)
        dpl = [[0] * (n + 1) for _ in range(m + 1)]
        dpr = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dpl[i + 1][j + 1] = dpl[i][j] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dpr[i][j] = dpr[i + 1][j + 1] + 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    ans += (dpl[i][j] + 1) * (dpr[i + 1][j + 1] + 1)
        return ans
# @lc code=end

p1 = "ab"
p2 = "bb"
sl = Solution()
print(sl.countSubstrings(p1, p2))