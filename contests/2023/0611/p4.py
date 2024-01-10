from typing import List, Optional


class Trie:
    def __init__(self):
        self.root = {}
    
    def add(self, num1, num2):
        node = self.root
        for i in range(31, -1, -1):
            bit1 = (num1 >> i) & 1
            bit2 = (num2 >> i) & 1
            if bit1 not in node:
                node[bit1] = {}
            if bit2 not in node[bit1]:
                node[bit1][bit2] = {}
            node = node[bit1][bit2]
    
    def search(self, num1, num2, target1, target2):
        node = self.root
        res = 0
        for i in range(31, -1, -1):
            bit1 = (num1 >> i) & 1
            bit2 = (num2 >> i) & 1
            bit1_t = (target1 >> i) & 1
            bit2_t = (target2 >> i) & 1
            if bit1_t == 1 and bit2_t == 1:  # 必须两个数的当前位都符合条件
                if 1 - bit1 in node and 1 - bit2 in node[1 - bit1]:  # 如果当前字典树中有符合要求的数，记录最大值
                    node = node[1 - bit1][1 - bit2]
                    res += (1 << i)
                else:
                    node = node[bit1][bit2]
            elif bit1_t == 1:  # 只要求 num1 符合条件
                if 1 - bit1 in node:  # 如果当前字典树中有符合要求的数，记录最大值
                    node = node[1 - bit1][bit2]
                    res += (1 << i)
                else:
                    node = node[bit1][bit2]
            elif bit2_t == 1:  # 只要求 num2 符合条件
                if 1 - bit2 in node:  # 如果当前字典树中有符合要求的数，记录最大值
                    node = node[bit1][1 - bit2]
                    res += (1 << i)
                else:
                    node = node[bit1][bit2]
            else:  # 如果两个数当前位都不符合条件，搜索下一位
                node = node[bit1][bit2]
        return res if res > 0 else -1

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        trie = Trie()
        for i in range(len(nums1)):
            trie.add(nums1[i], nums2[i])
        res = []
        for q in queries:
            x, y = q[0], q[1]
            tmp = trie.search(nums1[i], nums2[i], x, y)
            res.append(tmp)
        return res


sl = Solution()
params = (([4,3,1,2], [2,4,9,5], [[4,1],[1,3],[2,5]]),
          ([3,2,5], [2,3,4], [[4,4],[3,2],[1,1]]),
          ([2,1], [2,3], [[3,3]]))
f_ans = ([6,10,7], [9,9,9], [-1])
for i in range(len(params)):
    print(sl.maximumSumQueries(params[i][0], params[i][1], params[i][2]) == f_ans[i])