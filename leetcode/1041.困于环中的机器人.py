#
# @lc app=leetcode.cn id=1041 lang=python3
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir = [0, 1]
        pos = [0, 0]
        for i in instructions * 4:
            if i == 'G':
                pos[0] += dir[0]
                pos[1] += dir[1]
            elif i == 'L':
                if dir == [0, 1]:
                    dir = [-1, 0]
                elif dir == [0, -1]:
                    dir = [1, 0]
                elif dir == [1, 0]:
                    dir = [0, 1]
                elif dir == [-1, 0]:
                    dir = [0, -1]
            elif i == 'R':
                if dir == [0, 1]:
                    dir = [1, 0]
                elif dir == [0, -1]:
                    dir = [-1, 0]
                elif dir == [1, 0]:
                    dir = [0, -1]
                elif dir == [-1, 0]:
                    dir = [0, 1]
        if pos == [0, 0]: return True
        else: return False
# @lc code=end

