#
# @lc app=leetcode.cn id=1641 lang=python3
#
# [1641] 统计字典序元音字符串的数目
#

# @lc code=start
class Solution:
    def countVowelStrings(self, n: int) -> int:
        # 记忆化搜索
        # @cache
        # def dfs(cur_pos, cur_ch):
        #     nonlocal n
        #     if cur_pos == n:
        #         return 1
        #     return sum([dfs(cur_pos + 1, i) for i in range(cur_ch, 5)])

        # return dfs(0, 0)

        # 动态规划
        dp = [[0] * 5 for _ in range(n)]
        for i in range(5):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(5):
                dp[i][j] += sum(dp[i - 1][k] for k in range(j + 1))
        return sum(dp[n - 1][j] for j in range(5))
# @lc code=end

sl = Solution()
print(sl.countVowelStrings(2))