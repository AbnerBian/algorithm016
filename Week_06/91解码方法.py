class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if(n==0):return 0
        if(s[0]=='0'):return 0
        dp=[0 for i in range(n+1)]
        dp[0]=1
        dp[1]=(1 if s[0]!='0' else 0)
        for i in range(1,n):
            dp[i+1]=(dp[i] if s[i]!='0'else 0)+\
                    (dp[i-1] if int(s[i-1:i+1])<=26 and int(s[i-1:i+1])>=10 else 0)
        return dp[-1]