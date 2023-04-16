from typing import List
from collections import Counter, defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n
        mapping = defaultdict(list)
        for idx, num in enumerate(nums):
            mapping[num].append(idx)
        for num, idx_list in mapping.items():
            if len(idx_list) > 1:
                nums_2 = list(idx_list)
                m = len(idx_list)
                for i in range(1, m):
                    nums_2[i] += nums_2[i - 1]
                for idx, num in enumerate(nums_2):
                    presum = nums_2[idx - 1] if idx > 0 else 0
                    arr[idx_list[idx]] = idx_list[idx] * idx - presum + nums_2[-1] - nums_2[idx] - idx_list[idx] * (m - idx - 1)
        return arr




sl = Solution()

p1 = [1,3,1,1,2]

print(sl.distance(p1))