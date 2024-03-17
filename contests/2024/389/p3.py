from bisect import bisect_right
from math import inf
from typing import *


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        nums = sorted(cnt.values())
        ans = {}
        for i in range(len(nums)):
            if nums[i] in ans:
                continue
            cur_ans = 0
            for j in range(len(nums)):
                if j < i:
                    cur_ans += nums[j]
                elif j == i:
                    continue
                else:
                    if nums[j] - nums[i] > k:
                        cur_ans += nums[j] - nums[i] - k
            ans[nums[i]] = cur_ans
        return min(ans.values())



sl = Solution()
examples = [
    ("aabcaba", 0, 3),
    ("dabdcbdcdcd", 2, 2),
    ("aaabaaa", 2, 1),
    ("vvnowvov", 2, 1),
    ("klllurlrrul", 1, 3),
]
for example in examples:
    words, k, ans = example
    print(f"Output: {sl.minimumDeletions(words, k)}, Ans: {ans}")