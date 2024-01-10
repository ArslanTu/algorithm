#
# @lc app=leetcode.cn id=1000 lang=python3
#
# [1000] 合并石头的最低成本
#

# @lc code=start
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if k > 2 and len(stones) % (k - 1) != 1:
            return -1
        # 每次找到当前剩余石堆中，连续 k 个石堆的最小和
        ans = 0
        while (len(stones) > 1):
            k_sum = []
            start_idx = 0
            for i in range(len(stones) - k + 1):
                k_sum.append(sum(stones[i:i + k]))
                if k_sum[-1] < k_sum[start_idx]:
                    start_idx = i
            ans += k_sum[start_idx]
            stones = stones[:start_idx] + [k_sum[start_idx]] + stones[start_idx + k:]
        return ans
# @lc code=end

sl = Solution()
p1 = [6,4,4,6]
p2 = 2
print(sl.mergeStones(p1, p2))