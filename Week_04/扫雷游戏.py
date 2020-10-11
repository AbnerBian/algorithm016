class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        rownum=len(board)
        colnum=len(board[0])

        def caculate(i,j):
            ''' 假设i，j符合边界条件 '''
            count=0
            for row in [-1,0,1]:
                for col in [-1,0,1]:
                    if(row==0 and col==0):continue
                    if(i+row>=0 and i+row<rownum and j+col>=0 and j+col<colnum and board[i+row][col+j]=='M' ):
                        count+=1
            return count
        def helper(i,j):
            if(i>=0 and i<rownum and j>=0 and j<colnum):
                if(caculate(i,j)>0 and board[i][j]=='E'):
                    board[i][j]=str(caculate(i,j))
                    return
                elif(board[i][j]=='E'):
                    board[i][j]='B'
                    for row in [-1,0,1]:
                        for col in [-1,0,1]:
                            if(row==0 and col==0):continue
                            helper(i+row,j+col)
                        
        clicki=click[0]
        clickj=click[1]
        if(board[clicki][clickj]=='M'):
            board[clicki][clickj]='X'
        helper(clicki,clickj)
        return board