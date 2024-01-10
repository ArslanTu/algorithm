from typing import *
from collections import *

class Solution:
    def check(self, a, b, c):
        ans = str(a)
        if ans.find(b) != -1:
            pass
        else:
            p_len = 0
            for i in range(1, min(len(ans), len(b))):
                if ans[len(ans) - i:] == b[:i]:
                    p_len = i
            ans += b[p_len:]

        if ans.find(c) != -1:
            pass
        else:
            p_len = 0
            for i in range(1, min(len(ans), len(c))):
                if ans[len(ans) - i:] == c[:i]:
                    p_len = i
            ans += c[p_len:]
        return ans
    
    def minimumString(self, a: str, b: str, c: str) -> str:
        res1 = self.check(a, b, c)
        res2 = self.check(a, c, b)
        res3 = self.check(b, a, c)
        res4 = self.check(b, c, a)
        res5 = self.check(c, a, b)
        res6 = self.check(c, b, a)
        ans = None
        for res in [res1, res2, res3, res4, res5, res6]:
            if ans == None:
                ans = res
            elif len(ans) > len(res):
                ans = res
            elif len(ans) == len(res):
                if ans > res:
                    ans = res
        return ans


sl = Solution()

cases = [(("ab", "ba", "aba"), "aba")]
for case in cases:
    ss, ans = case
    print(f"expect: {ans}, output: {sl.minimumString(*ss)}")