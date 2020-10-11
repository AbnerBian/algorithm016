class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=0#第i个孩子
        j=0#第j个饼干
        g.sort()
        s.sort()
        count=0
        while(True):
            if(j==len(s)or i==len(g)):
                return count
            if(s[j]>=g[i]):
                count+=1
                j+=1
                i+=1
            elif(s[j]<g[i]):
                j+=1