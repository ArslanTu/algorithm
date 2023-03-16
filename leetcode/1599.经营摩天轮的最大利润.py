#
# @lc app=leetcode.cn id=1599 lang=python3
#
# [1599] 经营摩天轮的最大利润
#

# @lc code=start
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = [0, 0]
        cur_cus = 0
        profit = 0
        turns = 0
        # 一边转一边累加客人总数
        for num in customers:
            cur_cus += num
            batch = min(4, cur_cus)
            cur_cus -= batch
            profit += batch * boardingCost
            turns += 1
            profit -= runningCost
            if profit > ans[0]:
                ans = [profit, turns]
        # 客人都到了之后还剩的轮次
        while cur_cus:
            batch = min(4, cur_cus)
            cur_cus -= batch
            profit += batch * boardingCost
            turns += 1
            profit -= runningCost
            if profit > ans[0]:
                ans = [profit, turns]
        # 没有客人在等待，需要 3 轮把剩下的客人送到地面
        profit -= 3 * runningCost
        turns += 3
        if profit > ans[0]:
            ans = [profit, turns]

        if ans[0]:
            return ans[1]
        else:
            return -1
# @lc code=end

