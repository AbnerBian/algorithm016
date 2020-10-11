class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0
        for i,jump in enumerate(nums[:-1]):
            if(maxi>=i and i+jump>maxi):
                maxi=i+jump
        return maxi>=len(nums)-1