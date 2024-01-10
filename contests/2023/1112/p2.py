from typing import *

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def cal(s1, s2):
            dh = int(s2[:2]) - int(s1[:2])
            dm = int(s2[2:]) - int(s1[2:])
            total = dh * 60 + dm
            return total
        
        access_times.sort(key=lambda x: x[1])
        ans = set()
        men = {}
        for name, time in access_times:
            if men.get(name, None) == None:
                men[name] = []
            men[name].append(time)
            if len(men[name]) > 2 and cal(men[name][-3], men[name][-1]) < 60:
                ans.add(name)
        return list(ans)

sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")