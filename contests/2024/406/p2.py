"""
weekply contest p2
"""
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head
        while cur.next:
            if cur.next.val in nums:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next

def test():
    """
    test func
    """
    sl = Solution()
    examples = [
    ]
    for example in examples:
        ans = example
        print(f"Output: {sl}, Ans: {ans}")


if __name__ == "__main__":
    test()
