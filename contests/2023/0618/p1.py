from typing import List

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5:
            ans += 50
            mainTank -= 5
            if additionalTank:
                additionalTank -= 1
                mainTank += 1
        ans += mainTank * 10
        return ans

sl = Solution()

cases = ()
for p1 in cases:
    print(sl)