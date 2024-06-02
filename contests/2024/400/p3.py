"""
weekply contest p3
"""
from typing import *


class Solution:
    def clearStars(self, s: str) -> str:
        star_pos = [idx for idx, x in enumerate(s) if x == "*"]
        to_del = set(star_pos)
        if not star_pos:
            return s
        chs_pos = [[] for _ in range(26)]
        for idx, x in enumerate(s):
            if x == "*":
                for i in range(26):
                    if chs_pos[i]:
                        to_del.add(chs_pos[i].pop())
                        break
            else:
                chs_pos[ord(x) - ord("a")].append(idx)
        t = ""
        for idx, c in enumerate(s):
            if idx not in to_del:
                t += c
        return t



def test():
    """
    test func
    """
    sl = Solution()
    examples = [("aaba*", "aab"), ("abc", "abc")]
    for example in examples:
        s, ans = example
        print(f"Output: {sl.clearStars(s)}, Ans: {ans}")


if __name__ == "__main__":
    test()
