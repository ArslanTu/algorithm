#
# @lc app=leetcode.cn id=1452 lang=python3
#
# [1452] 收藏清单
#

# @lc code=start
from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [set(fc) for fc in favoriteCompanies]
        n = len(favoriteCompanies)
        ans = set(range(n))
        for idx in range(n):
            if idx in ans:
                for after in range(idx + 1, n):
                    if after in ans:
                        if favoriteCompanies[idx] < favoriteCompanies[after]:
                            ans.remove(idx)
                            break
                        elif favoriteCompanies[after] < favoriteCompanies[idx]:
                            ans.remove(after)
        return list(ans)
# @lc code=end

