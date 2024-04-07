from typing import *


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:

        def dis(c1, c2):
            return min(abs(ord(c1) - ord(c2)), 26 - abs(ord(c1) - ord(c2)))
        
        total_dis = 0
        t = ""
        for c1 in s:
            for c2 in "abcdefghijklmnopqrstuvwxyz":
                if dis(c1, c2) + total_dis <= k:
                    t += c2
                    total_dis += dis(c1, c2)
                    break
        return t

sl = Solution()
examples = [
    ("zbbz", 3, "aaaz"),
    ("xaxcd", 4, "aawcd"),
    ("lol", 0, "lol"),
]
for example in examples:
    s, k, ans = example
    print(f"Output: {sl.getSmallestString(s, k)}, Ans: {ans}")