from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diff = [[reward1[i] - reward2[i], i] for i in range(n)]
        diff.sort(key=lambda x: x[0], reverse=True)
        ans = 0
        for i in range(n):
            if i < k:
                ans += reward1[diff[i][1]]
            else:
                ans += reward2[diff[i][1]]
        return ans

sl = Solution()
p1 = [1,1,3,4]
p2 = [4,4,1,1]
p3 = 2
print(sl.miceAndCheese(p1 ,p2, p3))