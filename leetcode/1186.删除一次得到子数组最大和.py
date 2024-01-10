#
# @lc app=leetcode.cn id=1186 lang=python3
#
# [1186] 删除一次得到子数组最大和
#

# @lc code=start
from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = max(arr)
        if ans <= 0:
            return ans
        n = len(arr)
        
        def dfs(start):
            nonlocal ans, n
            min_neg = 0
            cur_sum = 0
            max_sum = 0
            todo = set()
            for i in range(start, n):
                num = arr[i]
                cur_sum += num
                min_neg = min(min_neg, num)
                max_sum = cur_sum - min_neg
                if cur_sum <= 0:
                    todo.add(i + 1)
                if max_sum <= 0:
                    todo.add(i + 1)
                    break
                ans = max(ans, max_sum)
            for s in todo:
                dfs(s)
        dfs(0)
        return ans
# @lc code=end

arr = [11,-10,-11,8,7,-6,9,4,11,6,5,0]
sl = Solution()
print(sl.maximumSum(arr))