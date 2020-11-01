class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<=2):return n
        f1=1
        f2=2
        for i in range(2,n):
            f3=f1+f2
            f1=f2
            f2=f3
        return f3

import functools

class Solution:
    @functools.lru_cache
    def climbStairs(self, n: int) -> int:
        if(n<=2):return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)