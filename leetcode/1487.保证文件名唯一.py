#
# @lc app=leetcode.cn id=1487 lang=python3
#
# [1487] 保证文件名唯一
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        cnt = Counter()
        for name in names:
            if not cnt[name]:
                ans.append(name)
            else:
                k = cnt[name]
                while cnt[name + f"({k})"]:
                    k += 1
                ans.append(name + f"({k})")
                cnt[name + f"({k})"] += 1
            cnt[name] += 1
        return ans
# @lc code=end

