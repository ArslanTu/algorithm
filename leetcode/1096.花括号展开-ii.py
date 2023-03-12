#
# @lc app=leetcode.cn id=1096 lang=python3
#
# [1096] 花括号展开 II
#

# @lc code=start
from typing import List, Set


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # 所有字母先加大括号
        '''
        1. 用栈划分单元（逗号，直接相邻区间）
        2. 递归处理单元，返回集合
        3. 排列组合
        3. 合并集合
        '''
        for od in range(97, 123):
            expression.replace(chr(od), "{" + chr(od) + "}")
        expression.replace("}{", "}+{")
        def process(s: str) -> Set[str]:

# @lc code=end

