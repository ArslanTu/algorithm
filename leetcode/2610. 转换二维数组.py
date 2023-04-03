from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        cnt = [[i, 0] for i in range(n + 1)]
        for num in nums:
            cnt[num][1] += 1
        cnt.sort(key=lambda x: x[1], reverse=True)
        ans = [[] for _ in range(cnt[0][1])]
        for elem in cnt:
            if elem[1] > 0:
                i = 0
                while elem[1] > 0:
                    ans[i].append(elem[0])
                    elem[1] -= 1
                    i += 1
        return ans

sl = Solution()
p1 = 
print(sl)