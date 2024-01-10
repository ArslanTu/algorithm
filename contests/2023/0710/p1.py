from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for w in words:
            ans += w.split(separator)
        ans_s = []
        for a in ans:
            if a != "":
                ans_s.append(a)
        return ans_s
sl = Solution()
cases = [()]
for case in cases:
    print(f"output: {sl}, ans: {ans}")