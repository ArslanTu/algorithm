#
# @lc app=leetcode.cn id=1110 lang=python3
#
# [1110] 删点成林


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        head = TreeNode()
        head.left = root
        ans = [root]

        def dfs(root_):
            if root_.left:
                cur = root_.left
                if root_.left.val in to_delete:
                    root_.left = None
                    if cur.left:
                        ans.append(cur.left)
                    if cur.right:
                        ans.append(cur.right)
                dfs(cur)
            if root_.right:
                cur = root_.right
                if root_.right.val in to_delete:
                    root_.right = None
                    if cur.left:
                        ans.append(cur.left)
                    if cur.right:
                        ans.append(cur.right)
                dfs(cur)

        dfs(head)
        res = []
        for node in ans:
            if node.val not in to_delete:
                res.append(node)
        return res
# @lc code=end

