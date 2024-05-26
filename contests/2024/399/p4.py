"""
weekply contest p4
"""
from typing import *


class Solution:
    """
    solution class
    """

    def main_method(self) -> None:
        """
        main method
        """
        return


def test():
    """
    test func
    """
    sl = Solution()
    examples = [("abcde", "1a1b1c1d1e"), ("aaaaaaaaaaaaaabb", "9a5a2b")]
    for example in examples:
        word, ans = example
        print(f"Output: {sl.compressedString(word)}, Ans: {ans}")


if __name__ == "__main__":
    test()
