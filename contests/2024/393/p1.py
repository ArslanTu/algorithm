"""
weekply contest p1
"""
from typing import *


class Solution:
    def findLatestTime(self, s: str) -> str:
        if s[0] == '?':
            if s[1] =='?' or s[1] == '0' or s[1] == '1':
                s = "1" + s[1:]
            else:
                s = "0" + s[1:]
        if s[1] == '?':
            if s[0] == '0':
                s = s[0] + "9" + s[2:]
            else:
                s = s[0] + "1" + s[2:]
        if s[3] == '?':
            s = s[:3] + "5" + s[4:]
        if s[4] == '?':
            s = s[:4] + "9"
        return s

def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        ("1?:?4", "11:54"),
        ("0?:5?", "09:59"),
        ("?3:12", "03:12")
    ]
    for example in examples:
        s, ans = example
        print(f"Output: {sl.findLatestTime(s)}, Ans: {ans}")


if __name__ == "__main__":
    test()
