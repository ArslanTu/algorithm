from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        mapping = [0] * n
        cur = 0
        r = 1
        while mapping[cur] != 1:
            mapping[cur] += 1
            cur = (cur + r * k) % n
            r += 1
        ans = []
        for i in range(n):
            if mapping[i] == 0:
                ans .append(i + 1)
        return ans

sl = Solution()
p1 = 5
p2 = 2
print(sl.circularGameLosers(p1, p2))