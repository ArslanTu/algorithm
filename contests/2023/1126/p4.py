from math import sqrt
from typing import *

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vo_ch = "aeiou"
        
        



sl = Solution()
examples = [
    ("baeyh", 2, 2),
    ("ihroyeeb", 5, 0),
    ("eeebjoxxujuaeoqibd", 8, 4),
    ("ilougekqlovegioemdvu", 4, 21),
]
for example in examples:
    s, k, ans = example
    print(f"Output: {sl.beautifulSubstrings(s, k)}, Ans: {ans}")