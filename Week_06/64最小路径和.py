import functools
class Solution:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        res=float('inf')
        if(not grid):return 0
        m=len(grid)
        n=len(grid[0])
        @functools.lru_cache()
        def helper(i,j,tmp):
            nonlocal res
            if(i>=0 and i<m and j>=0 and j<n):

                if(i==m-1 and j==n-1):
                    res=min(res,tmp+grid[i][j])
                else:
                    tmp+=grid[i][j]
                    helper(i+1, j, tmp)
                    helper(i, j+1, tmp)
                    tmp-=grid[i][j]
        helper(0,0,0)
        return res
                
class Solution:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        if(not grid):
            return 0
        m=len(grid)
        n=len(grid[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if(i==0):
                dp[i][0]=grid[i][0]
            else:
                dp[i][0]=grid[i][0]+dp[i-1][0]
        for i in range(n):
            if(i==0):
                dp[0][i]=grid[0][i]
            else:
                dp[0][i]=grid[0][i]+dp[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
       
        return dp[-1][-1]