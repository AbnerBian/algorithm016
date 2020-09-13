#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if(not height):
            return 0
        left=0
        right=len(height)-1
        maxleft=height[left]
        maxright=height[right]
        ans=0
        while(left<right):
            maxleft=max(maxleft,height[left])
            maxright=max(maxright,height[right])
            if(maxleft<maxright):
                ans+=maxleft-height[left]
                left+=1
            else:
                ans+=maxright-height[right]
                right-=1
        return ans



# @lc code=end

