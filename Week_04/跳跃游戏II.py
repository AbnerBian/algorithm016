class Solution:
    def jump(self, nums: List[int]) -> int:
        if(len(nums)<2):return 0
        maxi=nums[0]
        end=nums[0]
        res=1
        for i ,jump in enumerate(nums):
            maxi=max(maxi,i+jump)
            if(i==end):
                if(end<len(nums)-1):
                    res+=1
                    end=maxi
                    if(end>=len(nums)-1):
                        return res
        return res