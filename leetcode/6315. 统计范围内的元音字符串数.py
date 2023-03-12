from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        for i in range(left, right + 1):
            word = words[i]
            if (word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u') and (word[-1] == 'a' or word[-1] == 'e' or word[-1] == 'i' or word[-1] == 'o' or word[-1] == 'u'):
                ans += 1
        return ans

sl = Solution()
p1 = ["hey","aeo","mu","ooo","artro"]

print(sl.vowelStrings(p1, 1, 4))