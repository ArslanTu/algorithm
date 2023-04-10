#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        n = len(nums)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return ans
# @lc code=end

