from math import inf
from typing import *

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ""
        if s.count('1') == k:
            return s.strip('0')

        pos = [i for i in range(len(s)) if s[i] == '1']
        l = inf
        se = (-1, -1)
        for i  in range(k - 1, len(pos)):
            if pos[i] - pos[i - k + 1] + 1 < l:
                l = pos[i] - pos[i - k + 1] + 1
                se = (pos[i - k + 1], pos[i])
            elif pos[i] - pos[i - k + 1] + 1 == l:
                if s[se[0]:se[1] + 1] > s[pos[i - k + 1]:pos[i] + 1]:
                    se = (pos[i - k + 1], pos[i])
        return s[se[0]:se[1] + 1]

sl = Solution()
examples = [
    # ("100011001", 3, "11001"),
    # ("1011", 2, "11"),
    # ("000", 1, ""),
    ("111111110010001010", 11, "11111111001000101")
]
for example in examples:
    s, k, ans = example
    print(f"Output: {sl.shortestBeautifulSubstring(s, k)}, Ans: {ans}")