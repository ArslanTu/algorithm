from typing import List

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        max_k = None
        if num2 < 0:
            max_k = 10 ** 3
        elif num2 == 0:
            return bin(num1).count('1')
        else:
            max_k = num1 // num2
        for k in range(1, max_k + 1):
            num3 = num1 - k * num2
            bin_num3 = bin(num3)[2:]
            num_of_1 = bin_num3.count('1')
            bin_num3 = bin_num3[::-1]
            ops_num = 0
            for i in range(len(bin_num3)):
                if bin_num3[i] == '1':
                    ops_num += i + 1
            if num_of_1 <= k <= ops_num:
                return k
        return -1

params = [(3, -2, 3), (5, 7, -1)]
sl = Solution()
for num1, num2, ans in params:
    print(f"{sl.makeTheIntegerZero(num1, num2)} {ans}")