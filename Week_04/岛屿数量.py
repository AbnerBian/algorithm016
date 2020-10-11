class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if(grid==[]):return 0
        rownum=len(grid)
        colnum=len(grid[0])
        def helper(i,j):
            if( i>=0 and i<rownum and j>=0 and j<colnum and grid[i][j]=='1' ):
                grid[i][j]='0'
                helper(i-1,j)
                helper(i+1,j)
                helper(i,j-1)
                helper(i,j+1)
        if(not grid):
            return 0
        
        count=0
        for i in range(rownum):
            for j in range(colnum):
                if(grid[i][j]=='1'):
                    count+=1
                    helper(i,j)
        return count