from bisect import bisect_left, bisect_right
from typing import *

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        i_idxs = []
        j_idxs = []
        for i in range(len(s) - len(a) + 1):
            if s[i:i+len(a)] == a:
                i_idxs.append(i)
        
        for j in range(len(s) - len(b) + 1):
            if s[j:j+len(b)] == b:
                j_idxs.append(j)
        
        ans = []
        if len(i_idxs) == 0 or len(j_idxs) == 0:
            return ans
        for i in i_idxs:
            # left
            l = max(0, i - k)
            r = i
            l_idx = bisect_left(j_idxs, l)
            r_idx = bisect_right(j_idxs, r)
            if r_idx - l_idx > 0:
                ans.append(i)
                continue
            # right
            l = i
            r = min(k + i, len(s) - len(b))
            l_idx = bisect_left(j_idxs, l)
            r_idx = bisect_right(j_idxs, r)
            if r_idx - l_idx > 0:
                ans.append(i)
        return sorted(list(ans))

sl = Solution()
examples = [
    ("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15, [16,33]),
    ("abcd", "a", "a", 4, [0]),
    ("lahhnlwx", "hhnlw", "ty", 6, []),
    ("frkxslnnn", "rkxsl", "n", 2, []),
]
for example in examples:
    s, a, b, k, ans = example
    print(f"Output: {sl.beautifulIndices(s, a, b, k)}, Ans: {ans}")