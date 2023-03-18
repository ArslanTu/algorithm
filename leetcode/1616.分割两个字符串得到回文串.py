#
# @lc app=leetcode.cn id=1616 lang=python3
#
# [1616] 分割两个字符串得到回文串
#

# @lc code=start
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        '''
        枚举分割点？超时。
        先计算 s1 前缀和 s2 后缀的逆序的最大相同长度
        如果长度超过一半，一定 True
        否则分两种情况，中间部分取 s1 或中间部分取 s2
        任意一种情况成立即可
        将 a 和 b 分别作为 s1 s2 检查一次
        '''
        if a == a[::-1] or b == b[::-1]:
            return True
        
        def check(s1: str, s2:str) -> bool:
            n = len(s1)

            # 计算相同长度
            break_point = -1
            for idx in range(n):
                if s2[idx] == s1[-1 - idx]:
                    break_point = idx
                else:
                    break
            
            # 相同长度短于一半
            if -1 < break_point < (n - 1) // 2:
                surplus_1 = s1[break_point + 1:n - 1 - break_point]
                surplus_2 = s2[break_point + 1:n - 1 - break_point]
                if surplus_1 == surplus_1[::-1] or surplus_2 == surplus_2[::-1]:
                    return True
            # 相同长度长于一半
            elif break_point >= (n - 1) // 2:
                return True
            
            return False
        
        return check(a, b) or check(b, a)

# @lc code=end

sl = Solution()
p1 = "pvhmupgqeltozftlmfjjde"
p2 = "yjgpzbezspnnpszebzmhvp"
print(sl.checkPalindromeFormation(p1 ,p2))