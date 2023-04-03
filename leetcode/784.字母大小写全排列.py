#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        n = len(s)

        def choose(cur_pos, cur_s):
            # 到大终点，停止
            if cur_pos == n:
                ans.append(cur_s)
                return
            # 当前位置不变化
            choose(cur_pos + 1, cur_s + s[cur_pos])

            # 当前位置变化（可以的话）
            if ord('a') <= ord(s[cur_pos]) <= ord('z'):
                choose(cur_pos + 1, cur_s + s[cur_pos].upper())
            elif ord('A') <= ord(s[cur_pos]) <= ord('Z'):
                choose(cur_pos + 1, cur_s + s[cur_pos].lower())

        choose(0, "")
        return ans
# @lc code=end

