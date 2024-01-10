from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort(reverse=True)
        n = len(usageLimits)
        l, h = 0, n
        ans = 0

        def check(x):
            nonlocal n
            nums = [-usageLimits[i] for i in range(n)]
            heapify(nums)
            for i in range(x, 0, -1):
                j = i
                if not nums:
                    return False
                tmp = heappop(nums)
                tmp = -tmp
                if tmp >= j:
                    continue
                else:
                    j -= tmp
                    while j > 0:
                        if not nums:
                            return False
                        tmp = heappop(nums)
                        tmp = -tmp
                        if tmp >= j:
                            tmp -= j
                            j = 0
                            if tmp > 0:
                                heappush(nums, -tmp)
                        else:
                            j -= tmp
                
            return True

        while l <= h:
            mid = (l + h) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                h = mid - 1
        return ans


sl = Solution()
# print(sl.maxIncreasingGroups([2,2,2], " ", 3))
print(sl.maxIncreasingGroups([1,5,1,5,7,8,1,1,3,1,9,3]), " ", 9)