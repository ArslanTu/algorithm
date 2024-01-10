from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            if cur.next and cur.next.val >= 5:
                res = cur.val * 2 + 1
                if res >= 10 and cur == head:
                    p = ListNode()
                    p.val = 1
                    p.next = head
                    head = p
                cur.val = res % 10
            else:
                res = cur.val * 2
                if res >= 10 and cur == head:
                    p = ListNode()
                    p.val = 1
                    p.next = head
                    head = p
                cur.val = res % 10
            cur = cur.next
        return head

sl = Solution()

examples = [
    (),
]
for ex in examples:
    p, ans = ex
    print(f"output: {sl}, expect: {ans}")