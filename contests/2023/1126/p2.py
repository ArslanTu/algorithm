from typing import *

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vo_ch = "aeiou"
        nums = [1 if c in vo_ch else 0 for c in s]
        ans = 0
        for i in range(len(s)):
            cnt = [0, 0]
            for j in range(i, len(s)):
                if nums[j] == 0:
                    cnt[0] += 1
                else:
                    cnt[1] += 1
                if (cnt[0] == cnt[1]) and ((cnt[0] * cnt[1]) % k == 0):
                    ans += 1
        return ans


sl = Solution()
examples = [
    ("baeyh", 2, 2),
    ("ihroyeeb", 5, 0),
]
for example in examples:
    s, k, ans = example
    print(f"Output: {sl.beautifulSubstrings(s, k)}, Ans: {ans}")