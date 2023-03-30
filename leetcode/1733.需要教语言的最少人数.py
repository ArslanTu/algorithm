#
# @lc app=leetcode.cn id=1733 lang=python3
#
# [1733] 需要教语言的最少人数
#

# @lc code=start
from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        no_common =  set()
        languages = [set(l) for l in languages]
        for i, j in friendships:
            if not (languages[i - 1] & languages[j - 1]):
                no_common.add(i)
                no_common.add(j)
        if len(no_common) == 0:
            return 0
        language_cnt = [0] * n
        for i in no_common:
            for l in languages[i - 1]:
                language_cnt[l - 1] += 1
        max_pop = max(language_cnt)
        return len(no_common) - max_pop
# @lc code=end

