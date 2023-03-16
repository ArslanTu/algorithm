#
# @lc app=leetcode.cn id=2488 lang=python3
#
# [2488] 统计中位数为 K 的子数组
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 大于 k 标记为 1，小于 k 标记为 -1
        # 转换为前缀和
        # n = len(nums)
        # k_idx = 0
        # nums_convert = [0] * n
        # for idx in range(n):
        #     if nums[idx] > k:
        #         nums_convert[idx] = 1
        #     elif nums[idx] < k:
        #         nums_convert[idx] = -1
        #     else:
        #         k_idx = idx
        # ans = 0
        # pre_sum = []
        # cur_sum = 0
        # for num in nums_convert:
        #     cur_sum += num
        #     pre_sum.append(cur_sum)
        # cnt = Counter({0: 1})
        # for idx in range(n):
        #     if idx >= k_idx:
        #         ans += cnt[pre_sum[idx]]
        #         ans += cnt[pre_sum[idx] - 1]
        #     if idx < k_idx:
        #         cnt[pre_sum[idx]] += 1
        # return ans
        cur_sum = ans = 0
        k_idx = nums.index(k)
        cnt = Counter({0: 1})
        for idx in range(len(nums)):
            if nums[idx] > k:
                cur_sum += 1
            elif nums[idx] < k:
                cur_sum -= 1
            if idx >= k_idx:
                ans += cnt[cur_sum] + cnt[cur_sum - 1]
            else:
                cnt[cur_sum] += 1
        return ans
# @lc code=end

sl = Solution()
# p1 = [3,2,1,4,5]
# p2 = 4

p1 = [2,3,1]
p2 = 3
print(sl.countSubarrays(p1, p2))