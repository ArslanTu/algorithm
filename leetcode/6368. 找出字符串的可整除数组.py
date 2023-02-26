from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        div = []
        n = len(word)
        cur = 0
        for i in range(n):
            cur *= 10
            cur += int(word[i])
            cur %= m
            if cur == 0:
                div.append(1)
            else:
                div.append(0)
        return div

sl = Solution()

# p1 = "998244353"
# p2 = 3

p1 = "1010"
p2 = 10

print(sl.divisibilityArray(p1, p2))