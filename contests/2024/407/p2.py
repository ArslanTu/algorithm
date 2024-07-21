"""
weekply contest p2
"""
from typing import *


class Solution:

    def doesAliceWin(self, s: str) -> bool:
        chs = "aeiou"
        flag = False
        while s:
            if not flag:
                # alice turn
                cnt = 0
                last_idx = -1
                for i in range(len(s)):
                    if s[i] in chs:
                        cnt += 1
                    if cnt % 2 == 1:
                        last_idx = i
                if last_idx == -1:
                    return False
                s = s[last_idx + 1:]
                flag = True
            else:
                # bob turn
                cnt = 0
                last_idx = -1
                for i in range(len(s)):
                    if s[i] in chs:
                        cnt += 1
                    if cnt % 2 == 0:
                        last_idx = i
                if last_idx == -1:
                    return True
                s = s[last_idx + 1:]
                flag = False
        return flag



def test():
    """
    test func
    """
    sl = Solution()
    examples = []
    for example in examples:
        ans = example
        print(f"Output: {sl}, Ans: {ans}")


if __name__ == "__main__":
    test()
