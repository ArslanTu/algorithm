from typing import *

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_freq = max(cnt.values())
        max_cnt = sum([cnt[k] == max_freq for k in cnt.keys()])
        return max_cnt * max_freq        

sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")