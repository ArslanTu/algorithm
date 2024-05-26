"""
weekply contest p2
"""
from typing import *


class Solution:

    def compressedString(self, word: str) -> str:
        comp = ""
        while word:
            cur_chr = word[0]
            cnt = 1
            while cnt < 9 and cnt < len(word) and word[cnt] == cur_chr:
                cnt += 1
            comp += str(cnt) + cur_chr
            word = word[cnt:]
        return comp



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
