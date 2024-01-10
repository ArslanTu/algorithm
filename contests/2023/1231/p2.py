from typing import *

class Solution:
    def maximumLength(self, s: str) -> int:
        chs = "abcdefghijklmnopqrstuvwxyz"
        ans = -1

        def cnt(ss):
            res = 0
            for i in range(0, len(s) - len(ss) + 1):
                if s[i:i+len(ss)] == ss:
                    res += 1
            return res

        for ch in chs:
            cur_sub_s = ch
            while cur_sub_s in s:
                if cnt(cur_sub_s) >= 3:
                    ans = max(len(cur_sub_s), ans)
                    cur_sub_s += ch
                else:
                    break
        return ans


sl = Solution()
examples = [
    ("aaaa", 2),
    ("abcdef", -1),
    ("abcaba", 1),
]
for example in examples:
    s, ans = example
    print(f"Output: {sl.maximumLength(s)}, Ans: {ans}")