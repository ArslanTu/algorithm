# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # 前缀和
        arr = []
        ans = 0
        dummy = TreeNode(0)
        dummy.left = root

        def dfs(child_, pre):
            if not child_:
                return
            child_.val += pre
            dfs(child_.left, child_.val)
            dfs(child_.right, child_.val)

        dfs(dummy, 0)

        def dfs_2(root_):
            if not root_:
                return
            nonlocal ans
            arr.append(root_)
            for cur in arr[:-1]:
                if arr[-1].val - cur.val == sum:
                    ans += 1

            dfs_2(root_.left)
            dfs_2(root_.right)
            arr.pop(-1)
        
        dfs_2(dummy)

        return ans